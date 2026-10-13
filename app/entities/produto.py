"""Entidade de catálogo para um produto que pode ser armazenado e enviado."""
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Produto(Base):
    """Produto identificável por SKU e associado a posições de estoque."""
    __tablename__ = "produtos"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    sku: Mapped[str] = mapped_column(String(40), unique=True, nullable=False, index=True)
    unidade: Mapped[str] = mapped_column(String(20), nullable=False)
    estoques: Mapped[list["Estoque"]] = relationship(back_populates="produto")
