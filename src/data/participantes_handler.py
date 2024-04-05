import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.eventosRepository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_conflict import HttpConflictError


class ParticipantesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def regitrar(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]

        event_attendees_count = self.__events_repository.count_event_attendees(event_id)
        if (
            event_attendees_count["participantesQuantidade"]
            and event_attendees_count["maximoParticipantes"] < event_attendees_count["participantesQuantidade"]
        ): raise HttpConflictError("Evento Lotado")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id
        self.__attendees_repository.insert_attendee(body)

        return HttpResponse(body=None, status_code=201)

    def obterParticipanteCracha(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["participanteId"]
        cracha = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
        if not cracha: raise HttpNotFoundError("Participante nao encontrado")
    
        return HttpResponse(
            body={
                "cracha": {
                    "nome": cracha.nome,
                    "email": cracha.email,
                    "eventoTitulo": cracha.titulo
                }
            },
            status_code= 200
        )

    def obterParticipantePorEvento(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        participantes = self.__attendees_repository.get_attendees_by_event_id(event_id)
        if not participantes: raise HttpNotFoundError("Participantes nao encontrados")

        participantesFormatados = []
        for participante in participantes:
            participantesFormatados.append(
                {
                    "id": participante.id,
                    "name": participante.nome,
                    "email": participante.email,
                    "checkedInDataCriacao": participante.checkedInDataCriacao,
                    "dataCriacao": participante.dataCriacao
                }
            )

        return HttpResponse(
            body={ "participantes": participantesFormatados },
            status_code=200
        )