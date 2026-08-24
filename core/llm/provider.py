from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """Contrato para provedores de modelos de linguagem."""

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Gera uma resposta a partir de um prompt."""
        raise NotImplementedError
