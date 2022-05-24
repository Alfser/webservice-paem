from ..controller import DiscenteController, UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, reqparse, request
class DiscenteResource(Resource):
    
    ENDPOINT = 'discente'
    ROUTE = '/discentes/discente'
    
    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):

        # parser = reqparse.RequestParser()
        # parser.add_argument('matricula', type=str, required=False, help="You need to send query string maticula.")
        # parser.add_argument('id_discente', type=int, required=False, help="Query string id_discente must be integer.")
        # parser.add_argument('usuario_id_usuario', type=int, required=False, help="Query string usuario_id_usuario must be integer.")

        # args = parser.parse_args()

        # matricula = args.get("matricula")
        # id_discente = args.get("id_discente")
        # usuario_id_usuario = args.get("usuario_id_usuario")

        # if matricula:
        #     return DiscenteController.get_by_matricula(matricula)

        # if id_discente:
        #     return DiscenteController.get(id_discente)
        
        if usuario:
            return DiscenteController.get_by_usuario(usuario.id_usuario) 
        
        return {"message":" Usuário não encontrado."}, 404

    # @Authorization.token_required()
    def post(self):

        discente_body  = request.json.get("discente")
        usuario_body = request.json.get("usuario")
        result, has_error = UsuarioController.create_usuario(usuario_body)

        if has_error:
            return result
        
        return DiscenteController.post(discente_body, result)
      
    @Authorization.token_required()
    def put(self):
        discente = request.json
        return DiscenteController.put(discente)

    @Authorization.token_required()
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument("id_discente", type=int, required=True, help="query string id_discente não encontrada")

        args = parser.parse_args(strict=True)
        id_discente = args.get("id_discente")

        return DiscenteController.delete(id_discente)

class DiscenteVacinacaoResource(Resource):
    
    ENDPOINT = 'discente_vacinacao'
    ROUTE = '/discente_vacinacao'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('matricula', type=str, required=False, help="You need to send query string maticula.")
        args = parser.parse_args()

        matricula = args.get("matricula")

        if matricula:
            return DiscenteController.get_vacinacao(matricula)

    @Authorization.token_required()
    def put(self):
        new_discente_vacinacao = request.json
        return DiscenteController.put(new_discente_vacinacao)

class ListaDiscenteVacinacaoResource(Resource):
    
    ENDPOINT = 'discentes_vacinacoes'
    ROUTE = '/discentes_vacinacoes'
    
    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('curso_id_curso', type=str, required=False, help="Precisa enviar a query string curso_id_curso.")
        parser.add_argument('ano_turma', type=str, required=False, help="Precisa enviar um intero na query string turma, que é o ano de entrada dos discentes na turma.")
        parser.add_argument('numero_de_doses', type=str, required=False, help="Precisa enviar um intero na query string numero_de_doses.")
        args = parser.parse_args()

        curso_id_curso = args.get("curso_id_curso")
        ano_turma = args.get("ano_turma")
        numero_de_doses = args.get("numero_de_doses")
        
        return DiscenteController.get_vacinacoes(curso_id_curso, ano_turma, numero_de_doses)

class ListaDiscenteResource(Resource):
      
      ENDPOINT = 'discentes'
      ROUTE = '/discentes'

      @Authorization.token_required()
      def get(self):
          return DiscenteController.get_all_names()

class DiscenteVacinadosPorCursoResource(Resource):
      
      ENDPOINT = 'discentes_vacinados_por_curso'
      ROUTE = '/discentes/quantidade_vacinados_por_curso'

      @Authorization.token_required()
      def get(self):
            parser = reqparse.RequestParser()
            parser.add_argument("id_campus_instituto", type=int, required=True, help="Precisa do argumento 'id_campus_instituto' na solicitação para acessar este recurso.")
            args = parser.parse_args()
            id_campus_instituto = args.get('id_campus_instituto')
            return DiscenteController.contar_vacinados_por_curso(id_campus_instituto)