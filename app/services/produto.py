"""Regras e casos de uso do catálogo de produtos."""
from sqlalchemy.orm import Session
from app.core.errors import RecursoNaoEncontrado, RegraDeNegocioViolada
from app.dtos.produto import ProdutoCriacao
from app.entities.produto import Produto
from app.repositories.produto import ProdutoRepository

class ProdutoService:
    """Coordena cadastro e consulta de produtos."""
    def __init__(self, db: Session): self.db = db; self.repo = ProdutoRepository(db)
    def criar(self, dados: ProdutoCriacao) -> Produto:
        if self.repo.por_sku(dados.sku): raise RegraDeNegocioViolada("Já existe um produto cadastrado com este SKU.")
        try:
            item = self.repo.salvar(Produto(**dados.model_dump())); self.db.commit(); return item
        except Exception:
            self.db.rollback(); raise
    def listar(self) -> list[Produto]: return self.repo.listar()
    def buscar(self, id: int) -> Produto:
        item = self.repo.por_id(id)
        if not item: raise RecursoNaoEncontrado(f"Produto {id} não encontrado.")
        return item
