from ..model import UsuarioModel
from .base_controller import BaseController

class UsuarioController(BaseController):

    @classmethod
    def get(cls, id):
        return cls.get_by_id(id, UsuarioModel)

    @classmethod
    def post(cls, body):
        return super().post(body, UsuarioModel)

    @classmethod
    def put(cls, body):
        return super().put(body, UsuarioModel)
    
    @classmethod
    def delete(cls, id):
        return super().delete(id, UsuarioModel)
    
    @classmethod
    def get_list(cls):
        return super().get_list(UsuarioModel)
    
    @classmethod
    def get_by_login(cls, login):
        return UsuarioModel.find_by_login(login)