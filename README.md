# Sinapses

> Plataforma modular para agentes de IA orientados por conhecimento.

## Visão

Sinapses é uma plataforma projetada para hospedar agentes de IA especializados que utilizam diferentes bases de conhecimento.

O projeto é construído de forma incremental, começando por uma fatia vertical funcional.

## MVP

A primeira implementação contém:

- um núcleo mínimo de agentes;
- um agente especializado em infraestrutura;
- uma base de conhecimento baseada em Markdown;
- recuperação textual simples;
- construção de contexto;
- integração com um modelo de linguagem;
- uma API para consultas;
- execução containerizada.

## Arquitetura

```text
Usuário
  ↓
API
  ↓
Agent Core
  ↓
Infrastructure Agent
  ↓
Knowledge Core
  ↓
Context Builder
  ↓
LLM
  ↓
Resposta
