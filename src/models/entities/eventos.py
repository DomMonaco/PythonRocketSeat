from src.models.settings.base import Base
from sqlalchemy import Column, String, Integer


class Eventos(Base):
    __tablename__ = "eventos"

    id = Column(String, primary_key=True)
    titulo = Column(String, nullable=False)
    detalhes = Column(String)
    slug = Column(String, nullable=False)
    maximoParticipantes = Column(String, primary_key=True)