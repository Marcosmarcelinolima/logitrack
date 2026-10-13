"""Mapeia entidades Produto para o DTO de saída."""
from app.dtos.produto import ProdutoSaida
from app.entities.produto import Produto

class ProdutoMapper:
    """Centraliza a conversão da entidade Produto para a API."""
    @staticmethod
    def para_saida(entidade: Produto) -> ProdutoSaida:
        return ProdutoSaida.model_validate(entidade)
