from pathlib import Path

from atlas_ai_intelligent_studio.config import Settings, choose_secret
from atlas_ai_intelligent_studio.mcp import validate_mcp_config
from atlas_ai_intelligent_studio.rag import MemoryIndex
from atlas_ai_intelligent_studio.text import chunk_text, safe_filename


def test_chunk_text_overlap_validation():
    assert chunk_text("hello world", chunk_size=20, overlap=5) == ["hello world"]


def test_safe_filename_removes_unsafe_characters():
    assert safe_filename("../bad file!!.txt") == "bad_file_.txt"


def test_memory_index_retrieves_relevant_document():
    index = MemoryIndex()
    index.add_document("profile.txt", "Finn builds accessible AI assistants with RAG and voice output.")
    results = index.search("accessible voice RAG")
    assert results
    assert results[0].source == "profile.txt"


def test_mcp_missing_config_is_safe():
    ok, message = validate_mcp_config(Path("missing.yaml"))
    assert ok is False
    assert "not found" in message.lower()


def test_settings_defaults_are_atlas_branded():
    settings = Settings.from_env()
    assert settings.app_name == "Atlas AI Intelligent Studio"


def test_choose_secret_prefers_session_value():
    assert choose_secret("session-key", "env-key") == "session-key"
