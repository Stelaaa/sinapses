# ADR-001 — Conhecimento privado externo

## Status

Aceito

## Contexto

A plataforma utilizará conhecimento privado que não pode ser publicado junto ao código-fonte.

## Decisão

A base real de conhecimento permanecerá externa ao repositório.

A aplicação receberá o caminho da base através de configuração de ambiente e acesso em tempo de execução.

## Consequências

### Positivas

- evita exposição acidental de informações privadas;
- permite manter o código em repositórios públicos;
- separa aplicação e dados;
- facilita o uso de diferentes bases de conhecimento.

### Negativas

- o ambiente precisa fornecer a base externa;
- a configuração de volumes precisa ser mantida corretamente.
