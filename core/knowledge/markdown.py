from pathlib import Path
import re

from .provider import KnowledgeProvider


class MarkdownKnowledgeProvider(KnowledgeProvider):
    """Provedor de conhecimento baseado em arquivos Markdown."""

    def __init__(self, knowledge_path: str | Path) -> None:
        self.knowledge_path = Path(knowledge_path)
        self.documents: dict[str, str] = {}

    def load(self) -> None:
        """Carrega os documentos Markdown referenciados pelo index.md."""
        if not self.knowledge_path.exists():
            raise FileNotFoundError(
                f"Base de conhecimento não encontrada: {self.knowledge_path}"
            )

        if not self.knowledge_path.is_dir():
            raise NotADirectoryError(
                f"O caminho do conhecimento não é um diretório: "
                f"{self.knowledge_path}"
            )

        index_path = self.knowledge_path / "index.md"

        if not index_path.exists():
            raise FileNotFoundError(
                f"index.md não encontrado em: {self.knowledge_path}"
            )

        index_content = index_path.read_text(encoding="utf-8")

        references = re.findall(
            r"(?m)^\s*-\s+([^\s]+\.md)\s*$",
            index_content,
        )

        self.documents.clear()

        for reference in references:
            document_path = self.knowledge_path / reference

            if not document_path.exists():
                raise FileNotFoundError(
                    f"Documento referenciado pelo index.md não encontrado: "
                    f"{document_path}"
                )

            if not document_path.is_file():
                raise FileNotFoundError(
                    f"Documento referenciado pelo index.md não é um arquivo: "
                    f"{document_path}"
                )

            self.documents[reference] = document_path.read_text(
                encoding="utf-8"
            )

    def get_document(self, name: str) -> str:
        """Retorna o conteúdo de um documento carregado."""
        try:
            return self.documents[name]
        except KeyError as exc:
            raise KeyError(
                f"Documento '{name}' não foi carregado."
            ) from exc

    def search(self, query: str) -> list[str]:
        """Busca documentos relevantes por correspondência textual."""
        if not query.strip():
            return []

        terms = query.lower().split()
        scored_documents: list[tuple[str, int]] = []

        for name, content in self.documents.items():
            normalized_content = content.lower()

            score = sum(
                1 for term in terms if term in normalized_content
            )

            if score > 0:
                scored_documents.append((name, score))

        scored_documents.sort(
            key=lambda item: (-item[1], item[0])
        )

        return [
            name
            for name, _score in scored_documents
        ]
