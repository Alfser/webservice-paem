from ..controller import DisciplinaController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request


class DisciplinaResource(Resource):
    
    ENDPOINT = 'disciplina'
    ROUTE = '/disciplinas/disciplina'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_disciplina', type=int, required=False, help="Query string id_disciplina deve ser um inteiro.")
        args = parser.parse_args()
        id_disciplina = args.get("id_disciplina")
        
        return DisciplinaController.get(id_disciplina)

    @Authorization.token_required()
    def post(self):
        disciplina_body  = request.json.get('disciplina')
        discentes_matricula  = request.json.get('discentes')
        response = DisciplinaController.post(disciplina_body, discentes_matricula)
        if response[1]==201:
            pass

        return response

    @Authorization.token_required()
    def put(self):
        disciplina_body = request.json
        response = DisciplinaController.put(disciplina_body)
        return response

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

    @Authorization.token_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id_docente", type=int, required=True, help="query string id_docente deve ser um inteiro.")
        #parser.add_argument("id_discente", type=int, required=False, help="query string id_discente deve ser um inteiro.")
        args = parser.parse_args()
        id_docente = args.get("id_docente")
        #id_discente = args.get("id_discente")
          
        return DisciplinaController.get_all_names(docente_id_docente=id_docente)  
            