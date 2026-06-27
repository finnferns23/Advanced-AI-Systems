from __future__ import annotations

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import streamlit as st
from dotenv import load_dotenv

from atlas_ai_intelligent_studio.assistant import AtlasAssistant
from atlas_ai_intelligent_studio.config import Settings, choose_secret
from atlas_ai_intelligent_studio.ingest import read_uploaded_file
from atlas_ai_intelligent_studio.mcp import mcp_run_hint, validate_mcp_config
from atlas_ai_intelligent_studio.rag import MemoryIndex
from atlas_ai_intelligent_studio.text import safe_filename

load_dotenv()
settings = Settings.from_env()
settings.data_dir.mkdir(parents=True, exist_ok=True)

st.set_page_config(page_title=settings.app_name, page_icon="🧭", layout="wide")

if "memory_index" not in st.session_state:
    st.session_state.memory_index = MemoryIndex(chunk_size=settings.chunk_size, overlap=settings.overlap)
if "last_answer" not in st.session_state:
    st.session_state.last_answer = ""
if "last_sources" not in st.session_state:
    st.session_state.last_sources = []
if "run_count" not in st.session_state:
    st.session_state.run_count = 0

with st.sidebar:
    st.header("Setup")
    key_input = st.text_input("OpenAI API key", type="password", value="", help="Use .env for persistent local secrets.")
    api_key = choose_secret(key_input, settings.openai_api_key)
    model = st.text_input("Reasoning model", value=settings.model)
    voice = st.selectbox(
        "Voice output",
        ["alloy", "ash", "ballad", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer", "verse"],
        index=7,
    )
    st.divider()
    st.subheader("Runtime status")
    st.metric("API key", "Loaded" if api_key else "Missing")
    st.metric("Knowledge chunks", st.session_state.memory_index.count)
    st.metric("Runs", st.session_state.run_count)
    st.caption("Secrets are loaded from .env or the current session only.")

st.title("🧭 Atlas AI Intelligent Studio")
st.caption(settings.app_tagline)

status_1, status_2, status_3, status_4 = st.columns(4)
status_1.metric("Assistant", "Ready" if api_key else "Needs key")
status_2.metric("Knowledge", f"{st.session_state.memory_index.count} chunks")
status_3.metric("Vision", "Enabled")
status_4.metric("MCP", "Dry check")

st.info(
    "Use this dashboard as a single AI workspace: plan, answer, analyze files and images, create voice output, "
    "and prepare MCP/browser automation safely."
)

command_tab, knowledge_tab, vision_tab, voice_tab, mcp_tab, diagnostics_tab = st.tabs(
    ["Command Center", "Knowledge Base", "Vision", "Voice", "MCP Planner", "Diagnostics"]
)


def build_assistant() -> AtlasAssistant:
    return AtlasAssistant(api_key=api_key, model=model, audio_model=settings.audio_model)


with command_tab:
    st.subheader("Command Center")
    mode = st.selectbox(
        "Workflow",
        ["General assistant", "Ask knowledge base", "Implementation plan", "Business automation plan", "Risk and validation review"],
    )
    prompt = st.text_area("Request", height=180, placeholder="Ask for a plan, explanation, review, implementation, or workflow...")
    make_audio = st.checkbox("Create MP3 from answer", value=False)

    if st.button("Run", type="primary"):
        if not prompt.strip():
            st.error("Enter a request.")
        elif not api_key:
            st.error("Add an OpenAI API key in the sidebar or .env file.")
        else:
            try:
                with st.spinner("Generating..."):
                    context_chunks = []
                    instruction = prompt.strip()
                    if mode == "Ask knowledge base":
                        context_chunks = st.session_state.memory_index.search(prompt, limit=5)
                    elif mode == "Implementation plan":
                        instruction = "Create a production-minded implementation plan with clear validation steps.\n\n" + instruction
                    elif mode == "Business automation plan":
                        instruction = "Create a safe business automation plan with inputs, outputs, checks, risks, and rollback steps.\n\n" + instruction
                    elif mode == "Risk and validation review":
                        instruction = "Review the request for risks, missing requirements, validation checks, and production readiness.\n\n" + instruction

                    answer = build_assistant().respond(instruction, context_chunks)
                    st.session_state.last_answer = answer
                    st.session_state.last_sources = sorted({chunk.source for chunk in context_chunks})
                    st.session_state.run_count += 1
                    st.write(answer)

                    if context_chunks:
                        st.subheader("Retrieved context")
                        for chunk in context_chunks:
                            with st.expander(chunk.source):
                                st.write(chunk.text)

                    if make_audio:
                        audio_path = build_assistant().create_audio(answer, settings.data_dir / "audio", voice)
                        st.audio(str(audio_path))
                        st.download_button("Download MP3", audio_path.read_bytes(), file_name=audio_path.name, mime="audio/mpeg")
            except Exception as exc:
                st.error(str(exc))

with knowledge_tab:
    st.subheader("Knowledge Base")
    st.write("Upload TXT, Markdown, or PDF files to build a lightweight local memory index for the current session.")
    uploads = st.file_uploader("Documents", type=["txt", "md", "pdf"], accept_multiple_files=True)
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("Add to knowledge"):
            if not uploads:
                st.warning("Upload at least one document.")
            else:
                total = 0
                sources = []
                for item in uploads:
                    source = safe_filename(item.name)
                    text = read_uploaded_file(item.name, item.getvalue())
                    total += st.session_state.memory_index.add_document(source, text)
                    sources.append(source)
                st.session_state.last_sources = sorted(set(st.session_state.last_sources + sources))
                st.success(f"Added {total} chunks from {len(sources)} file(s).")
    with col_b:
        if st.button("Clear knowledge"):
            st.session_state.memory_index = MemoryIndex(chunk_size=settings.chunk_size, overlap=settings.overlap)
            st.session_state.last_sources = []
            st.success("Session knowledge cleared.")

with vision_tab:
    st.subheader("Vision")
    image_upload = st.file_uploader("Image", type=["png", "jpg", "jpeg", "webp"])
    image_question = st.text_area("Question about the image", value="Analyze this image and summarize the important details.", height=120)
    if st.button("Analyze image"):
        if not api_key:
            st.error("Add an OpenAI API key in the sidebar or .env file.")
        elif not image_upload:
            st.error("Upload an image first.")
        else:
            try:
                with st.spinner("Analyzing image..."):
                    answer = build_assistant().analyze_image(image_upload.getvalue(), image_upload.type or "image/png", image_question)
                    st.session_state.last_answer = answer
                    st.session_state.run_count += 1
                    st.write(answer)
            except Exception as exc:
                st.error(str(exc))

with voice_tab:
    st.subheader("Voice")
    text_for_audio = st.text_area("Text to convert", value=st.session_state.last_answer, height=180)
    if st.button("Create voice file"):
        if not api_key:
            st.error("Add an OpenAI API key in the sidebar or .env file.")
        elif not text_for_audio.strip():
            st.error("Enter text or generate an answer first.")
        else:
            try:
                audio_path = build_assistant().create_audio(text_for_audio.strip(), settings.data_dir / "audio", voice)
                st.audio(str(audio_path))
                st.download_button("Download MP3", audio_path.read_bytes(), file_name=audio_path.name, mime="audio/mpeg")
            except Exception as exc:
                st.error(str(exc))

with mcp_tab:
    st.subheader("MCP Planner")
    mcp_path = Path(st.text_input("MCP config path", value="config/mcp_agent.config.yaml"))
    ok, message = validate_mcp_config(mcp_path)
    st.write(("✅ " if ok else "⚠️ ") + message)
    st.code(mcp_run_hint(mcp_path), language="powershell")
    plan_prompt = st.text_area(
        "Planning request",
        value="Create a safe MCP/browser automation workflow for researching a company website and summarizing useful business information.",
        height=140,
    )
    if st.button("Create MCP plan"):
        if not api_key:
            st.error("Add an OpenAI API key in the sidebar or .env file.")
        else:
            try:
                instruction = (
                    "Create a safe MCP/browser automation plan. Do not claim execution. "
                    "Include config checks, commands, expected outputs, risk controls, and failure handling.\n\n"
                    + plan_prompt.strip()
                )
                answer = build_assistant().respond(instruction)
                st.session_state.last_answer = answer
                st.session_state.run_count += 1
                st.write(answer)
            except Exception as exc:
                st.error(str(exc))

with diagnostics_tab:
    st.subheader("Diagnostics")
    st.write("Use these checks before committing or deploying the project.")
    st.code("python -m compileall app.py src tests\npython -m pytest -q", language="powershell")
    st.write("Configuration flags")
    st.json(
        {
            "app_name": settings.app_name,
            "model": model,
            "audio_model": settings.audio_model,
            "voice": voice,
            "chunk_size": settings.chunk_size,
            "chunk_overlap": settings.overlap,
            "data_dir": str(settings.data_dir),
            "api_key_loaded": bool(api_key),
        }
    )

st.divider()
st.caption("Atlas AI Intelligent Studio provides one consistent production-focused application surface with modular local services.")
