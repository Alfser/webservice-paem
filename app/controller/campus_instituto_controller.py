from .base_controller import BaseHasNameController
from ..model import CampusInstitutoModel

class CampusInstitutoController(BaseHasNameController):
    
    @classmethod
    def get(cls, id):
        return super().get(id, CampusInstitutoModel)

    @classmethod
    def post(cls, body):
        return super().post(body, CampusInstitutoModel)

    @classmethod
    def put(cls, body):
        return super().put(body, CampusInstitutoModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id, CampusInstitutoModel)

    @classmethod
    def get_all_names(cls):
        return super().get_all_names(CampusInstitutoModel)