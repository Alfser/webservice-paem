
from app.model import campus_instituto
from ..controller import CampusInstitutoController
from ..util.authorization import Authorization
from .base_resource import BaseResource
from ..serializer import CampusInstitutoSerializer, DirecaoSerializer

from flask_restful import Resource

from flask_apispec import marshal_with, use_kwargs, doc

@doc(description='Obter, atualizar e deletar Campus ou Instituto da UFOPA', tags=['Campus ou Instituto UFOPA'])
class CampusInstitutoResource(BaseResource, Resource):
    ENDPOINT = 'campus_instituto-detail'
    ROUTE = '/campus_instituto/<int:id_campus_instituto>'
    scheme = CampusInstitutoSerializer

    @marshal_with(CampusInstitutoSerializer, description='Retorna os dados do campus ou instituto.')
    @Authorization.token_required()
    def get(self, id_campus_instituto):
        return CampusInstitutoController.get(id_campus_instituto)

    @use_kwargs(CampusInstitutoSerializer(exclude=('id_campus_instituto',)))
    @marshal_with(CampusInstitutoSerializer, description='Retorna os dados do campus ou instituto atualizado.')
    @Authorization.token_required()
    def put(self, id_campus_instituto, **kwargs):
        return CampusInstitutoController.put(id=id_campus_instituto, body=kwargs)

    @marshal_with(None, description='Retorna a mensagem de deletado quando quando a operação foi executada com sucesso.')
    @Authorization.token_required()
    def delete(self, id_campus_instituto):
        return CampusInstitutoController.delete(id_campus_instituto)

@doc(description='Listar ou criar Campus ou Instituto da UFOPA', tags=['Campus ou Instituto UFOPA'])
class ListaCampusInstitutoResource(BaseResource, Resource):

    ENDPOINT = 'campus_instituto-list'
    ROUTE = '/campus_instituto'
    scheme = CampusInstitutoSerializer

    @marshal_with(CampusInstitutoSerializer(many=True), description='Lista dos campus e institutos.')
    @Authorization.token_required()
    def get(self):
        return CampusInstitutoController.get_all_names()

    @use_kwargs(CampusInstitutoSerializer(exclude=('id_campus_instituto',)), )
    @marshal_with(CampusInstitutoSerializer, description='Caso e respota de OK, retorna o campus ou instituto criado.')
    @Authorization.token_required()
    def post(self, **kwargs):
        return CampusInstitutoController.post(body=kwargs)