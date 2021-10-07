from ..controller import CursoController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request

class CursoResource(Resource):
    
    ENDPOINT = "curso"
    ROUTE =  "/cursos/curso"

    @Authorization.token_required()
    def get(self):
        
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("id_curso", required=True, type=int, help="query string id_curso não encontrado na requisição.")
        args = parser.parse_args(strict=True)
        id_curso = args.get("id_curso")

        return CursoController.get(id_curso)

    @Authorization.token_required()
    def post(self):
        body = request.json
        return CursoController.post(body)
    
    @Authorization.token_required()
    def put(self):
        body = request.json
        return CursoController.put(body)

    @Authorization.token_required()
    def delete(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("id_curso", required=True, type=int, help="query string id_curso não encontrado na requisição.")
        args = parser.parse_args(strict=True)
        id_curso = args.get("id_curso")

        return CursoController.delete(id_curso)

class ListaCursoResource(Resource):
    
    ENDPOINT = "cursos"
    ROUTE = "/cursos"

    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):
        return CursoController.get_all_names(usuario.campus_instituto_id_campus_instituto)

