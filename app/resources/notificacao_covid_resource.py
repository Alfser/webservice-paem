from ..controller import NotificacaoCovidController
from ..util.authorization import Authorization

from flask_restful import Resource, request, reqparse


class NotificacaoCovidResource(Resource):
    
    ENDPOINT = 'notificacao_covid'
    ROUTE = '/notificacoes_covid/notificacao_covid'
        
    @Authorization.token_required()
    def get(self):        
        parser = reqparse.RequestParser()
        parser.add_argument("id_notificacao_covid", type=int, required=True, help="Exije um valor inteiro para query string id_notificacao_covid")
        args = parser.parse_args()
        id_notificacao_covid = args.get("id_notificacao_covid")
        return NotificacaoCovidController.get(id_notificacao_covid)
    
    @Authorization.token_required(with_usuario=True)
    def post(self, usuario):
        body = request.json
        body["campus_instituto_id_campus_instituto"] = usuario.campus_instituto_id_campus_instituto
        return NotificacaoCovidController.post(body)
    
    @Authorization.token_required(with_usuario=True)
    def put(self, usuario):
        body = request.json
        body["campus_instituto_id_campus_instituto"] = usuario.campus_instituto_id_campus_instituto
        return NotificacaoCovidController.put(body)
    
    @Authorization.token_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id_notificacao_covid", type=int, required=True, help="Exije um valor inteiro para query string id_notificacao_covid")
        args = parser.parse_args()
        id_notificacao_covid = args.get("id_notificacao_covid")    
        return NotificacaoCovidController.delete(id_notificacao_covid)
       
class ListaNotificacaoCovidResource(Resource):
    
    ENDPOINT = 'notificacoes_covid'
    ROUTE = '/notificacoes_covid'
    
    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):
        return NotificacaoCovidController.get_list(usuario.campus_instituto_id_campus_instituto)