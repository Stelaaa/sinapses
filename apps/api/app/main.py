from fastapi import FastAPI, HTTPException

from .container import create_agent_registry
from .models import ChatRequest, ChatResponse
from core.agents.registry import AgentRegistry


def create_app(agent_registry: AgentRegistry | None = None) -> FastAPI:
    """Cria a aplicação FastAPI."""

    app = FastAPI(
        title="Sinapses API",
        description=(
            "API da plataforma modular para agentes de IA "
            "orientados por conhecimento."
        ),
        version="0.1.0",
    )

    registry = agent_registry or create_agent_registry()

    @app.get("/health")
    def health() -> dict[str, str]:
        """Verifica se a API está funcionando."""
        return {"status": "ok"}

    @app.post("/chat", response_model=ChatResponse)
    def chat(request: ChatRequest) -> ChatResponse:
        """Envia uma mensagem para um agente."""

        try:
            agent = registry.get(request.agent)
        except KeyError as exc:
            raise HTTPException(
                status_code=404,
                detail=str(exc),
            ) from exc

        answer = agent.execute(request.message)

        return ChatResponse(
            agent=agent.name,
            answer=answer,
        )

    return app
