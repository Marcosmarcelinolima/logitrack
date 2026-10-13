"""DTOs de criação, transição e consulta de entrega."""
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class EntregaCriacao(BaseModel):
    """Dados de entrega que será criada e terá estoque reservado."""
    codigo_rastreamento: str = Field(min_length=4, max_length=50, pattern=r"^[A-Za-z0-9-]+$")
    destinatario: str = Field(min_length=2, max_length=120)
    estoque_id: int = Field(gt=0)
    quantidade: int = Field(gt=0)
    endereco_entrega: str = Field(min_length=5, max_length=240)

class TransicaoEntrega(BaseModel):
    """Corpo vazio para documentar a ação explícita de transição."""
    observacao: str | None = Field(default=None, max_length=240)

class EntregaSaida(BaseModel):
    """Dados públicos da entrega e estado de rastreamento."""
    id: int
    codigo_rastreamento: str
    destinatario: str
    estoque_id: int
    quantidade: int
    endereco_entrega: str
    status: str
    criada_em: datetime
    model_config = ConfigDict(from_attributes=True)
