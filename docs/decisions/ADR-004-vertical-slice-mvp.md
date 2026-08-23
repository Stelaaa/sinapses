# ADR-004 — MVP por fatia vertical

## Status

Aceito

## Contexto

A arquitetura futura possui diversos componentes que não precisam ser implementados antes da validação da primeira funcionalidade.

## Decisão

O desenvolvimento inicial seguirá uma estratégia de fatia vertical.

Será implementado o menor conjunto de componentes necessário para executar o fluxo completo:

Question
↓
API
↓
Agent
↓
Knowledge
↓
Context
↓
LLM
↓
Answer

## Consequências

### Positivas

- validação rápida;
- redução de complexidade prematura;
- entrega funcional antecipada.

### Negativas

- alguns componentes avançados serão adiados.
