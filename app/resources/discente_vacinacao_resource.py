from ..controller import DiscenteController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request

class DiscenteVacinacaoResource(Resource):
    
    ENDPOINT = 'discente_vacinacao'
    ROUTE = '/discente_vacinacao'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('matricula', type=str, required=False, help="You need to send query string maticula.")
        args = parser.parse_args()

        matricula = args.get("matricula_discente")

        if matricula:
            return DiscenteController.get_discente_vacinacao(matricula)

    @Authorization.token_required()
    def put(self):
        new_discente_vacinacao = request.json
        return DiscenteController.put(new_discente_vacinacao)