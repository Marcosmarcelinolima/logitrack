"""Ponto de entrada da API FastAPI LogiTrack."""
from fastapi import FastAPI
from app.controllers import entrega, estoque, produto
from app.core.exception_handlers import register_exception_handlers

app = FastAPI(title="LogiTrack API", version="1.0.0", description="API de controle de estoque e rastreamento de entregas.")
register_exception_handlers(app)
app.include_router(produto.router)
app.include_router(estoque.router)
app.include_router(entrega.router)

@app.get("/health", tags=["Infraestrutura"])
def health():
    """Confirma que o processo da API está respondendo."""
    return {"status": "ok"}
