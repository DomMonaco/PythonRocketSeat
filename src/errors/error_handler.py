from src.http_types.http_response import HttpResponse
from .error_types.http_conflict import HttpConflictError
from .error_types.http_not_found import HttpNotFoundError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpConflictError, HttpNotFoundError)):
        return HttpResponse(
            body={
                "errors": [{
                    "titulo": error.nome,
                    "detalhes": error.mensagem
                }]
            },
            status_code=error.statusCode
        )

    return HttpResponse(
        body={
            "errors": [{
                "titulo": "error",
                "detalhes": str(error)
            }]
        }
    )
