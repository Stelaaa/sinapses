from abc import ABC, abstractmethod


class KnowledgeProvider(ABC):
    """Contrato base para provedores de conhecimento."""

    @abstractmethod
    def load(self) -> None:
        """Carrega a base de conhecimento."""
        raise NotImplementedError

    @abstractmethod
    def search(self, query: str) -> list[str]:
        """Busca conteúdo relevante para uma consulta."""
        raise NotImplementedError

    @abstractmethod
    def get_document(self, name: str) -> str:
        """Retorna o conteúdo de um documento carregado."""
        raise NotImplementedError
