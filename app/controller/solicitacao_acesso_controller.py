from ..model import SolicitacaoAcessoModel
from ..util.http_status_code import BAD_REQUEST

from .base_controller import BaseController


class SolicitacaoAcessoController(BaseController):
   
    @classmethod
    def get(cls, id):
        return super().get(id, SolicitacaoAcessoModel)

    @classmethod
    def get_id_discente(cls, id_discente):
        return SolicitacaoAcessoModel.find_by_id_discente(id_discente)

    @classmethod
    def post(cls, body):
        return super().post(body, SolicitacaoAcessoModel)

    @classmethod
    def put(cls, body):
        try:
            response = super().put(body, SolicitacaoAcessoModel)
            return response

        except ValueError as msg:
            return {"message":msg}, BAD_REQUEST 

    @classmethod
    def delete(cls, id):
        return super().delete(id, SolicitacaoAcessoModel)

    @classmethod
    def get_list(cls):
        return super().get_list(SolicitacaoAcessoModel)