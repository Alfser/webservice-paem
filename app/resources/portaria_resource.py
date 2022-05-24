from ..controller import PortariaController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request

class PortariaResource(Resource):
    
    ENDPOINT = 'portaria'
    ROUTE = '/portarias/portaria'

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
            return PortariaController.get_by_usuario(usuario.id_usuario) 

        return {"message":"there is no user logged."}, 401
    
    # @Authorization.token_required()
    def post(self):

        portaria_body = request.json.get("portaria")
        usuario_body = request.json.get("usuario")
        result, has_error = UsuarioController.create_usuario(usuario_body)

        # if usuario variable is an  dict mean an error has occorred.
        if has_error:
            return result

        return PortariaController.post(portaria_body, result)

    @Authorization.token_required()
    def put(self):
        body = request.json
        return PortariaController.put(body)

    @Authorization.token_required()
    def delete(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument('id_portaria', type=int, required=True, help="Required query string id_portaria")
        
        args = parser.parse_args()
        id_portaria = args.get('id_portaria')

        return PortariaController.delete(id_portaria)


'''class PortariaVacinacaoResource(Resource):
    
    ENDPOINT = 'portaria_vacinacao'
    ROUTE = '/portaria_vacinacao'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('siape', type=str, required=False, help="You need to send query string siape.")
        args = parser.parse_args()

        siape = args.get("siape")

        if siape:
            return PortariaController.get_vacinacao(siape)

    @Authorization.token_required()
    def put(self):
        new_portaria_vacinacao = request.json
        return PortariaController.put(new_portaria_vacinacao)
    '''
class ListaPortariaResource(Resource):
    
    ENDPOINT = 'portarias'
    ROUTE = '/portarias'
    
    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):
        return PortariaController.get_all_names(usuario.campus_instituto_id_campus_instituto)
