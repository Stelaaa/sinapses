from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Dados recebidos pelo endpoint de chat."""

    agent: str = Field(
        default="infrastructure",
        min_length=1,
    )
    message: str = Field(
        min_length=1,
    )


class ChatResponse(BaseModel):
    """Resposta retornada pelo endpoint de chat."""

    agent: str
    answer: str
