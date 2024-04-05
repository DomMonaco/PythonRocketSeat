from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.participantes import Participantes
from src.models.entities.checkIns import CheckIns
from src.models.entities.eventos import Eventos
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError

class ParticipantesRepository:
    def inserirPaticipantes(self, informacaoPaticipante: Dict) -> Dict:
        with db_connection_handler as bancoDeDados:
            try:
                participante = (
                    Participantes(
                        id=informacaoPaticipante.get("uuid"),
                        nome=informacaoPaticipante.get("nome"),
                        email=informacaoPaticipante.get("email"),
                        eventoId=informacaoPaticipante.get("eventoId")
                    )
                )
                bancoDeDados.session.add(participante)
                bancoDeDados.session.commit()

                return informacaoPaticipante
            except IntegrityError:
                raise HttpConflictError('Participante ja cadastrado!')
            except Exception as exception:
                bancoDeDados.session.rollback()
                raise exception

    def obterParticipanteCrachaPorId(self, participanteId: str):
        with db_connection_handler as bancoDeDados:
            try:
                attendee = (
                    bancoDeDados.session
                        .query(Participantes)
                        .join(Eventos, Eventos.id == Participantes.eventoId)
                        .filter(Participantes.id==participanteId)
                        .with_entities(
                            Participantes.nome,
                            Participantes.email,
                            Eventos.titulo
                        )
                        .one()
                )
                return attendee
            except NoResultFound:
                return None

    def obterParticipantePorEventoId(self, eventoId: str) -> List[Participantes]:
        with db_connection_handler as bancoDeDados:
            participantes = (
                bancoDeDados.session
                    .query(Participantes)
                    .outerjoin(CheckIns, CheckIns.participanteId==Participantes.id)
                    .filter(Participantes.eventoId==eventoId)
                    .with_entities(
                        Participantes.id,
                        Participantes.nome,
                        Participantes.email,
                        CheckIns.dataCriacao.label('checkedInDataCriacao'),
                        Participantes.dataCriacao.label('dataCriacao')
                    )
                    .all()
            )
            return participantes