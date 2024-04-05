from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.evento_handler import EventoHandler
from src.errors.error_handler import handle_error

eventoRoute_bp = Blueprint("eventoRoute", __name__)

@eventoRoute_bp.route("/eventos", methods=["POST"])
def criarEvento():
    try:
        http_request = HttpRequest(body=request.json)
        event_handler = EventoHandler()

        http_response = event_handler.registrar(http_request)
        return jsonify(http_response.body), http_response.statusCode
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.statusCode

@eventoRoute_bp.route("/eventos/<eventoId>", methods=["GET"])
def obterEvento(eventoId):
    try:
        event_handler = EventoHandler()
        http_request = HttpRequest(param={ "eventoId": eventoId })

        http_response = event_handler.obterPorId(http_request)
        return jsonify(http_response.body), http_response.statusCode
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.statusCode
