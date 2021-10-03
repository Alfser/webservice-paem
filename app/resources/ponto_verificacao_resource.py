from ..controller import PontoVerificacaoController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import reqparse, request, Resource

class PontoVerificacaoResource(Resource):

    ENDPOINT = 'ponto_verificacao'
    ROUTE = '/pontos_verificacao/ponto_verificacao'

    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):
        return PontoVerificacaoController.get_by_usuario(usuario.id_usuario)
            
    @Authorization.token_required()
    def post(self):
        res = request.json
        ponto_verificacao_body = res.get("ponto_verificacao")
        usuario_body = res.get("usuario")
        usuario = UsuarioController.create_usuario(usuario_body)
        return PontoVerificacaoController.post(ponto_verificacao_body, usuario=usuario)
    
    @Authorization.token_required()
    def put(self):
        body = request.json
        return PontoVerificacaoController.put(body)

    @Authorization.token_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_ponto_verificacao', type=int, required=True, help='Required query string id_ponto_verificacao.')
        args = parser.parse_args()

        id_ponto_verificacao = args.get('id_ponto_verificacao')
        return PontoVerificacaoController.delete(id_ponto_verificacao)


class ListaPontoVerificacaoResource(Resource):

    ENDPOINT = 'pontos_verificacao'
    ROUTE = '/pontos_verificacao'

    @Authorization.token_required()
    def get(self):
        return PontoVerificacaoController.get_list()
