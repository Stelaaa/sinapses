from agents.infrastructure.agent import InfrastructureAgent
from core.knowledge.provider import KnowledgeProvider
from core.llm.provider import LLMProvider


class FakeLLMProvider(LLMProvider):
    def __init__(self):
        self.last_prompt = None

    def generate(self, prompt: str) -> str:
        self.last_prompt = prompt
        return "Resposta simulada."


def test_infrastructure_agent_uses_llm_provider():
    llm_provider = FakeLLMProvider()
    knowledge_provider = FakeKnowledgeProvider()

    agent = InfrastructureAgent(
        llm_provider=llm_provider,
        knowledge_provider=knowledge_provider,
    )

    response = agent.execute("O que é um servidor?")

    assert response == "Resposta simulada."
    assert llm_provider.last_prompt is not None
    assert "O que é um servidor?" in llm_provider.last_prompt
    assert "Infrastructure Agent" in llm_provider.last_prompt


class FakeKnowledgeProvider(KnowledgeProvider):
    def __init__(self):
        self.last_query = None
        self.documents = {
            "architecture.md": "Conteúdo simulado de arquitetura."
        }

    def load(self) -> None:
        pass

    def search(self, query: str) -> list[str]:
        self.last_query = query
        return ["architecture.md"]

    def get_document(self, name: str) -> str:
        return self.documents[name]


def test_infrastructure_agent_uses_knowledge_provider():
    llm_provider = FakeLLMProvider()
    knowledge_provider = FakeKnowledgeProvider()

    agent = InfrastructureAgent(
        llm_provider=llm_provider,
        knowledge_provider=knowledge_provider,
    )

    response = agent.execute("Como funciona o Agent Core?")

    assert response == "Resposta simulada."
    assert knowledge_provider.last_query == "Como funciona o Agent Core?"
    assert "Conteúdo simulado de arquitetura." in llm_provider.last_prompt


class KnowledgeAwareFakeProvider(KnowledgeProvider):
    def __init__(self):
        self.last_query = None
        self.documents = {
            "architecture.md": (
                "# Demo Infrastructure Architecture\n\n"
                "The Agent Core manages agent registration and execution."
            )
        }

    def load(self) -> None:
        pass

    def search(self, query: str) -> list[str]:
        self.last_query = query
        return ["architecture.md"]

    def get_document(self, name: str) -> str:
        return self.documents[name]


def test_infrastructure_agent_includes_knowledge_content_in_prompt():
    llm_provider = FakeLLMProvider()
    knowledge_provider = KnowledgeAwareFakeProvider()

    agent = InfrastructureAgent(
        llm_provider=llm_provider,
        knowledge_provider=knowledge_provider,
    )

    agent.execute("Como funciona o Agent Core?")

    assert knowledge_provider.last_query == "Como funciona o Agent Core?"
    assert "Agent Core manages agent registration and execution" in (
        llm_provider.last_prompt
    )
