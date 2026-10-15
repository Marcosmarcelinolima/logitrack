# LogiTrack — Gestão de estoque e rastreamento de entregas

API REST para pequenas transportadoras que precisam acompanhar os produtos disponíveis, separar mercadorias para pedidos e registrar o ciclo de entrega. O sistema é usado por operadores de estoque e despachantes. Foi implementado em Python com FastAPI, SQLAlchemy e PostgreSQL, como equivalente às camadas do template Spring Boot da disciplina.

## Problema e regras de negócio

Operadores controlam o saldo físico e reservado de cada produto. Despachantes criam entregas, reservam estoque e avançam a entrega por estados, evitando promessas de envio que não podem ser cumpridas.

1. **Reserva atômica:** ao criar uma entrega, o sistema reserva a quantidade solicitada. Estoque disponível é `quantidade - reservada`; se for insuficiente, a operação retorna HTTP 400 sem criar a entrega.
2. **Reserva protegida:** uma atualização do saldo físico não pode reduzi-lo abaixo da quantidade já reservada.
3. **Fluxo rastreável:** uma entrega só pode ir de `CRIADA` para `EM_TRANSITO` e então para `ENTREGUE`. Não se pode entregar antes do despacho nem repetir uma transição.
4. **Baixa na confirmação:** ao marcar como entregue, a reserva é liberada e o saldo físico é baixado uma única vez.

## Estrutura e mapa de classes

`app/main.py` cria a aplicação e registra os controladores; `app/core/` contém configuração, conexão com banco, erros e tratamento HTTP.

Cada entidade segue `entities/` (modelo ORM), `dtos/` (entrada/saída), `mappers/`, `repositories/`, `services/` (regras) e `controllers/` (rotas):

| Entidade | Classes por camada |
|---|---|
| Produto | `Produto`, `ProdutoCriacao`, `ProdutoSaida`, `ProdutoMapper`, `ProdutoRepository`, `ProdutoService`, `produto_router` |
| Estoque | `Estoque`, `EstoqueCriacao`, `EstoqueAtualizacao`, `EstoqueSaida`, `EstoqueMapper`, `EstoqueRepository`, `EstoqueService`, `estoque_router` |
| Entrega | `Entrega`, `EntregaCriacao`, `EntregaSaida`, `TransicaoEntrega`, `EntregaMapper`, `EntregaRepository`, `EntregaService`, `entrega_router` |

As migrações ficam em `alembic/versions/`. `app/core/errors.py` define as exceções de aplicação e `app/core/exception_handlers.py` padroniza respostas de erro.

## Rotas

| Método e rota | Ação |
|---|---|
| `POST /api/produtos`, `GET /api/produtos`, `GET /api/produtos/{id}` | Cadastrar e consultar produtos |
| `POST /api/estoques`, `GET /api/estoques`, `GET /api/estoques/{id}`, `PATCH /api/estoques/{id}` | Cadastrar, consultar e ajustar saldo |
| `POST /api/entregas`, `GET /api/entregas`, `GET /api/entregas/{id}` | Criar (reservando estoque) e consultar entregas |
| `POST /api/entregas/{id}/despachar`, `POST /api/entregas/{id}/confirmar-entrega` | Avançar o rastreamento e baixar estoque |

Campos inválidos e violações de regra retornam HTTP 400; identificadores inexistentes retornam 404. O Swagger UI fica em `/docs` e OpenAPI em `/openapi.json`.

## Como executar

Requisitos: Docker Desktop com Compose. Na raiz:

```bash
docker compose up --build
```

A API estará em `http://localhost:8000`; documentação interativa em `http://localhost:8000/docs`. Para encerrar: `docker compose down`. Os dados ficam no volume `postgres_data`.

### Exemplo rápido

1. `POST /api/produtos` com `{"nome":"Café especial","sku":"CAF-001","unidade":"pacote"}`.
2. `POST /api/estoques` com `{"produto_id":1,"local":"CD Criciúma","quantidade":50}`.
3. `POST /api/entregas` com `{"codigo_rastreamento":"LOG-2026-0001","destinatario":"Mercado Central","estoque_id":1,"quantidade":5,"endereco_entrega":"Rua Central, 100"}`.
4. `POST /api/entregas/1/despachar` e depois `POST /api/entregas/1/confirmar-entrega`.

As respostas completas e os erros estão em [docs/contrato-da-api.md](docs/contrato-da-api.md); entidades e relacionamento em [docs/modelo-de-dominio.md](docs/modelo-de-dominio.md). Autoavaliação: [docs/autoavaliacao.md](docs/autoavaliacao.md).

## O que funciona

Cadastro e consulta das três entidades, validação dos dados de entrada, busca por ID, reserva transacional de estoque, ajuste protegido de saldo, transições rastreáveis e baixa de estoque na entrega. Não foram incluídos PUT ou DELETE, pois nenhuma regra exige essas operações.

## Equivalência arquitetural com Java/Spring

| Critério da disciplina | Implementação Python |
|---|---|
| `@Entity` | Modelos SQLAlchemy em `app/entities/` |
| Repositório | Classes em `app/repositories/` |
| DTOs e Mapper | Modelos Pydantic em `app/dtos/` e conversores em `app/mappers/` |
| Service | Regras de negócio em `app/services/` |
| Controller | `APIRouter` em `app/controllers/` |
| Migration | Alembic em `alembic/versions/` |
| Erros REST | Handlers FastAPI com JSON `{"detail":"..."}` |
| Swagger | OpenAPI automático em `/docs` |

## Integrantes

Marcos Marcelino, Simei Mondardo e Henrique
