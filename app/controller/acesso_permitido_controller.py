from ..model import AcessoPermitidoModel
from .base_controller import BaseController

class AcessoPermitidoController(BaseController):
    
    @classmethod
    def get(cls, id):
        return super().get_by_id(id, AcessoPermitidoModel)

    @classmethod
    def post(cls, body):
        return super().post(body, AcessoPermitidoModel)

    @classmethod
    def put(cls, body):
        return super().put(body, AcessoPermitidoModel)

    @classmethod
    def delete(cls, id):
        return super().delete(id,AcessoPermitidoModel)
    
    @classmethod
    def get_list(cls):
        return super().get_list(AcessoPermitidoModel)