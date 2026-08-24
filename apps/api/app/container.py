import os

from agents.infrastructure.agent import InfrastructureAgent
from core.agents.registry import AgentRegistry
from core.context import ContextBuilder
from core.knowledge.markdown import MarkdownKnowledgeProvider
from core.llm.ollama import OllamaProvider


def create_agent_registry() -> AgentRegistry:
    """Cria e configura o registro de agentes da aplicação."""

    model = os.getenv("LLM_MODEL", "llama3.2:latest")
    api_url = os.getenv(
        "LLM_API_URL",
        "http://localhost:11434",
    )
    knowledge_path = os.getenv(
        "KNOWLEDGE_PATH",
        "/data/knowledge",
    )

    llm_provider = OllamaProvider(
        model=model,
        api_url=api_url,
    )

    knowledge_provider = MarkdownKnowledgeProvider(
        knowledge_path=knowledge_path,
    )

    knowledge_provider.load()

    context_builder = ContextBuilder()

    infrastructure_agent = InfrastructureAgent(
        llm_provider=llm_provider,
        knowledge_provider=knowledge_provider,
        context_builder=context_builder,
    )

    registry = AgentRegistry()
    registry.register(infrastructure_agent)

    return registry
