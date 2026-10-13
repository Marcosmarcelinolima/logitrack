"""Mapeia entidades Entrega para o DTO público."""
from app.dtos.entrega import EntregaSaida
from app.entities.entrega import Entrega

class EntregaMapper:
    """Centraliza a conversão da entidade Entrega para a API."""
    @staticmethod
    def para_saida(entidade: Entrega) -> EntregaSaida:
        return EntregaSaida.model_validate(entidade)
