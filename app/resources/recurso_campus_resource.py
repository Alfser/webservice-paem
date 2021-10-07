
from ..controller import RecursoCampusController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request


class RecursoCampusResource(Resource):

    ENDPOINT = 'recurso_campus'
    ROUTE = '/recursos_campus/recurso_campus'

    @Authorization.token_required()
    def get(self):
      parser = reqparse.RequestParser()
      parser.add_argument('id_recurso_campus', type=int, required=True, help='Required query string id_recurso.')
      
      args = parser.parse_args()
      id_recurso_campus = args.get('id_recurso_campus')
      return RecursoCampusController.get(id_recurso_campus)

    @Authorization.token_required()
    def post(self):
        body = request.json
        return RecursoCampusController.post(body)
    
    @Authorization.token_required()
    def put(self):
      body = request.json
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

    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):
        
        return RecursoCampusController.get_all_names(usuario.campus_instituto_id_campus_instituto)