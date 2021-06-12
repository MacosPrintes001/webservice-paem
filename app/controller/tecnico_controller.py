from ..model import TecnicoModel
from .base_controller import BaseController

class TecnicoController(BaseController):
    
    @classmethod
    def get(cls, id_tecnico):
        return super().get_by_id(id_tecnico, TecnicoModel)

    @classmethod
    def post(cls, body):
        return super().post(body, TecnicoModel)

    @classmethod
    def put(cls, body):
        return super().put(body, TecnicoModel)

    @classmethod
    def delete(cls, id_tecnico):
        return super().delete(id_tecnico, TecnicoModel)

    @classmethod
    def get_list(cls):
        return super().get_list(TecnicoModel)