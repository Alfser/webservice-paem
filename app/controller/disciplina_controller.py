from .base_controller import BaseHasDiscentesListController
from ..model import DisciplinaModel, DiscenteModel
from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class DisciplinaController(BaseHasDiscentesListController):
    
    @classmethod
    def get(cls, id_disciplina):
        return super().get(id_disciplina, DisciplinaModel)

    @classmethod
    def post(cls, body, discentes_matricula):
        discentes = list()
        for matricula in discentes_matricula:
            discenteModel = DiscenteModel.find_by_matricula(matricula)
            discentes.append(discenteModel)

        return super().post(body, DisciplinaModel, discentes)

    @classmethod
    def put(cls, body):
        return super().put(body, DisciplinaModel)

    @classmethod
    def delete(cls, id_disciplina):
        return super().delete(id_disciplina, DisciplinaModel)

    @classmethod
    def get_all_names(cls, 
                docente_id_docente=None,
            ):
        return super().get_all_names(
            DisciplinaModel, 
            docente_id_docente=docente_id_docente
        )