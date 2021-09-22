from app.util.authorization import Authorization
from ..controller import ProtocoloController
from flask_restful import reqparse, request, Resource

class ProtocoloResource(Resource):

    ENDPOINT = 'protocolo'
    ROUTE = '/protocolos/protocolo'

    # @Authorization.token_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_protocolo', type=int, required=True, help='Required query string id_protocolo.')
        args = parser.parse_args()
        id_protocolo = args.get('id_protocolo')
        return ProtocoloController.get(id_protocolo)

    # @Authorization.token_required()
    def post(self):
        body = request.json
        return ProtocoloController.post(body)

    # @Authorization.token_required()
    def put(self):
        body = request.json
        return ProtocoloController.put(body)

    # @Authorization.token_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_protocolo', type=int, required=True, help='Required query string id_protocolo.')
        args = parser.parse_args()
        id_protocolo = args.get('id_protocolo')
        return ProtocoloController.delete(id_protocolo)


class ListaProtocolosResource(Resource):

    ENDPOINT = 'protocolos'
    ROUTE = '/protocolos'

    # @Authorization.token_required()
    def get(self):
        return ProtocoloController.get_list()