"""Converte erros da aplicação em mensagens JSON consistentes."""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.core.errors import RecursoNaoEncontrado, RegraDeNegocioViolada

def register_exception_handlers(app: FastAPI) -> None:
    """Registra respostas 400 para entrada/regra inválida e 404 para ausência."""
    @app.exception_handler(RequestValidationError)
    async def validacao_handler(request: Request, exc: RequestValidationError):
        erros = [{"campo": " -> ".join(str(parte) for parte in erro["loc"]), "mensagem": erro["msg"]} for erro in exc.errors()]
        return JSONResponse(status_code=400, content={"detail": "Dados inválidos.", "erros": erros})
    @app.exception_handler(RegraDeNegocioViolada)
    async def regra_handler(request: Request, exc: RegraDeNegocioViolada):
        return JSONResponse(status_code=400, content={"detail": str(exc)})
    @app.exception_handler(RecursoNaoEncontrado)
    async def nao_encontrado_handler(request: Request, exc: RecursoNaoEncontrado):
        return JSONResponse(status_code=404, content={"detail": str(exc)})
