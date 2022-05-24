from ..model import UsuarioModel
from .base_controller import BaseHasCPFController
from ..util.http_status_code import BAD_REQUEST

class UsuarioController(BaseHasCPFController):

    @classmethod
    def create_usuario(cls, usuario_dict):
        has_error = True
        try:
            usuario = UsuarioModel(**usuario_dict)
        except Exception as msg:
            return {'message':msg.args[0]} , has_error
        return usuario, not has_error

    @classmethod
    def get(cls, id):
        return cls.get(id, UsuarioModel)

    @classmethod
    def post(cls, body):
        return super().post(body, UsuarioModel)

    @classmethod
    def put(cls, body):
        return super().put(body, UsuarioModel)
    
    @classmethod
    def delete(cls, id):
        return super().delete(id, UsuarioModel)
    
    @classmethod
    def get_all_names(cls):
        return super().get_all_names(UsuarioModel)
    
    @classmethod
    def get_by_login(cls, login):
        return UsuarioModel.find_by_login(login)
    
    @classmethod
    def get_by_email(cls, email):
        return UsuarioModel.find_by_email(email)

    @classmethod
    def get_by_cpf(cls, cpf):
        return UsuarioModel.find_by_cpf(cpf)