from fastapi.testclient import TestClient

from agents.infrastructure.agent import InfrastructureAgent
from apps.api.app.main import create_app
from core.agents.registry import AgentRegistry
from core.knowledge.provider import KnowledgeProvider
from core.llm.provider import LLMProvider


class FakeLLMProvider(LLMProvider):
    def generate(self, prompt: str) -> str:
        return "Resposta simulada pelo provider de teste."


class FakeKnowledgeProvider(KnowledgeProvider):
    def load(self) -> None:
        pass

    def search(self, query: str) -> list[str]:
        return []

    def get_document(self, name: str) -> str:
        raise KeyError(f"Documento '{name}' não encontrado.")


def create_test_client() -> TestClient:
    llm_provider = FakeLLMProvider()
    knowledge_provider = FakeKnowledgeProvider()
    agent = InfrastructureAgent(
        llm_provider=llm_provider,
        knowledge_provider=knowledge_provider,
    )

    registry = AgentRegistry()
    registry.register(agent)

    app = create_app(registry)

    return TestClient(app)


def test_health():
    client = create_test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat():
    client = create_test_client()

    response = client.post(
        "/chat",
        json={
            "agent": "infrastructure",
            "message": "O que é um servidor?",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "agent": "infrastructure",
        "answer": "Resposta simulada pelo provider de teste.",
    }


def test_chat_unknown_agent():
    client = create_test_client()

    response = client.post(
        "/chat",
        json={
            "agent": "unknown",
            "message": "Teste",
        },
    )

    assert response.status_code == 404


def test_chat_empty_message():
    client = create_test_client()

    response = client.post(
        "/chat",
        json={
            "agent": "infrastructure",
            "message": "",
        },
    )

    assert response.status_code == 422
