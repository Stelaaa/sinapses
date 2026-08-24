import os

from agents.infrastructure.agent import InfrastructureAgent
from core.agents.registry import AgentRegistry
from core.llm.ollama import OllamaProvider


def create_agent_registry() -> AgentRegistry:
    """Cria e configura o registro de agentes da aplicação."""

    model = os.getenv("LLM_MODEL", "llama3.2:latest")
    api_url = os.getenv(
        "LLM_API_URL",
        "http://localhost:11434",
    )

    llm_provider = OllamaProvider(
        model=model,
        api_url=api_url,
    )

    infrastructure_agent = InfrastructureAgent(
        llm_provider=llm_provider,
    )

    registry = AgentRegistry()
    registry.register(infrastructure_agent)

    return registry
