from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.participantes_handler import ParticipantesHandler
from src.errors.error_handler import handle_error

participantesRoute_bp = Blueprint("participantesRoute", __name__)

@participantesRoute_bp.route("/events/<eventoId>/register", methods=["POST"])
def create_attendees(eventoId):
    try:
        participantesHandler = ParticipantesHandler()
        http_request = HttpRequest(param={ "eventoId": eventoId }, body=request.json)

        http_response = participantesHandler.regitrar(http_request)
        return jsonify(http_response.body), http_response.statusCode
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.statusCode

@participantesRoute_bp.route("/participantes/<participanteId>/badge", methods=["GET"])
def obterParticipantesCracha(participanteId):
    try:
        participantesHandler = ParticipantesHandler()
        http_request = HttpRequest(param={ "participanteId": participanteId })

        http_response = participantesHandler.obterParticipanteCracha(http_request)
        return jsonify(http_response.body), http_response.statusCode
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.statusCode

@participantesRoute_bp.route("/eventos/<eventoId>/participantes", methods=["GET"])
def obterParticipantes(eventoId):
    try:
        participantesHandler = ParticipantesHandler()
        http_request = HttpRequest(param={ "eventoId": eventoId })

        http_response = participantesHandler.obterParticipantePorEvento(http_request)
        return jsonify(http_response.body), http_response.statusCode
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.statusCode
