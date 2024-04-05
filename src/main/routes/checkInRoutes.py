from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.checkIn_handler import CheckInHandler
from src.errors.error_handler import handle_error

checkInRoutes_bp = Blueprint("checkInRoute", __name__)

@checkInRoutes_bp.route("/participantes/<participanteId>/checkIn", methods=["POST"])
def criarCheckIn(participanteId):
    try:
        checkInHandler = CheckInHandler()
        http_request = HttpRequest(param={ "participanteId": participanteId })
        http_response = checkInHandler.registrar(http_request)

        return jsonify(http_response.body), http_response.statusCode
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.statusCode
