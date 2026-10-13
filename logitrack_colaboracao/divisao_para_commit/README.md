# Divisão do trabalho para três pessoas

Esta cópia está em `logitrack_colaboracao/`, separada da pasta original do projeto, e aponta para `https://github.com/Marcosmarcelinolima/logitrack.git`. O código original foi copiado para cá; o projeto na pasta acima não foi alterado.

## Antes de começar

O repositório GitHub estava vazio quando foi clonado. A cópia local já está ligada a ele, mas ainda não há commit base. Primeiro, alguém do grupo precisa combinar e publicar a versão inicial do projeto; depois, os outros integrantes podem criar branches próprias a partir dessa base e enviar seus commits. Não consigo atribuir commits às três pessoas sem os nomes/autores e sem inventar alterações: os módulos listados abaixo já existem no projeto copiado.

Não inicialize outro Git dentro de uma pasta de entrega individual. Os commits precisam acontecer na raiz de `logitrack_colaboracao/`, para que a integração seja simples.

## Responsabilidades

Cada pessoa fica responsável por uma entidade e por suas camadas. Assim, cada uma trabalha em arquivos diferentes.

### Pessoa 1 — Produtos

Arquivos de responsabilidade:

- `app/controllers/produto.py`
- `app/dtos/produto.py`
- `app/entities/produto.py`
- `app/mappers/produto.py`
- `app/repositories/produto.py`
- `app/services/produto.py`

Commit sugerido: `feat: implementar gerenciamento de produtos`

### Pessoa 2 — Estoque

Arquivos de responsabilidade:

- `app/controllers/estoque.py`
- `app/dtos/estoque.py`
- `app/entities/estoque.py`
- `app/mappers/estoque.py`
- `app/repositories/estoque.py`
- `app/services/estoque.py`

Commit sugerido: `feat: implementar gerenciamento de estoque`

### Pessoa 3 — Entregas

Arquivos de responsabilidade:

- `app/controllers/entrega.py`
- `app/dtos/entrega.py`
- `app/entities/entrega.py`
- `app/mappers/entrega.py`
- `app/repositories/entrega.py`
- `app/services/entrega.py`

Commit sugerido: `feat: implementar rastreamento de entregas`

## Arquivos compartilhados

Para evitar conflitos, combinem antes de alterar estes arquivos compartilhados: `app/main.py`, `app/core/`, `app/*/__init__.py`, `alembic/`, `docs/`, `README.md`, `requirements.txt` e arquivos Docker. Uma pessoa pode assumir essas integrações depois que os três commits por entidade estiverem prontos.

As pastas `app/*/__init__.py` podem precisar de imports para registrar as novas classes; façam essas alterações em conjunto ou deixem para quem integrar. O mesmo vale para a migração Alembic: uma única pessoa deve consolidar qualquer mudança de esquema.

## Fluxo de cada integrante

1. Criar uma branch própria a partir da versão inicial combinada.
2. Alterar somente os arquivos da sua responsabilidade; combinar previamente qualquer arquivo compartilhado.
3. Revisar as mudanças e fazer o commit com a mensagem sugerida.
4. Enviar a branch e solicitar a integração ao responsável pelo repositório.

Depois que a versão inicial estiver publicada, exemplo para a Pessoa 1, a partir da raiz de `logitrack_colaboracao/`:

```bash
git switch -c feature/produtos
git add app/controllers/produto.py app/dtos/produto.py app/entities/produto.py app/mappers/produto.py app/repositories/produto.py app/services/produto.py
git commit -m "feat: implementar gerenciamento de produtos"
git push -u origin feature/produtos
```

As pessoas de Estoque e Entregas devem trocar o nome da branch, os caminhos e a mensagem pelos da sua parte. O `git add` explícito ajuda a não incluir alterações de outro integrante no commit.
