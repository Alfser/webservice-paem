from email.policy import default

from app.model import campus_instituto
from ..controller import CampusInstitutoController
from ..util.authorization import Authorization

from flask_restful import reqparse, request, Resource

from flask_apispec import marshal_with, use_kwargs, doc
from flask_apispec.views import MethodResource

from marshmallow import Schema, fields

# serialization
class CampusInstitutoSerializer(Schema):
    
    id_campus_instituto = fields.Int()
    nome = fields.Str(default='anonymous')
    abertura_total = fields.Int()
    ano_fundacao = fields.Date()
    direcao_id_direcao = fields.Int(allow_none=True)
    direcao = fields.Dict(keys=fields.Str(), allow_none=True) 


class CampusInstitutoResource(MethodResource, Resource):
    ENDPOINT = 'campus_instituto'
    ROUTE = '/campus_instituto/<int:id_campus_instituto>'

    @doc(description='Obter Campus ou Instituto da UFOPA', tags=['Campus ou Instituto'])
    @marshal_with(CampusInstitutoSerializer)
    @Authorization.token_required()
    def get(self, id_campus_instituto):
        
        return CampusInstitutoController.get(id_campus_instituto)

    # @Authorization.token_required()
    # def post(self):
    #     body = request.json
    #     return CampusInstitutoController.post(body)
      
    # @Authorization.token_required()
    # def put(self):
    #     body = request.json
    #     return CampusInstitutoController.put(body)

    # @Authorization.token_required()
    # def delete(self):

    #     parser = reqparse.RequestParser()
    #     parser.add_argument('id_campus_instituto', type=str, required=True, help="You need to send query string id_campus.")

    #     args = parser.parse_args(strict=True)
    #     id_campus_instituto = args.get('id_campus_instituto')

    #     return CampusInstitutoController.delete(id_campus_instituto)

class ListaCampusInstitutoResource(Resource):
    
    ENDPOINT = 'campus_institutos'
    ROUTE = '/campus_institutos'
    
    @Authorization.token_required()
    def get(self):
        return CampusInstitutoController.get_all_names()
