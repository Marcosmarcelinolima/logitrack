"""Rotas HTTP para cadastro e consulta de produtos."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.dtos.produto import ProdutoCriacao, ProdutoSaida
from app.mappers.produto import ProdutoMapper
from app.services.produto import ProdutoService

router = APIRouter(prefix="/api/produtos", tags=["Produtos"])

@router.post("", response_model=ProdutoSaida, status_code=status.HTTP_201_CREATED)
def criar(dados: ProdutoCriacao, db: Session = Depends(get_db)):
    return ProdutoMapper.para_saida(ProdutoService(db).criar(dados))

@router.get("", response_model=list[ProdutoSaida])
def listar(db: Session = Depends(get_db)):
    return [ProdutoMapper.para_saida(item) for item in ProdutoService(db).listar()]

@router.get("/{id}", response_model=ProdutoSaida)
def buscar(id: int, db: Session = Depends(get_db)):
    return ProdutoMapper.para_saida(ProdutoService(db).buscar(id))
