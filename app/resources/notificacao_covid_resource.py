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

class NotificacaoCovidQuantidadePorCampusResource(Resource):
      
      ENDPOINT = 'notificacoes_covid_quantidade_por_campus'
      ROUTE = '/notificacoes_covid/quantidade_por_campus'

      @Authorization.token_required()
      def get(self):
            parser = reqparse.RequestParser()
            parser.add_argument("id_campus_instituto", type=int, required=True, help="Precisa do argumento 'id_campus_instituto' na solicitação para acessar este recurso.")
            parser.add_argument("ano", type=int, required=True, help="Precisa do argumento 'ano' na solicitação para acessar este recurso.")
            args = parser.parse_args()
            id_campus_instituto = args.get('id_campus_instituto')
            ano = args.get('ano')
            return NotificacaoCovidController.contar_notificacao_por_campus(ano, id_campus_instituto)

class NotificacaoCovidQuantidadePorCursoResource(Resource):
      
      ENDPOINT = 'notificacoes_covid_quantidade_por_curso'
      ROUTE = '/notificacoes_covid/quantidade_por_curso'

      @Authorization.token_required()
      def get(self):
            parser = reqparse.RequestParser()
            parser.add_argument("id_campus_instituto", type=int, required=True, help="Precisa do argumento 'id_campus_instituto' na solicitação para acessar este recurso.")
            parser.add_argument("ano", type=int, required=True, help="Precisa do argumento 'ano' na solicitação para acessar este recurso.")
            args = parser.parse_args()
            id_campus_instituto = args.get('id_campus_instituto')
            ano = args.get('ano')
            return NotificacaoCovidController.contar_notificacao_por_curso(ano, id_campus_instituto)