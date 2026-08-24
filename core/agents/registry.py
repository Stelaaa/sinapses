from .base import BaseAgent


class AgentRegistry:
    """Registro central dos agentes disponíveis na plataforma."""

    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """Registra um agente utilizando seu nome como identificador."""
        if not agent.name:
            raise ValueError("O agente precisa possuir um nome.")

        if agent.name in self._agents:
            raise ValueError(f"O agente '{agent.name}' já está registrado.")

        self._agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent:
        """Retorna um agente registrado pelo nome."""
        try:
            return self._agents[name]
        except KeyError:
            raise KeyError(f"Agente '{name}' não encontrado.")

    def list_agents(self) -> list[str]:
        """Retorna os nomes dos agentes registrados."""
        return list(self._agents.keys())
