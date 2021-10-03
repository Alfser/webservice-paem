from ..model import PontoVerificacaoModel
from .base_controller import BaseHasUsuarioController, BaseHasNameController


class PontoVerificacaoController(BaseHasUsuarioController, BaseHasNameController):

    @classmethod
    def get(cls, id_usuario):
        return super().get(id_usuario, PontoVerificacaoModel)
    
    @classmethod
    def post(cls, body, usuario):
        return super().post(body, PontoVerificacaoModel, usuario=usuario)
    
    @classmethod
    def put(cls, body):
        return super().put(body, PontoVerificacaoModel)

    @classmethod
    def delete(cls, id_ponto_verificacao):
        return super().delete(id_ponto_verificacao, PontoVerificacaoModel)
    
    @classmethod
    def get_list(cls):
        return super().get_all_names(PontoVerificacaoModel)
    
