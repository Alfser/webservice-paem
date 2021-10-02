from ..controller import CampusInstitutoController
from ..util.authorization import Authorization

from flask_restful import reqparse, request, Resource


class CampusInstitutoResource(Resource):
    ENDPOINT = 'campus_instituto'
    ROUTE = '/campus_institutos/campus_instituto'

    @Authorization.token_required()
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_campus_instituto', type=str, required=True, help="You need to send query string id_campus.")

        args = parser.parse_args(strict=True)
        id_campus_instituto = args.get('id_campus_instituto')
        
        return CampusInstitutoController.get(id_campus_instituto)

    @Authorization.token_required()
    def post(self):
        body = request.json
        return CampusInstitutoController.post(body)
      
    @Authorization.token_required()
    def put(self):
        body = request.json
        return CampusInstitutoController.put(body)

    @Authorization.token_required()
    def delete(self):

        parser = reqparse.RequestParser()
        parser.add_argument('id_campus_instituto', type=str, required=True, help="You need to send query string id_campus.")

        args = parser.parse_args(strict=True)
        id_campus_instituto = args.get('id_campus_instituto')

        return CampusInstitutoController.delete(id_campus_instituto)

class ListaCampusInstitutoResource(Resource):
    
    ENDPOINT = 'campus_institutos'
    ROUTE = '/campus_institutos'
    
    @Authorization.token_required()
    def get(self):
        return CampusInstitutoController.get_all_names()
