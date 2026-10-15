from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Entrega(Base):
    """Representa uma entrega no banco de dados. Situação: implementada."""
    __tablename__ = "entregas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    codigo_rastreamento: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, index=True)
    destinatario: Mapped[str] = mapped_column(String(120), nullable=False)
    estoque_id: Mapped[int] = mapped_column(ForeignKey("estoques.id", ondelete="RESTRICT"), nullable=False, index=True)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    endereco_entrega: Mapped[str] = mapped_column(String(240), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="CRIADA")
    criada_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    estoque: Mapped["Estoque"] = relationship(back_populates="entregas")
