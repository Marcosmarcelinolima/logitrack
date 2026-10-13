"""Consultas e persistência das posições de estoque."""
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.entities.estoque import Estoque

class EstoqueRepository:
    """Executa operações de leitura e escrita de estoque."""
    def __init__(self, db: Session): self.db = db
    def listar(self) -> list[Estoque]: return list(self.db.scalars(select(Estoque).order_by(Estoque.id)))
    def por_id(self, id: int, bloquear: bool = False) -> Estoque | None:
        stmt = select(Estoque).where(Estoque.id == id)
        if bloquear: stmt = stmt.with_for_update()
        return self.db.scalar(stmt)
    def por_produto_local(self, produto_id: int, local: str) -> Estoque | None: return self.db.scalar(select(Estoque).where(Estoque.produto_id == produto_id, Estoque.local == local))
    def salvar(self, entidade: Estoque) -> Estoque:
        self.db.add(entidade); self.db.flush(); self.db.refresh(entidade); return entidade
