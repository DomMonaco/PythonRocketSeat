import pytest
from .participantesRepository import ParticipantesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_inserirParticipante():
    eventoId = "meu-uuid-e-nois"
    informacaoParticipantes = {
        "uuid": "meu_uuid_attendee3",
        "nome": "atendee name3",
        "email": "email3@email.com",
        "eventoId": eventoId
    }
    partipantesRepository = ParticipantesRepository()
    resposta = partipantesRepository.inserirPaticipantes(informacaoParticipantes)
    print(resposta)

@pytest.mark.skip(reason="...")
def test_obterParticipanteCrachaPorId():
    participanteId = "meu_uuid_attendee"
    partipantesRepository = ParticipantesRepository()
    participante = partipantesRepository.obterParticipanteCrachaPorId(participanteId)

    print(participante)
    print(participante.titulo)
