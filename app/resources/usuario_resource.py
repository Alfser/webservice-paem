from ..util.http_status_code import BAD_REQUEST, FORBIDDEN_REQUEST, NOT_FOUND_REQUEST, OK
from ..util.authorization import Authorization

from ..controller import UsuarioController
from flask_restful import Resource, reqparse, request


class UsuarioResource(Resource):
    ENDPOINT = 'usuario'
    ROUTE = '/usuarios/usuario'

    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):

        # parser = reqparse.RequestParser()
        # parser.add_argument('id_usuario', type=str, required=True, help="You need to send query string id_usuario.")
        # args = parser.parse_args(strict=True)
        # id_usuario = args.get('id_usuario')
        return usuario.serialize()

    # @Authorization.token_required
    # def post(self):
    #     body = request.json
    #     return UsuarioController.post(body)
      
    @Authorization.token_required
    def put(self):
        body = request.json
        return UsuarioController.put(body)

    @Authorization.token_required
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_usuario', type=str, required=True, help="You need to send query string id_usuario.")

        args = parser.parse_args(strict=True)
        id_usuario = args.get('id_usuario')

        return UsuarioController.delete(id_usuario)

class ListaUsuarioResource(Resource):

    ENDPOINT = 'users'
    ROUTE = '/usuarios'

    @Authorization.token_required()
    def get(self):
        return UsuarioController.get_all_names()