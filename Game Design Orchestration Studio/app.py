from __future__ import annotations

import json

import streamlit as st

from main import run_pipeline
from schemas import GameBrief
from tools.report_builder import build_markdown_report


st.set_page_config(page_title="Game Design Agent Team", layout="wide")
st.title("Game Design Agent Team")
st.caption("Advanced multi-agent AI system for text, voice, image, audio, video, dynamic systems, and interactive game design.")

with st.sidebar:
    st.header("Game Brief")
    title = st.text_input("Title", "Echoes of Ember")
    genre = st.text_input("Genre", "Action Adventure")
    audience = st.text_input("Audience", "Indie PC and console players")
    platform = st.text_input("Platform", "PC")
    theme = st.text_area("Theme", "Memory, survival, and discovery")
    constraints = st.text_area("Constraints", "Prototype-first, accessible, realistic indie scope")
    target_rating = st.text_input("Target Rating", "Teen")
    monetization = st.text_input("Monetization", "Premium indie release")
    run_button = st.button("Generate Game Design Package", type="primary")

if run_button:
    brief = GameBrief(title, genre, audience, platform, theme, constraints, target_rating, monetization)
    with st.spinner("Running specialist agents..."):
        package, paths = run_pipeline(brief)
    st.success("Game design package generated successfully.")
    tab_report, tab_agents, tab_json, tab_paths = st.tabs(["Report", "Agents", "JSON", "Saved Files"])
    with tab_report:
        report = build_markdown_report(package)
        st.markdown(report)
        st.download_button("Download Markdown Report", report, file_name="game_design_report.md")
    with tab_agents:
        for result in package.results:
            with st.expander(result.agent_name):
                st.write(result.summary)
                st.json(result.outputs)
                if result.risks:
                    st.warning("Risks: " + "; ".join(result.risks))
                if result.next_steps:
                    st.info("Next steps: " + "; ".join(result.next_steps))
    with tab_json:
        data = json.dumps(package.to_dict(), indent=2, ensure_ascii=False)
        st.code(data, language="json")
        st.download_button("Download JSON Package", data, file_name="game_design_package.json")
    with tab_paths:
        st.write({key: str(value) for key, value in paths.items()})
else:
    st.info("Enter a brief and generate the package. Offline deterministic mode is enabled by default; optional OpenAI live mode can be enabled with environment variables.")
