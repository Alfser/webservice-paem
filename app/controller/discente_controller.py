from .base_controller import BaseHasOtherIdController, BaseHasUsuarioController
from ..model import DiscenteModel
from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class DiscenteController(BaseHasUsuarioController, BaseHasOtherIdController):
    
    @classmethod
    def get_by_matricula(cls, matricula):

        discente = DiscenteModel.find_by_matricula(matricula)
        if not discente:
            return {"message":"Not found this discente."}, NOT_FOUND_REQUEST
      
        return discente.serialize(), OK

    @classmethod
    def get(cls, id):
        return super().get(id, DiscenteModel)
    
    @classmethod
    def get_by_usuario(cls, usuario_id_usuario):
        return super().get_by_usuario(usuario_id_usuario, DiscenteModel)

    @classmethod
    def get_discente_vacinacao(cls, matricula_dsicente):
        json_discente_vacinacao = DiscenteModel.get_discente_vacinacao(matricula=matricula_dsicente)
        if json_discente_vacinacao:
            return json_discente_vacinacao, OK
        return {"message":"Not found status vacinacao of this discente."}, NOT_FOUND_REQUEST

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