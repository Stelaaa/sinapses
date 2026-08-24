from core.agents.base import BaseAgent
from core.knowledge.provider import KnowledgeProvider
from core.llm.provider import LLMProvider


class InfrastructureAgent(BaseAgent):
    """Agente especializado em infraestrutura."""

    name = "infrastructure"
    description = "Agente especializado em infraestrutura."
    instructions = (
        "Você é o Infrastructure Agent do Sinapses. "
        "Responda de forma objetiva e clara. "
        "Não invente informações."
    )

    def __init__(
        self,
        llm_provider: LLMProvider,
        knowledge_provider: KnowledgeProvider,
    ) -> None:
        self.llm_provider = llm_provider
        self.knowledge_provider = knowledge_provider

    def execute(self, message: str) -> str:
        document_names = self.knowledge_provider.search(message)

        knowledge = "\n\n".join(
            self.knowledge_provider.get_document(name)
            for name in document_names
        )

        prompt = (
            f"{self.instructions}\n\n"
            f"Conhecimento relevante:\n{knowledge}\n\n"
            f"Usuário: {message}"
        )

        return self.llm_provider.generate(prompt)
