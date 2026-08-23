# Demo Infrastructure Services

## API

The API exposes the application interface.

Its initial responsibility is to receive chat requests and return agent responses.

## Infrastructure Agent

The Infrastructure Agent specializes in infrastructure knowledge.

It receives user questions and requests relevant knowledge documents.

## Knowledge Provider

The Knowledge Provider reads Markdown documents from the configured knowledge path.

The initial implementation uses simple text retrieval.

## Context Builder

The Context Builder combines:

- Agent instructions
- Relevant knowledge
- User question

The resulting context is sent to the configured LLM.

## LLM Provider

The LLM Provider abstracts communication with the configured language model.

The application core should not depend directly on a specific model provider.
