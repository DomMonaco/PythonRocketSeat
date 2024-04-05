from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.eventos import Eventos
from src.models.entities.participantes import Participantes
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError


class EventosRepository:
    def inserirEvento(self, informacoesEventos: Dict) -> Dict:
        with db_connection_handler as bancoDeDados:
            try:
                event = Eventos(
                    id=informacoesEventos.get("uuid"),
                    title=informacoesEventos.get("titulo"),
                    details=informacoesEventos.get("detalhes"),
                    slug=informacoesEventos.get("slug"),
                    maximum_attendees=informacoesEventos.get("maximoParticipantes"),
                )
                bancoDeDados.session.add(event)
                bancoDeDados.session.commit()

                return informacoesEventos
            except IntegrityError:
                raise HttpConflictError('Evento ja cadastrado!')
            except Exception as exception:
                bancoDeDados.session.rollback()
                raise exception

    def obterEventoPorId(self, eventoId: str) -> Eventos:
        with db_connection_handler as bancoDeDados:
            try:
                evento = (
                    bancoDeDados.session
                        .query(Eventos)
                        .filter(Eventos.id==eventoId)
                        .one()
                )
                return evento
            except NoResultFound:
                return None

    def quantidadeParticipantesEvento(self, eventoId: str) -> Dict:
        with db_connection_handler as bancoDeDados:
            quantidadeEvento = (
                bancoDeDados.session
                    .query(Eventos)
                    .join(Participantes, Eventos.id == Participantes.eventoId)
                    .filter(Eventos.id==eventoId)
                    .with_entities(
                        Eventos.maximoParticipantes,
                        Participantes.id
                    )
                    .all()
            )
            if not len(quantidadeEvento):
                return {
                    "maximoParticipantes": 0,
                    "quantidadeParticipantes": 0,
                }

            return {
                "maximoParticipantes": quantidadeEvento[0].maximoParticipantes,
                "quantidadeParticipantes": len(quantidadeEvento),
            }
