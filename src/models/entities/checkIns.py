from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = "checkIns"

    id = Column(Integer, primary_key=True)
    dataCriacao = Column(DateTime, default=func.now())
    participanteId = Column(String, ForeignKey("participantes.id"))

    def __repr__(self):
        return f"CheckIns [participanteId={self.participanteId}]"
