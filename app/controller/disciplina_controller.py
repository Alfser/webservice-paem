from .base_controller import BaseHasCursoController
from ..model import DisciplinaModel
from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class DisciplinaController(BaseHasCursoController):
    
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
    def get_all_names(cls, curso_id_curso=None):
        return super().get_all_names(DisciplinaModel, curso_id_curso=curso_id_curso)