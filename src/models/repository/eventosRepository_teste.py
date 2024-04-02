import pytest
from src.models.settings.connection import db_connection_handler
from .eventosRepository import EventosRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def teste_inserirEvento():
    evento = {
        "uuid" : "meu-uuid",
        "titulo" : "meu-titulo",
        "slug" : "meu-slug",
        "maximoParticipantes" : 20 
    }

    eventos_Repository = EventosRepository()
    resposta = eventos_Repository.inserirEvento(evento)
    print(resposta)

@pytest.mark.skip(reason="Nao necessita")
def teste_obterEventoPorId():
    eventoId = "meu_uuid"
    eventosRepository = EventosRepository()
    resposta = eventosRepository.obterEventoPorId(eventoId)
    print(resposta)
    print(resposta.titulo)