import uuid
from src.models.repository.eventosRepository import EventosRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError

class EventoHandler:
    def __init__(self) -> None:
        self.__events_repository = EventosRepository()

    def registrar(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.inserirEvento(body)

        return HttpResponse(
            body={ "eventoId": body["uuid"] },
            status_code=200
        )

    def obterPorId(self, http_request: HttpRequest) -> HttpResponse:
        eventoId = http_request.param["eventoId"]
        evento = self.__events_repository.get_event_by_id(eventoId)
        if not evento: raise HttpNotFoundError("Evento não encontrado")

        event_attendees_count = self.__events_repository.quantidadeParticipantesEvento(eventoId)

        return HttpResponse(
            body={
                "evento": {
                    "id": evento.id,
                    "titulo": evento.titulo,
                    "detalhes": evento.detalhes,
                    "slug": evento.slug,
                    "maximoParticipantes": evento.maximoParticipantes,
                    "participantesQuantidade": event_attendees_count["participantesQuantidade"]
                }
            },
            status_code=200
        )
