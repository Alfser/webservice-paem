
from ..controller import DocenteController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request
class DocenteResource(Resource):
    ENDPOINT = 'docente'
    ROUTE = '/docentes/docente'

    @Authorization.token_required(with_usuario=True)    
    def get(self, usuario):
        # parse = reqparse.RequestParser()
        # parse.add_argument("id_docente", required=False, type=int, help="Query string id_discente must be integer")
        # parse.add_argument("usuario_id_usuario", Required=True, type=int, help="Query string usuario_id_usuario must be integer")
        
        # args = parse.parse_args()
        # id_docente = args.get("id_docente")
        # usuario_id_usuario = args.get("usuario_id_usuario")

        # if id_docente:
            # DocenteController.get(id_docente)

        if usuario:
            return DocenteController.get_by_usuario(usuario.id_usuario)
        
        return {"message": "there is no user logged."}
    
    def post(self):
        body = request.json
        docente_body = body.get("docente")
        usuario_body = body.get("usuario")
        result, has_error = UsuarioController.create_usuario(usuario_body)

        if has_error:
            return result

        return DocenteController.post(docente_body, usuario=result)

    @Authorization.token_required()
    def put(self):
        body = request.json
        return DocenteController.put(body)
    
    @Authorization.token_required()
    def delete(self):
        parse = reqparse.RequestParser()
        parse.add_argument("id_docente", required=True, type=int, help="Query string id_discente must be integer")
        args = parse.parse_args(strict=True)
        id_docente = args.get("id_docente")

        return DocenteController.delete(id_docente)

class DocenteVacinacaoResource(Resource):
    
    ENDPOINT = 'docente_vacinacao'
    ROUTE = '/docente_vacinacao'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('siape', type=str, required=False, help="You need to send query string siape.")
        args = parser.parse_args()

        siape = args.get("siape")

        if siape:
            return DocenteController.get_vacinacao(siape)

    @Authorization.token_required()
    def put(self):
        new_docente_vacinacao = request.json
        return DocenteController.put(new_docente_vacinacao)

class ListaDocenteResource(Resource):
    
    ENDPOINT = 'docentes'
    ROUTE = '/docentes'

    @Authorization.token_required()
    def get(self):
        return DocenteController.get_all_names()    
