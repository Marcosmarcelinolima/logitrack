"""DTOs para cadastro e consulta de produtos."""
from pydantic import BaseModel, ConfigDict, Field

class ProdutoCriacao(BaseModel):
    """Dados obrigatórios para cadastrar produto."""
    nome: str = Field(min_length=2, max_length=120)
    sku: str = Field(min_length=2, max_length=40, pattern=r"^[A-Za-z0-9-]+$")
    unidade: str = Field(min_length=1, max_length=20)

class ProdutoSaida(BaseModel):
    """Representação pública de produto."""
    id: int
    nome: str
    sku: str
    unidade: str
    model_config = ConfigDict(from_attributes=True)
