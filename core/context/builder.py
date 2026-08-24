class ContextBuilder:
    """Constrói o contexto que será enviado ao provedor de LLM."""

    def build(
        self,
        *,
        instructions: str,
        question: str,
        knowledge: str,
    ) -> str:
        return (
            f"{instructions}\n\n"
            f"Conhecimento relevante:\n{knowledge}\n\n"
            f"Pergunta do usuário:\n{question}"
        )
