import uuid
from src.models.repository.participantesRepository import ParticipantesRepository
from src.models.repository.eventosRepository import EventosRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_conflict import HttpConflictError


class ParticipantesHandler:
    def __init__(self) -> None:
        self.__attendees_repository = ParticipantesRepository()
        self.__events_repository = EventosRepository()

    def regitrar(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        eventoId = http_request.param["eventoId"]

        event_attendees_count = self.__events_repository.quantidadeParticipantesEvento(eventoId)
        if (
            event_attendees_count["participantesQuantidade"]
            and event_attendees_count["maximoParticipantes"] < event_attendees_count["participantesQuantidade"]
        ): raise HttpConflictError("Evento Lotado")

        body["uuid"] = str(uuid.uuid4())
        body["eventoId"] = eventoId
        self.__attendees_repository.inserirPaticipantes(body)

        return HttpResponse(body=None, status_code=201)

    def obterParticipanteCracha(self, http_request: HttpRequest) -> HttpResponse:
        participanteId = http_request.param["participanteId"]
        cracha = self.__attendees_repository.obterParticipanteCrachaPorId(participanteId)
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
        eventoId = http_request.param["eventoId"]
        participantes = self.__attendees_repository.obterParticipantePorEventoId(eventoId)
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