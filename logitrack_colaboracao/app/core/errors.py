"""Exceções de aplicação mapeadas para respostas HTTP."""
class RecursoNaoEncontrado(Exception):
    """Indica que o recurso solicitado não existe."""

class RegraDeNegocioViolada(Exception):
    """Indica que a operação viola uma regra do domínio."""
