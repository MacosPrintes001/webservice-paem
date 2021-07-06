from .base_controller import BaseHasNameController
from ..model import CampusModel

class CampusController(BaseHasNameController):
    
    @classmethod
    def get(cls, id):
        return super().get(id, CampusModel)

    @classmethod
    def post(cls, body):
        return super().post(body, CampusModel)

    @classmethod
    def put(cls, body):
        return super().put(body, CampusModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id, CampusModel)

    @classmethod
    def get_all_names(cls):
        return super().get_all_names(CampusModel)