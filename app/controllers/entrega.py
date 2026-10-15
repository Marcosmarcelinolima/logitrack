"""Recebe as requisições HTTP de entregas. Situação: implementado."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.dtos.entrega import EntregaCriacao, EntregaSaida, TransicaoEntrega
from app.services.entrega import EntregaService

router = APIRouter(prefix="/api/entregas", tags=["Entregas"])

@router.post("", response_model=EntregaSaida, status_code=status.HTTP_201_CREATED)
def criar(dados: EntregaCriacao, db: Session = Depends(get_db)) -> EntregaSaida:
    return EntregaService(db).criar(dados)

@router.get("", response_model=list[EntregaSaida])
def listar(db: Session = Depends(get_db)) -> list[EntregaSaida]:
    return EntregaService(db).listar()

@router.get("/{id}", response_model=EntregaSaida)
def buscar(id: int, db: Session = Depends(get_db)) -> EntregaSaida:
    return EntregaService(db).buscar(id)

@router.post("/{id}/despachar", response_model=EntregaSaida)
def despachar(id: int, dados: TransicaoEntrega | None = None, db: Session = Depends(get_db)) -> EntregaSaida:
    return EntregaService(db).despachar(id)

@router.post("/{id}/confirmar-entrega", response_model=EntregaSaida)
def confirmar_entrega(id: int, dados: TransicaoEntrega | None = None, db: Session = Depends(get_db)) -> EntregaSaida:
    return EntregaService(db).confirmar_entrega(id)
