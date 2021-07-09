from ..model import TecnicoModel
from .base_controller import BaseHasOtherIdController, BaseHasUsuarioController

class TecnicoController(BaseHasUsuarioController, BaseHasOtherIdController):
    
    @classmethod
    def get(cls, id_tecnico):
        return super().get(id_tecnico, TecnicoModel)

    @classmethod
    def get_by_usuario(cls, usuario_id_usuario):
        return super().get_by_usuario(usuario_id_usuario, TecnicoModel)

    @classmethod
    def post(cls, body, usuario):
        return super().post(body, TecnicoModel, usuario=usuario)

    @classmethod
    def put(cls, body):
        return super().put(body, TecnicoModel)

    @classmethod
    def delete(cls, id_tecnico):
        return super().delete(id_tecnico, TecnicoModel)

    @classmethod
    def get_all_names(cls):
        return super().get_all_names(TecnicoModel)