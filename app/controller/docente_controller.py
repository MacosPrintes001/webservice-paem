
from ..model import DocenteModel
from .base_controller import BaseHasOtherIdController
class DocenteController(BaseHasOtherIdController):

    @classmethod
    def get(cls, id):
        return super().get_by_id(id, DocenteModel)

    @classmethod
    def post(cls, body, usuario):
        return super().post(body, DocenteModel, usuario)

    @classmethod
    def put(cls, body):
        return super().put(body, DocenteModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id, DocenteModel)

    @classmethod
    def get_all_names(cls):
        return super().get_all_names(DocenteModel)