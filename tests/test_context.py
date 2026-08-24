from core.context import ContextBuilder


def test_context_builder_combines_instructions_question_and_knowledge() -> None:
    builder = ContextBuilder()

    context = builder.build(
        instructions="Responda utilizando o conhecimento fornecido.",
        question="O que é um servidor?",
        knowledge="Um servidor fornece serviços para outros sistemas.",
    )

    assert "Responda utilizando o conhecimento fornecido." in context
    assert "Um servidor fornece serviços para outros sistemas." in context
    assert "O que é um servidor?" in context


def test_context_builder_preserves_sections_order() -> None:
    builder = ContextBuilder()

    context = builder.build(
        instructions="INSTRUCTIONS",
        question="QUESTION",
        knowledge="KNOWLEDGE",
    )

    assert context.index("INSTRUCTIONS") < context.index("KNOWLEDGE")
    assert context.index("KNOWLEDGE") < context.index("QUESTION")

