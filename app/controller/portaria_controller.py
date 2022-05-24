from ..model import PortariaModel
from .base_controller import BaseHasUsuarioController, BaseHasSiapeController


class PortariaController(BaseHasUsuarioController):
    
    @classmethod
    def get(cls, id_portaria):
        return super().get(id_portaria, PortariaModel)

    # @classmethod
    # def get_vacinacao(cls, siape):
        # return super().get_vacinacao(PortariaModel, siape)

    @classmethod
    def get_by_usuario(cls, usuario_id_usuario):
        return super().get_by_usuario(usuario_id_usuario, PortariaModel)

    @classmethod
    def post(cls, body, usuario):
        return super().post(body, PortariaModel, usuario=usuario)

    @classmethod
    def put(cls, body):
        return super().put(body, PortariaModel)

    @classmethod
    def delete(cls, id_portaria):
        return super().delete(id_portaria, PortariaModel)

    @classmethod
    def get_all_names(cls, campus_instituto_id_campus_instituto):
        return super().get_all_names(
            PortariaModel, 
            campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto)