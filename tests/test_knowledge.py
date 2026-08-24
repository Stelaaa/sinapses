from pathlib import Path

import pytest

from core.knowledge import MarkdownKnowledgeProvider


KNOWLEDGE_PATH = Path("examples/knowledge-vault/demo-infrastructure")


def test_loads_documents_from_index() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    assert "architecture.md" in provider.documents
    assert "services.md" in provider.documents


def test_loaded_document_contains_content() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    assert provider.documents["architecture.md"]
    assert provider.documents["services.md"]


def test_missing_document_referenced_by_index_raises(tmp_path: Path) -> None:
    index = tmp_path / "index.md"
    index.write_text(
        "# Knowledge\n\n- missing.md\n",
        encoding="utf-8",
    )

    provider = MarkdownKnowledgeProvider(tmp_path)

    with pytest.raises(FileNotFoundError):
        provider.load()


def test_search_returns_relevant_document() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    results = provider.search("Agent Core")

    assert "architecture.md" in results


def test_search_returns_service_document_for_knowledge_provider() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    results = provider.search("Provedor de Conhecimento")

    assert "services.md" in results


def test_search_is_case_insensitive() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    results = provider.search("agent core")

    assert "architecture.md" in results


def test_search_prioritizes_exact_phrase() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    results = provider.search("Agent Core")

    assert results[0] == "architecture.md"


def test_search_returns_empty_for_blank_query() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    assert provider.search("") == []
    assert provider.search("   ") == []


def test_get_document_returns_content() -> None:
    provider = MarkdownKnowledgeProvider(KNOWLEDGE_PATH)

    provider.load()

    content = provider.get_document("architecture.md")

    assert "# Arquitetura da Infraestrutura — Demonstração" in content
