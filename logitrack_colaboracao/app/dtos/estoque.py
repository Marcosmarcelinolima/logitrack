"""DTOs para criar, ajustar e consultar posições de estoque."""
from pydantic import BaseModel, ConfigDict, Field

class EstoqueCriacao(BaseModel):
    """Dados para abrir uma posição de estoque."""
    produto_id: int = Field(gt=0)
    local: str = Field(min_length=2, max_length=120)
    quantidade: int = Field(ge=0)

class EstoqueAtualizacao(BaseModel):
    """Novo saldo físico desejado para a posição."""
    quantidade: int = Field(ge=0)

class EstoqueSaida(BaseModel):
    """Saldo físico, reservado e disponível de uma posição."""
    id: int
    produto_id: int
    local: str
    quantidade: int
    reservada: int
    disponivel: int
    model_config = ConfigDict(from_attributes=True)
