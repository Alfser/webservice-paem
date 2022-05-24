from ..controller import TecnicoController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request

class TecnicoResource(Resource):
    
    ENDPOINT = 'tecnico'
    ROUTE = '/tecnicos/tecnico'

    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):
        # parser = reqparse.RequestParser()
        # parser.add_argument('id_tecnico', type=int, required=False, help="Required query string id_tecnico.")
        # parser.add_argument('usuario_id_usuario', type=int, required=False, help="Query string usuario_id_usuario must be integer.")

        # args = parser.parse_args()
        # id_tecnico = args.get('id_tecnico')
        # usuario_id_usuario = args.get("usuario_id_usuario")

        # if id_tecnico:
        #     return TecnicoController.get(id_tecnico)
        
        if usuario:
            return TecnicoController.get_by_usuario(usuario.id_usuario) 

        return {"message":"there is no user logged."}, 401
    
    # @Authorization.token_required()
    def post(self):

        tecnico_body = request.json.get("tecnico")
        usuario_body = request.json.get("usuario")
        result, has_error = UsuarioController.create_usuario(usuario_body)

        if has_error:
            return result

        return TecnicoController.post(tecnico_body, result)

    @Authorization.token_required()
    def put(self):
        body = request.json
        return TecnicoController.put(body)

    @Authorization.token_required()
    def delete(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('id_tecnico', type=int, required=True, help="Required query string id_tecnico")
        
        args = parser.parse_args()
        id_tecnico = args.get('id_tecnico')

        return TecnicoController.delete(id_tecnico)

class TecnicoVacinacaoResource(Resource):
    
    ENDPOINT = 'tecnico_vacinacao'
    ROUTE = '/tecnico_vacinacao'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('siape', type=str, required=False, help="You need to send query string siape.")
        args = parser.parse_args()

        siape = args.get("siape")

        if siape:
            return TecnicoController.get_vacinacao(siape)

    @Authorization.token_required()
    def put(self):
        new_discente_vacinacao = request.json
        return TecnicoController.put(new_discente_vacinacao)

class ListaTecnicoResource(Resource):
    
    ENDPOINT = 'tenicos'
    ROUTE = '/tecnicos'
    
    @Authorization.token_required()
    def get(self):
        return TecnicoController.get_all_names()
