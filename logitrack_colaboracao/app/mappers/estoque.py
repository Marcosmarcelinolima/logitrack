"""Mapeia entidades Estoque para DTOs com quantidade disponível."""
from app.dtos.estoque import EstoqueSaida
from app.entities.estoque import Estoque

class EstoqueMapper:
    """Converte saldo físico e reserva na representação de estoque."""
    @staticmethod
    def para_saida(entidade: Estoque) -> EstoqueSaida:
        return EstoqueSaida(id=entidade.id, produto_id=entidade.produto_id, local=entidade.local, quantidade=entidade.quantidade, reservada=entidade.reservada, disponivel=entidade.quantidade - entidade.reservada)
