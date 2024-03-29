
from app.model import campus_instituto
from ..controller import RecursoCampusController
from ..util.authorization import Authorization
from ..util.http_status_code import BAD_REQUEST
from flask_restful import Resource, reqparse, request


class RecursoCampusResource(Resource):

    ENDPOINT = 'recurso_campus'
    ROUTE = '/recursos_campus/recurso_campus'

    @Authorization.token_required()
    def get(self):
      parser = reqparse.RequestParser()
      parser.add_argument('id_recurso_campus', type=int, required=True, help='Required query string id_recurso_campus.')
      
      args = parser.parse_args()
      id_recurso_campus = args.get('id_recurso_campus')
      return RecursoCampusController.get(id_recurso_campus)

    @Authorization.token_required(with_usuario=True)
    def post(self, usuario):
        body = request.json
        body["campus_instituto_id_campus_instituto"] = usuario.campus_instituto_id_campus_instituto
        return RecursoCampusController.post(body)
    
    @Authorization.token_required(with_usuario=True)
    def put(self, usuario):
      body = request.json
      body["campus_instituto_id_campus_instituto"] = usuario.campus_instituto_id_campus_instituto
      return RecursoCampusController.put(body)

    @Authorization.token_required()
    def delete(self):
      parser = reqparse.RequestParser()
      parser.add_argument('id_recurso_campus', type=int, required=True, help='Required query string id_recurso_campus.')

      args = parser.parse_args()
      id_recurso_campus = args.get('id_recurso_campus')
      return RecursoCampusController.delete(id_recurso_campus)


class ListaRecursoCampusResource(Resource):

    ENDPOINT = 'recursos_campus'
    ROUTE = '/recursos_campus'

    @Authorization.token_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('usuario_id_usuario', type=int, required=False, help='Required query string usuario_id_usuario.')
        parser.add_argument('campus_instituto_id_campus_instituto', type=int, required=False, help='Required query string campus_instituto_id_campus_instituto.')
        
        args = parser.parse_args()
        
        usuario_id_usuario = args.get('usuario_id_usuario')
        campus_instituto_id_campus_instituto = args.get('campus_instituto_id_campus_instituto')
        if usuario_id_usuario or campus_instituto_id_campus_instituto:
          return RecursoCampusController.get_all_names(
          campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto, 
          usuario_id_usuario=usuario_id_usuario
        )
        
        return RecursoCampusController.get_all_names(None, None)