from .base_controller import BaseController
from ..model import RecursoCampusModel


class RecursoCampusController(BaseController):
    
    @classmethod
    def get(cls, id_recurso_campus):
        return super().get_by_id(id_recurso_campus, RecursoCampusModel)

    @classmethod
    def post(cls, body):
        return super().post(body, RecursoCampusModel)

    @classmethod
    def put(cls, body):
        return super().put(body, RecursoCampusModel)

    @classmethod
    def delete(cls, id_recurso_campus):
        return super().delete(id_recurso_campus, RecursoCampusModel)

    @classmethod
    def get_list(cls):
        return super().get_list(RecursoCampusModel)