from ..model import NotificacaoCovidModel
from .base_controller import BaseController


class NotificacaoCovidController(BaseController):
    
    @classmethod
    def get(cls, id):
        return super().get(id, NotificacaoCovidModel)

    @classmethod
    def post(cls, body):
        return super().post(body, NotificacaoCovidModel)

    @classmethod
    def put(cls, body):
        return super().put(body, NotificacaoCovidModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id,NotificacaoCovidModel)
    
    @classmethod
    def get_list(cls, campus_instituto_id_campus_instituto=None):
        return super().get_list(NotificacaoCovidModel, campus_instituto_id_campus_instituto)

    @classmethod
    def contar_notificacao_por_campus(cls, ano, id_campus_instituto):
        return NotificacaoCovidModel.contar_notificacao_por_campus(ano, id_campus_instituto)
    
    @classmethod
    def contar_notificacao_por_curso(cls, ano, id_campus_instituto):
        return NotificacaoCovidModel.contar_notificacao_por_curso(ano, id_campus_instituto)
