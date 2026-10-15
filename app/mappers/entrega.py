from app.dtos.entrega import EntregaCriacao, EntregaSaida
from app.entities.entrega import Entrega

class EntregaMapper:
    """Converte entre os DTOs e a entidade de entrega. Situação: implementada."""
    @staticmethod
    def para_entidade(dados: EntregaCriacao) -> Entrega:
        return Entrega(**dados.model_dump())

    @staticmethod
    def para_saida(entidade: Entrega) -> EntregaSaida:
        return EntregaSaida.model_validate(entidade)
