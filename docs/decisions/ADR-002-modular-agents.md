# ADR-002 — Arquitetura modular de agentes

## Status

Aceito

## Contexto

A plataforma deverá suportar múltiplos agentes especializados no futuro.

## Decisão

Os agentes serão implementados como módulos independentes construídos sobre um núcleo reutilizável.

O MVP implementará inicialmente apenas um agente:

Infrastructure Agent.

## Consequências

### Positivas

- permite adicionar novos agentes;
- evita dependência direta do núcleo em um agente específico;
- favorece reutilização.

### Negativas

- adiciona uma abstração inicial mesmo com apenas um agente.
