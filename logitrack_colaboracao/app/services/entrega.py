"""Regras de reserva, despacho e confirmação de entrega."""
from sqlalchemy.orm import Session
from app.core.errors import RecursoNaoEncontrado, RegraDeNegocioViolada
from app.dtos.entrega import EntregaCriacao
from app.entities.entrega import Entrega
from app.repositories.entrega import EntregaRepository
from app.repositories.estoque import EstoqueRepository

class EntregaService:
    """Garante reserva atômica e avanço válido do rastreamento."""
    def __init__(self, db: Session): self.db = db; self.repo = EntregaRepository(db); self.estoques = EstoqueRepository(db)
    def criar(self, dados: EntregaCriacao) -> Entrega:
        if self.repo.por_codigo(dados.codigo_rastreamento): raise RegraDeNegocioViolada("O código de rastreamento já está em uso.")
        estoque = self.estoques.por_id(dados.estoque_id, bloquear=True)
        if not estoque: raise RecursoNaoEncontrado(f"Estoque {dados.estoque_id} não encontrado.")
        disponivel = estoque.quantidade - estoque.reservada
        if dados.quantidade > disponivel: raise RegraDeNegocioViolada(f"Estoque insuficiente: disponíveis {disponivel}, solicitadas {dados.quantidade}.")
        try:
            estoque.reservada += dados.quantidade
            entrega = self.repo.salvar(Entrega(**dados.model_dump())); self.db.commit(); return entrega
        except Exception:
            self.db.rollback(); raise
    def listar(self) -> list[Entrega]: return self.repo.listar()
    def buscar(self, id: int) -> Entrega:
        item = self.repo.por_id(id)
        if not item: raise RecursoNaoEncontrado(f"Entrega {id} não encontrada.")
        return item
    def despachar(self, id: int) -> Entrega:
        entrega = self._bloquear_entrega(id)
        if entrega.status != "CRIADA": raise RegraDeNegocioViolada("Só é possível despachar uma entrega no estado CRIADA.")
        try:
            entrega.status = "EM_TRANSITO"; self.db.commit(); self.db.refresh(entrega); return entrega
        except Exception:
            self.db.rollback(); raise
    def confirmar_entrega(self, id: int) -> Entrega:
        entrega = self._bloquear_entrega(id)
        if entrega.status != "EM_TRANSITO": raise RegraDeNegocioViolada("A entrega precisa estar EM_TRANSITO antes da confirmação.")
        estoque = self.estoques.por_id(entrega.estoque_id, bloquear=True)
        try:
            estoque.quantidade -= entrega.quantidade
            estoque.reservada -= entrega.quantidade
            entrega.status = "ENTREGUE"
            self.db.commit(); self.db.refresh(entrega); return entrega
        except Exception:
            self.db.rollback(); raise
    def _bloquear_entrega(self, id: int) -> Entrega:
        entrega = self.repo.por_id_bloqueando(id)
        if not entrega: raise RecursoNaoEncontrado(f"Entrega {id} não encontrada.")
        return entrega
