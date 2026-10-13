"""Dependências de infraestrutura injetadas pelos controladores."""
from collections.abc import Generator
from sqlalchemy.orm import Session
from app.core.database import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """Abre uma sessão por requisição e sempre a encerra."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
