# Contrato da API

Base local: `http://localhost:8000`. Corpos e respostas usam JSON. Swagger UI: `/docs`. Campos omitidos ou inválidos retornam HTTP 400; erros de regras retornam 400; ID ausente retorna 404.

## Produtos

### `POST /api/produtos` — 201

Entrada: `{"nome":"Café especial","sku":"CAF-001","unidade":"pacote"}`

Saída: `{"id":1,"nome":"Café especial","sku":"CAF-001","unidade":"pacote"}`

SKU já cadastrado: 400 `{"detail":"Já existe um produto cadastrado com este SKU."}`.

### `GET /api/produtos` — 200

Saída: `[{"id":1,"nome":"Café especial","sku":"CAF-001","unidade":"pacote"}]`.

### `GET /api/produtos/{id}` — 200 / 404

Saída id 1 igual ao objeto acima. Exemplo não encontrado: `{"detail":"Produto 999 não encontrado."}`.

## Estoques

### `POST /api/estoques` — 201

Entrada: `{"produto_id":1,"local":"CD Criciúma","quantidade":50}`

Saída: `{"id":1,"produto_id":1,"local":"CD Criciúma","quantidade":50,"reservada":0,"disponivel":50}`.

Produto inexistente: 404. Posição duplicada para produto/local: 400.

### `GET /api/estoques` — 200

Saída é uma lista de objetos no mesmo formato de criação.

### `GET /api/estoques/{id}` — 200 / 404

Saída é o objeto da posição; id inexistente retorna `{"detail":"Estoque 999 não encontrado."}`.

### `PATCH /api/estoques/{id}` — 200 / 400 / 404

Entrada: `{"quantidade":60}`. Saída: objeto de estoque atualizado. Se o novo saldo ficar abaixo das reservas, retorna HTTP 400 com mensagem explicativa.

## Entregas

### `POST /api/entregas` — 201 / 400 / 404

Entrada: `{"codigo_rastreamento":"LOG-2026-0001","destinatario":"Mercado Central","estoque_id":1,"quantidade":5,"endereco_entrega":"Rua Central, 100"}`.

Saída: `{"id":1,"codigo_rastreamento":"LOG-2026-0001","destinatario":"Mercado Central","estoque_id":1,"quantidade":5,"endereco_entrega":"Rua Central, 100","status":"CRIADA","criada_em":"2026-10-08T12:00:00Z"}`.

Reserva as unidades dentro da mesma transação. Saldo insuficiente retorna 400, por exemplo `{"detail":"Estoque insuficiente: disponíveis 2, solicitadas 5."}`. Estoque inexistente retorna 404; código de rastreamento duplicado retorna 400.

### `GET /api/entregas` — 200 e `GET /api/entregas/{id}` — 200 / 404

Retornam lista ou objeto no formato da resposta de criação. ID inexistente retorna `{"detail":"Entrega 999 não encontrada."}`.

### `POST /api/entregas/{id}/despachar` — 200 / 400 / 404

Entrada opcional: `{"observacao":"Saiu do centro de distribuição"}`. Resposta: objeto atualizado com `status: "EM_TRANSITO"`. Só pode ser chamado para entrega `CRIADA`.

### `POST /api/entregas/{id}/confirmar-entrega` — 200 / 400 / 404

Entrada opcional: `{"observacao":"Recebido no destino"}`. Resposta: objeto atualizado com `status: "ENTREGUE"`. Só aceita entrega `EM_TRANSITO`; ao confirmar, libera a reserva e baixa a quantidade física.

## Formato de erro

Erros de regra e ausência de recurso: `{"detail":"mensagem explicativa"}`. Campo inválido: `{"detail":"Dados inválidos.","erros":[{"campo":"body -> quantidade","mensagem":"Input should be greater than 0"}]}` com HTTP 400.

## Health

`GET /health` responde `200 {"status":"ok"}`.
