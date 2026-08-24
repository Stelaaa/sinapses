from core.agents.base import BaseAgent
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

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm_provider = llm_provider

    def execute(self, message: str) -> str:
        prompt = (
            f"{self.instructions}\n\n"
            f"Usuário: {message}"
        )

        return self.llm_provider.generate(prompt)
