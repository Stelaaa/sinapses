from agents.infrastructure.agent import InfrastructureAgent
from core.llm.provider import LLMProvider


class FakeLLMProvider(LLMProvider):
    def __init__(self):
        self.last_prompt = None

    def generate(self, prompt: str) -> str:
        self.last_prompt = prompt
        return "Resposta simulada."


def test_infrastructure_agent_uses_llm_provider():
    provider = FakeLLMProvider()
    agent = InfrastructureAgent(provider)

    response = agent.execute("O que é um servidor?")

    assert response == "Resposta simulada."
    assert provider.last_prompt is not None
    assert "O que é um servidor?" in provider.last_prompt
    assert "Infrastructure Agent" in provider.last_prompt
