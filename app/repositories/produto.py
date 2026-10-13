"""Consultas e persistência da entidade Produto."""
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.entities.produto import Produto

class ProdutoRepository:
    """Executa operações de leitura e escrita de produtos."""
    def __init__(self, db: Session): self.db = db
    def listar(self) -> list[Produto]: return list(self.db.scalars(select(Produto).order_by(Produto.id)))
    def por_id(self, id: int) -> Produto | None: return self.db.get(Produto, id)
    def por_sku(self, sku: str) -> Produto | None: return self.db.scalar(select(Produto).where(Produto.sku == sku))
    def salvar(self, entidade: Produto) -> Produto:
        self.db.add(entidade); self.db.flush(); self.db.refresh(entidade); return entidade
