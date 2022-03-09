from ..model import SolicitacaoAcessoModel, DisciplinaModel
from ..util.http_status_code import BAD_REQUEST

from .base_controller import BaseController


class SolicitacaoAcessoController(BaseController):
   
    @classmethod
    def get(cls, id):
        return super().get(id, SolicitacaoAcessoModel)

    @classmethod
    def get_id_discente(cls, id_discente):
        return SolicitacaoAcessoModel.find_by_id_discente(id_discente)

    @classmethod
    def post(cls, body):
        return super().post(body, SolicitacaoAcessoModel)

    @classmethod
    def put(cls, body):
        try:
            response = super().put(body, SolicitacaoAcessoModel)
            return response

        except ValueError as msg:
            return {"message":msg}, BAD_REQUEST 

    @classmethod
    def delete(cls, id):
        return super().delete(id, SolicitacaoAcessoModel)

    @classmethod
    def solicitar_para_disciplina_criada(cls, body):
        '''
            Solicitar acesso ao recurso para os discentes, de acordo com a disciplina. 
        
        '''
        id_disciplina = body['id_disciplina']
        body.pop('id_disciplina', None) # remove id_disciplina from dict
        disciplinaModel = DisciplinaModel.find_by_id(id_disciplina)
        
        lista_solicitacao_acesso = list() 

        try:
            for discente in disciplinaModel.discentes:
                body['nome'] = discente.nome
                body['usuario_id_usuario'] = discente.usuario_id_usuario
                body['discente_id_discente'] = discente.id_discente

            
                solicitacaoAcessoModel = SolicitacaoAcessoModel(**body)
                lista_solicitacao_acesso.append(solicitacaoAcessoModel)
        except:
            return {"message":"Há dado(s) inválido(s) no body da requisição."}, BAD_REQUEST    

        SolicitacaoAcessoModel.save_all(lista_solicitacao_acesso) 
        
        return {"message":f"solicitações criada para os discentes da disciplina {disciplinaModel.nome}"}, 201

    @classmethod
    def get_list(cls, campus_instituto_id_campus_instituto=None):
        return super().get_list(SolicitacaoAcessoModel, campus_instituto_id_campus_instituto)

    @classmethod
    def contar_agendamento_por_campus(cls):
        return SolicitacaoAcessoModel.contar_agendamento_por_campus()
    
    @classmethod
    def contar_agendamento_por_recurso_campus(cls, ano, mes, id_campus_instituto):
        return SolicitacaoAcessoModel.contar_agendamento_por_recurso_campus(ano, mes, id_campus_instituto)

    @classmethod
    def contar_agendamento_por_curso(cls, ano, mes, id_campus_instituto):
        return SolicitacaoAcessoModel.contar_agendamento_por_curso(ano, mes, id_campus_instituto)
        