from sqlalchemy import select
from sqlalchemy.orm import Session
from app.entities.entrega import Entrega

class EntregaRepository:
    """Consulta e salva entregas no banco de dados. Situação: implementada."""
    def __init__(self, db: Session):
        self.db = db

    def listar(self) -> list[Entrega]:
        consulta = select(Entrega).order_by(Entrega.id)
        return list(self.db.scalars(consulta))

    def por_id(self, id: int) -> Entrega | None:
        return self.db.get(Entrega, id)

    def por_id_bloqueando(self, id: int) -> Entrega | None:
        # O bloqueio dura até o fim da transação.
        consulta = select(Entrega).where(Entrega.id == id).with_for_update()
        return self.db.scalar(consulta)

    def por_codigo(self, codigo: str) -> Entrega | None:
        consulta = select(Entrega).where(Entrega.codigo_rastreamento == codigo)
        return self.db.scalar(consulta)

    def salvar(self, entidade: Entrega) -> Entrega:
        self.db.add(entidade)
        self.db.flush()
        self.db.refresh(entidade)
        return entidade
