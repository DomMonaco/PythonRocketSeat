from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.eventos import Eventos


class EventosRepository:
    def inserirEvento(self, informacoesEventos: Dict) -> Dict:
        with db_connection_handler as bancoDeDados:
            evento = Eventos(
                id=informacoesEventos.get["uuid"],
                titulo=informacoesEventos.get["titulo"],
                detalhes=informacoesEventos.get["detalhes"],
                slug=informacoesEventos.get["slug"],
                maximoParticipantes=informacoesEventos.get["maximoParticipantes"],
            ) 
            bancoDeDados.session.add(evento)
            bancoDeDados.session.commit()

            return informacoesEventos
        
    def obterEventoPorId(self, envetoId: str) -> Eventos:
        with db_connection_handler as bancoDeDados:
            evento = (
                bancoDeDados.session
                    .query(Eventos)
                    .filter(Eventos.id==envetoId)
                    .one()
            )

            return evento