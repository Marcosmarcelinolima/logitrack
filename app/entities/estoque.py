"""Entidade que registra saldo físico e reservado de um produto em um local."""
from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Estoque(Base):
    """Posição de estoque; disponível corresponde ao saldo menos reservas."""
    __tablename__ = "estoques"
    __table_args__ = (CheckConstraint("quantidade >= 0", name="ck_estoque_quantidade_nao_negativa"), CheckConstraint("reservada >= 0 AND reservada <= quantidade", name="ck_estoque_reservada_valida"), UniqueConstraint("produto_id", "local", name="uq_estoque_produto_local"))
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id", ondelete="RESTRICT"), nullable=False, index=True)
    local: Mapped[str] = mapped_column(String(120), nullable=False)
    quantidade: Mapped[int] = mapped_column(Integer, nullable=False)
    reservada: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    produto: Mapped["Produto"] = relationship(back_populates="estoques")
    entregas: Mapped[list["Entrega"]] = relationship(back_populates="estoque")
