# Arquitetura da Infraestrutura — Demonstração

## Visão geral

A infraestrutura fictícia é composta por um pequeno conjunto de serviços
containerizados.

## Componentes

### Serviço de API

O Serviço de API recebe solicitações dos usuários e encaminha essas
solicitações para os componentes apropriados da aplicação.

### Núcleo de Agentes

O Núcleo de Agentes gerencia o registro e a execução dos agentes.

### Núcleo de Conhecimento

O Núcleo de Conhecimento é responsável por localizar e recuperar
documentos Markdown relevantes.

### Provedor de LLM

O Provedor de LLM recebe o contexto preparado e gera a resposta final.

## Fluxo de solicitação

Usuário
↓
API
↓
Núcleo de Agentes
↓
Infrastructure Agent
↓
Núcleo de Conhecimento
↓
Context Builder
↓
Provedor de LLM
↓
Resposta
