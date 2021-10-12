from .base_controller import BaseHasNameController
from ..model import DisciplinaModel
from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class DisciplinaController(BaseHasNameController):
    
    @classmethod
    def get(cls, id_disciplina):
        return super().get(id_disciplina, DisciplinaModel)

    @classmethod
    def post(cls, body):
        return super().post(body, DisciplinaModel)

    @classmethod
    def put(cls, body):
        return super().put(body, DisciplinaModel)

    @classmethod
    def delete(cls, id_disciplina):
        return super().delete(id_disciplina, DisciplinaModel)

    @classmethod
    def get_all_names(cls, campus_instituto_id_campus_instituto=None):
        return super().get_all_names(DisciplinaModel, campus_instituto_id_campus_instituto)