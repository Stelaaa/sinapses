# Arquitetura do MVP

## Visão geral

O Sinapses é uma plataforma modular para agentes de IA orientados por conhecimento.

O MVP implementa uma fatia vertical completa da arquitetura utilizando apenas os componentes necessários para responder uma pergunta com base em uma fonte de conhecimento.

## Fluxo principal

Usuário -> API -> Agent Core -> Infrastructure Agent -> Knowledge Core -> Context Builder -> LLM Provider -> Resposta

## Componentes

### API

Recebe as requisições dos usuários e encaminha a execução para o agente selecionado.

### Agent Core

Contém o contrato base dos agentes e o mecanismo de registro. O núcleo não deve depender diretamente de um agente específico.

### Infrastructure Agent

Primeiro agente especializado implementado no MVP. É responsável por interpretar a solicitação dentro do seu escopo e utilizar a camada de conhecimento.

### Knowledge Core

Responsável pelo acesso e recuperação dos documentos relevantes. No MVP, a fonte de conhecimento será composta por arquivos Markdown.

### Context Builder

Combina instruções do agente, documentos relevantes e pergunta do usuário. O resultado é enviado ao provedor de IA.

### LLM Provider

Abstrai a comunicação com o modelo de linguagem configurado. O núcleo da aplicação não deve depender diretamente de um fornecedor específico.

## Conhecimento privado

O conhecimento real permanece externo ao repositório. A aplicação receberá o caminho através da variável KNOWLEDGE_PATH.

Em ambiente containerizado, essa base será montada como volume com acesso somente leitura.

## Estrutura lógica

Sinapses
|-- API
|-- Core
|   |-- Agents
|   |-- Knowledge
|   |-- Context
|   -- Infrastructure Agent
-- Markdown

## Princípios

- modularidade;
- separação entre código e dados privados;
- configuração externa;
- menor privilégio;
- evolução incremental;
- evitar complexidade prematura.
