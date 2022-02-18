from .base_controller import BaseHasMatriculaController, BaseHasUsuarioController
from ..model import DiscenteModel
from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class DiscenteController(BaseHasUsuarioController, BaseHasMatriculaController):
    
    @classmethod
    def get(cls, id):
        return super().get(id, DiscenteModel)
    
    @classmethod
    def get_vacinacao(cls, matricula):
        return super().get_vacinacao(DiscenteModel, matricula)

    @classmethod
    def get_by_usuario(cls, usuario_id_usuario):
        return super().get_by_usuario(usuario_id_usuario, DiscenteModel)

    @classmethod
    def post(cls, body, usuario):
        return super().post(body, DiscenteModel, usuario=usuario)

    @classmethod
    def put(cls, body):
        return super().put(body, DiscenteModel)

    @classmethod
    def delete(cls, id_discente):
        return super().delete(id_discente, DiscenteModel)

    @classmethod
    def get_all_names(cls):
        return super().get_all_names(DiscenteModel)
    
    @classmethod
    def contar_vacinados_por_curso(cls, id_campus_instituto):
        return DiscenteModel.contar_vacinados_por_curso(id_campus_instituto)