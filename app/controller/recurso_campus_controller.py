from .base_controller import BaseHasHorarioController
from ..model import RecursoCampusModel


class RecursoCampusController(BaseHasHorarioController):
    
    @classmethod
    def get(cls, id_recurso_campus):
        return super().get(id_recurso_campus, RecursoCampusModel)

    @classmethod
    def post(cls, body):
        return super().post(body, RecursoCampusModel)

    @classmethod
    def put(cls, body):
        return super().put(body, RecursoCampusModel)

    @classmethod
    def delete(cls, id_recurso_campus):
        return super().delete(id_recurso_campus, RecursoCampusModel)

    @classmethod
    def get_all_names(cls, campus_instituto_id_campus_instituto, usuario_id_usuario):
        return super().get_all_names(
            RecursoCampusModel, 
            campus_instituto_id_campus_instituto,
            usuario_id_usuario
        )