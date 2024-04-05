from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql import func

class Participantes(Base):
    __tablename__ = "participantes"

    id = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    eventoId = Column(String, ForeignKey("eventos.id"))
    dataCriacao = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"Participantes [nome={self.nome}, email={self.email}, eventoId={self.eventoId}]"
