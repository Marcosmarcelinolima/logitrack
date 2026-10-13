"""Consultas e persistência das entregas."""
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.entities.entrega import Entrega

class EntregaRepository:
    """Executa operações de leitura e escrita de entregas."""
    def __init__(self, db: Session): self.db = db
    def listar(self) -> list[Entrega]: return list(self.db.scalars(select(Entrega).order_by(Entrega.id)))
    def por_id(self, id: int) -> Entrega | None: return self.db.get(Entrega, id)
    def por_id_bloqueando(self, id: int) -> Entrega | None: return self.db.scalar(select(Entrega).where(Entrega.id == id).with_for_update())
    def por_codigo(self, codigo: str) -> Entrega | None: return self.db.scalar(select(Entrega).where(Entrega.codigo_rastreamento == codigo))
    def salvar(self, entidade: Entrega) -> Entrega:
        self.db.add(entidade); self.db.flush(); self.db.refresh(entidade); return entidade
