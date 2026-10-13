# Autoavaliação

| Item pedido | Implementação | Situação |
|---|---|---|
| Problema, usuários e pelo menos três regras | README, regras de reserva, saldo protegido e fluxo/baixa de entrega | Feito |
| Mapa das classes por entidade e camada | README e pastas em `app/` | Feito |
| Modelo com pelo menos três entidades, relacionamento e diagrama | `docs/modelo-de-dominio.md` | Feito |
| Contrato com rotas, entradas e saídas | `docs/contrato-da-api.md` | Feito |
| Migração, entidade, repositório, DTO, mapper, service e controller | Estrutura Python equivalente documentada no README | Feito |
| API simples POST, GET, GET por ID | Rotas de produtos, estoques e entregas | Feito |
| 400 para campo inválido | Handler de `RequestValidationError` padroniza entrada inválida para 400 | Feito |
| 404 para ID ausente | Handlers de `RecursoNaoEncontrado` | Feito |
| Regras executadas no Service | Reserva, ajuste, estados e baixa | Feito |
| PostgreSQL, migração e Swagger | Docker Compose, Alembic, OpenAPI `/docs` | Feito |
| Execução de ponta a ponta | Docker não está disponível neste ambiente para iniciar a API | Pendente de validação |
| GitHub público, colaboradores, e-mail e apresentação | Dependem do grupo e da conta/repositorio do grupo | Pendente pelo grupo |

## Limitações conhecidas

Este código foi organizado como aplicação Python independente porque a pasta recebida não continha o template Java nem um repositório Git local. Antes de entregar, preencher integrantes, validar a execução em Docker e conferir que a instituição aceita Python como linguagem alternativa.
