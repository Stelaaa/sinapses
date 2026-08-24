# Serviços da Infraestrutura — Demonstração

## API

A API expõe a interface da aplicação.

Sua responsabilidade inicial é receber solicitações de chat e retornar
as respostas dos agentes.

## Infrastructure Agent

O Infrastructure Agent é especializado em conhecimento de infraestrutura.

Ele recebe perguntas dos usuários e solicita ao provedor de conhecimento
os documentos relevantes.

## Provedor de Conhecimento

O Provedor de Conhecimento lê documentos Markdown a partir do caminho
de conhecimento configurado.

A implementação inicial utiliza recuperação textual simples.

## Context Builder

O Context Builder combina:

- Instruções do agente
- Conhecimento relevante
- Pergunta do usuário

O contexto resultante é enviado ao provedor de LLM.

## Provedor de LLM

O Provedor de LLM abstrai a comunicação com o modelo de linguagem configurado.

O núcleo da aplicação não deve depender diretamente de um provedor
específico de modelo.
