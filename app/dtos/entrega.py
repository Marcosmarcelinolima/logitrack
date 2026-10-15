from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator

class EntregaCriacao(BaseModel):
    """Valida os dados para criar uma entrega. Situação: implementada."""
    codigo_rastreamento: str = Field(min_length=4, max_length=50, pattern=r"^[A-Za-z0-9-]+$")
    destinatario: str = Field(min_length=2, max_length=120)
    estoque_id: int = Field(gt=0)
    quantidade: int = Field(gt=0)
    endereco_entrega: str = Field(min_length=5, max_length=240)

    @field_validator("destinatario", "endereco_entrega", mode="before")
    @classmethod
    def remover_espacos_externos(cls, valor: object) -> object:
        # Remove espaços externos antes de validar o tamanho; mantém os internos.
        if isinstance(valor, str):
            return valor.strip()
        return valor

class TransicaoEntrega(BaseModel):
    """Aceita uma observação opcional, sem efeito no status. Situação: implementada."""
    observacao: str | None = Field(default=None, max_length=240)

class EntregaSaida(BaseModel):
    """Define os dados das respostas de entrega. Situação: implementada."""
    id: int
    codigo_rastreamento: str
    destinatario: str
    estoque_id: int
    quantidade: int
    endereco_entrega: str
    status: str
    criada_em: datetime
    model_config = ConfigDict(from_attributes=True)
