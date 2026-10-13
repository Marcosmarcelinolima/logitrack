"""Regras para cadastro, consulta e ajuste protegido de estoque."""
from sqlalchemy.orm import Session
from app.core.errors import RecursoNaoEncontrado, RegraDeNegocioViolada
from app.dtos.estoque import EstoqueAtualizacao, EstoqueCriacao
from app.entities.estoque import Estoque
from app.repositories.estoque import EstoqueRepository
from app.repositories.produto import ProdutoRepository

class EstoqueService:
    """Coordena estoque e impede alterações que invalidem reservas."""
    def __init__(self, db: Session): self.db = db; self.repo = EstoqueRepository(db)
    def criar(self, dados: EstoqueCriacao) -> Estoque:
        if not ProdutoRepository(self.db).por_id(dados.produto_id): raise RecursoNaoEncontrado(f"Produto {dados.produto_id} não encontrado.")
        if self.repo.por_produto_local(dados.produto_id, dados.local): raise RegraDeNegocioViolada("Já existe uma posição deste produto neste local.")
        try:
            item = self.repo.salvar(Estoque(**dados.model_dump())); self.db.commit(); return item
        except Exception:
            self.db.rollback(); raise
    def listar(self) -> list[Estoque]: return self.repo.listar()
    def buscar(self, id: int) -> Estoque:
        item = self.repo.por_id(id)
        if not item: raise RecursoNaoEncontrado(f"Estoque {id} não encontrado.")
        return item
    def atualizar(self, id: int, dados: EstoqueAtualizacao) -> Estoque:
        item = self.repo.por_id(id, bloquear=True)
        if not item: raise RecursoNaoEncontrado(f"Estoque {id} não encontrado.")
        if dados.quantidade < item.reservada: raise RegraDeNegocioViolada(f"Saldo não pode ficar abaixo das {item.reservada} unidades reservadas.")
        try:
            item.quantidade = dados.quantidade; self.db.commit(); self.db.refresh(item); return item
        except Exception:
            self.db.rollback(); raise
