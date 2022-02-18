from ..util.http_status_code import NOT_FOUND_REQUEST, BAD_REQUEST, FORBIDDEN_REQUEST, CREATED, OK
from ..util.authorization import Authorization
from ..controller import SolicitacaoAcessoController

from flask_restful import Resource, reqparse, request


class SolicitacaoAcessoResource(Resource):
    
    ENDPOINT = 'solicitacao_acesso'
    ROUTE = '/solicitacoes_acessos/solicitacao_acesso'

    @Authorization.token_required()
    def get(self):
        
        parser = reqparse.RequestParser()
        parser.add_argument("id_discente", type=int, help="Required query string integer id_discente.")
        parser.add_argument("id_solicitacao_acesso", type=int, help="Required query string integer id_solicitacao_acesso.")
        
        args = parser.parse_args(strict=True)
        id_solicitacao_acesso = args.get("id_solicitacao_acesso")
        id_discente = args.get("id_discente")

        if id_discente:
            return SolicitacaoAcessoController.get_id_discente(id_discente)

        if id_solicitacao_acesso:
            return SolicitacaoAcessoController.get(id_solicitacao_acesso)    

        return {"message":"Required query string id_solicitacao_acesso or id_discente."}, BAD_REQUEST

    @Authorization.token_required(with_usuario=True)
    def post(self, usuario):
        body = request.json
        body["campus_instituto_id_campus_instituto"] = usuario.campus_instituto_id_campus_instituto
        return SolicitacaoAcessoController.post(body)

    @Authorization.token_required(with_usuario=True)
    def put(self, usuario):
        body = request.json
        body["campus_instituto_id_campus_instituto"] = usuario.campus_instituto_id_campus_instituto
        return SolicitacaoAcessoController.put(body)

    @Authorization.token_required()
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument("id_solicitacao_acesso", type=int, required=True, help="Precisa do argumento id_solicitação_acesso na solicitação para acessar a solicitação do mesmo.")
        
        args = parser.parse_args()
        id_solicitacao_acesso = args.get('id_solicitacao_acesso')
        
        return SolicitacaoAcessoController.delete(id_solicitacao_acesso)

class ListaSolicitacaoAcessoResource(Resource):
    
    ENDPOINT = 'solicitacoes_acessos'
    ROUTE = '/solicitacoes_acessos'
    
    @Authorization.token_required(with_usuario=True)
    def get(self, usuario):
        return SolicitacaoAcessoController.get_list(usuario.campus_instituto_id_campus_instituto)

class SolicitacaoAcessoQuantidadePorCampusResource(Resource):
    
    ENDPOINT = 'solicitacoes_acessos_quantidade_por_campus'
    ROUTE = '/solicitacoes_acessos/quantidade_por_campus'
    
    @Authorization.token_required()
    def get(self):
        return SolicitacaoAcessoController.contar_agendamento_por_campus()

class SolicitacaoAcessoQuantidadePorRecursoCampusResource(Resource):
    
    ENDPOINT = 'solicitacoes_acessos_quantidade_por_recurso_campus'
    ROUTE = '/solicitacoes_acessos/quantidade_por_recurso_campus'
    
    @Authorization.token_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id_campus_instituto", type=int, required=True, help="Precisa do argumento 'id_campus_instituto' na solicitação para acessar a solicitação deste recurso.")
        parser.add_argument("ano", type=int, required=True, help="Precisa do argumento 'ano' para solicitação deste recurso.")
        parser.add_argument("mes", type=int, required=True, help="Precisa do argumento 'mes' para solicitação deste recurso.")
        args = parser.parse_args()
        id_campus_instituto = args.get('id_campus_instituto')
        ano = args.get('ano')
        mes = args.get('mes')

        return SolicitacaoAcessoController.contar_agendamento_por_recurso_campus(ano, mes, id_campus_instituto)

class SolicitacaoAcessoPorCursoResource(Resource):
    
    ENDPOINT = 'solicitacoes_acessos_quantidade_por_curso'
    ROUTE = '/solicitacoes_acessos/quantidade_por_curso'
    
    @Authorization.token_required()
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id_campus_instituto", type=int, required=True, help="Precisa do argumento 'id_campus_instituto' na solicitação para a solicitação deste recurso.")
        parser.add_argument("ano", type=int, required=True, help="Precisa do argumento 'ano' para solicitação deste recurso.")
        parser.add_argument("mes", type=int, required=True, help="Precisa do argumento 'mes' para solicitação deste recurso.")
        args = parser.parse_args()
        id_campus_instituto = args.get('id_campus_instituto')
        ano = args.get('ano')
        mes = args.get('mes')

        return SolicitacaoAcessoController.contar_agendamento_por_curso(ano, mes, id_campus_instituto)
    
