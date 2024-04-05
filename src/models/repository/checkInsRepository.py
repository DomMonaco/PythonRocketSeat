from src.models.settings.connection import db_connection_handler
from src.models.entities.checkIns import CheckIns
from sqlalchemy.exc import IntegrityError
from src.errors.error_types.http_conflict import HttpConflictError

class CheckInRepository:
    def inserirCheckIns(self, participanteId: str) -> str:
        with db_connection_handler as bancoDeDados:
            try:
                checkIin = (
                    CheckIns(participanteId=participanteId)
                )
                bancoDeDados.session.add(checkIin)
                bancoDeDados.session.commit()
                return participanteId
            except IntegrityError:
                raise HttpConflictError('Check In ja cadastrado!')
            except Exception as exception:
                bancoDeDados.session.rollback()
                raise exception
