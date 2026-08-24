from core.agents.base import BaseAgent
from core.agents.registry import AgentRegistry


class FakeAgent(BaseAgent):
    name = "fake"
    description = "Agente utilizado nos testes."
    instructions = "Responda aos testes."

    def execute(self, message: str) -> str:
        return f"Resposta: {message}"


def test_agent_registry_register_and_get():
    registry = AgentRegistry()
    agent = FakeAgent()

    registry.register(agent)

    assert registry.list_agents() == ["fake"]
    assert registry.get("fake") is agent


def test_agent_registry_rejects_duplicate_agent():
    registry = AgentRegistry()
    agent = FakeAgent()

    registry.register(agent)

    try:
        registry.register(agent)
        assert False, "Era esperado ValueError"
    except ValueError as exc:
        assert "já está registrado" in str(exc)


def test_agent_registry_rejects_unknown_agent():
    registry = AgentRegistry()

    try:
        registry.get("unknown")
        assert False, "Era esperado KeyError"
    except KeyError as exc:
        assert "não encontrado" in str(exc)
