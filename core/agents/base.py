from abc import ABC, abstractmethod


class BaseAgent(ABC):
    """Contrato base para todos os agentes da plataforma."""

    name: str
    description: str
    instructions: str

    @abstractmethod
    def execute(self, message: str) -> str:
        """Executa o agente para uma mensagem recebida."""
        raise NotImplementedError
