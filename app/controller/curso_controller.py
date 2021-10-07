from ..model import CursoModel
from .base_controller import BaseHasNameController

class CursoController(BaseHasNameController):
    
    @classmethod
    def get(cls, id):
        return super().get(id, CursoModel)

    @classmethod
    def post(cls, body):
        return super().post(body, CursoModel)

    @classmethod
    def put(cls, body):
        return super().put(body, CursoModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id, CursoModel)

    @classmethod
    def get_all_names(cls, campus_instituto_id_campus_instituto=None):
        return super().get_all_names(CursoModel, campus_instituto_id_campus_instituto)