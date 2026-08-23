# Demo Infrastructure Architecture

## Overview

The fictional infrastructure is composed of a small set of containerized services.

## Components

### API Service

The API service receives requests from users and forwards them to the appropriate application components.

### Agent Core

The Agent Core manages agent registration and execution.

### Knowledge Core

The Knowledge Core is responsible for locating and retrieving relevant Markdown documents.

### LLM Provider

The LLM Provider receives the prepared context and generates the final response.

## Request Flow

User
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
LLM Provider
↓
Response
