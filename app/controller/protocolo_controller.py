from ..model import ProtocoloModel
from .base_controller import BaseController

class ProtocoloController(BaseController):
    
    @classmethod
    def get(cls, id):
        return super().get(id, ProtocoloModel)

    @classmethod
    def post(cls, body):
        return super().post(body, ProtocoloModel)

    @classmethod
    def put(cls, body):
        return super().put(body, ProtocoloModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id, ProtocoloModel)
    
    @classmethod
    def get_list(cls):
        return super().get_list(ProtocoloModel)
