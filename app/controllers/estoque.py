"""Rotas HTTP para criação, consulta e ajuste de estoques."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.dtos.estoque import EstoqueAtualizacao, EstoqueCriacao, EstoqueSaida
from app.mappers.estoque import EstoqueMapper
from app.services.estoque import EstoqueService

router = APIRouter(prefix="/api/estoques", tags=["Estoques"])

@router.post("", response_model=EstoqueSaida, status_code=status.HTTP_201_CREATED)
def criar(dados: EstoqueCriacao, db: Session = Depends(get_db)):
    return EstoqueMapper.para_saida(EstoqueService(db).criar(dados))

@router.get("", response_model=list[EstoqueSaida])
def listar(db: Session = Depends(get_db)):
    return [EstoqueMapper.para_saida(item) for item in EstoqueService(db).listar()]

@router.get("/{id}", response_model=EstoqueSaida)
def buscar(id: int, db: Session = Depends(get_db)):
    return EstoqueMapper.para_saida(EstoqueService(db).buscar(id))

@router.patch("/{id}", response_model=EstoqueSaida)
def atualizar(id: int, dados: EstoqueAtualizacao, db: Session = Depends(get_db)):
    return EstoqueMapper.para_saida(EstoqueService(db).atualizar(id, dados))
