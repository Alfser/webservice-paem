from ..model import AcessoPermitidoModel
from .base_controller import BaseController

class AcessoPermitidoController(BaseController):
    
    @classmethod
    def get(cls, id):
        return super().get(id, AcessoPermitidoModel)

    @classmethod
    def post(cls, body):
        return super().post(body, AcessoPermitidoModel)

    @classmethod
    def put(cls, body):
        return super().put(body, AcessoPermitidoModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id,AcessoPermitidoModel)
    
    @classmethod
    def get_list(cls, campus_instituto_id_campus_instituto=None):
        return super().get_list(AcessoPermitidoModel, campus_instituto_id_campus_instituto)