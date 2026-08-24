from core.agents.base import BaseAgent
from core.context import ContextBuilder
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
        context_builder: ContextBuilder | None = None,
    ) -> None:
        self.llm_provider = llm_provider
        self.knowledge_provider = knowledge_provider
        self.context_builder = context_builder or ContextBuilder()

    def execute(self, message: str) -> str:
        document_names = self.knowledge_provider.search(message)

        knowledge = "\n\n".join(
            self.knowledge_provider.get_document(name)
            for name in document_names
        )

        context = self.context_builder.build(
            instructions=self.instructions,
            question=message,
            knowledge=knowledge,
        )

        return self.llm_provider.generate(context)
