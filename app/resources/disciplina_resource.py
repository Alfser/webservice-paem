from ..controller import DisciplinaController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request


class DisciplinaResource(Resource):
    
    ENDPOINT = 'disciplina'
    ROUTE = '/disciplinas/disciplina'
    
    @Authorization.token_required(with_usuario=True)
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_disciplina', type=int, required=False, help="Query string id_disciplina deve ser um inteiro.")
        args = parser.parse_args()
        id_disciplina = args.get("id_disciplina")
        
        return DisciplinaController.get(id_disciplina)

    @Authorization.token_required()
    def post(self):
        disciplina_body  = request.json
        return DisciplinaController.post(disciplina_body)
      
    @Authorization.token_required()
    def put(self):
        disciplina_body = request.json
        return DisciplinaController.put(disciplina_body)

    @Authorization.token_required()
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id_disciplina", type=int, required=True, help="query string id_disciplina deve ser um inteiro.")
        args = parser.parse_args(strict=True)
        id_disciplina = args.get("id_disciplina")

        return DisciplinaController.delete(id_disciplina)

class ListaDisciplinaResource(Resource):
      
      ENDPOINT = 'disciplinas'
      ROUTE = '/disciplinas'

      @Authorization.token_required(with_usuario=True)
      def get(self, usuario):
          return DisciplinaController.get_all_names(usuario.campus_instituto_id_campus_instituto)