from ..model import TecnicoModel
from .base_controller import BaseHasNameController, BaseHasUsuarioController

class TecnicoController(BaseHasUsuarioController):
    
    @classmethod
    def get(cls, id_tecnico):
        return super().get_by_id(id_tecnico, TecnicoModel)

    @classmethod
    def post(cls, body, usuario):
        TecnicoModel.usuario = usuario
        return super().post(body, TecnicoModel, usuario=usuario)

    @classmethod
    def put(cls, body):
        return super().put(body, TecnicoModel)

    @classmethod
    def delete(cls, id_tecnico):
        return super().delete(id_tecnico, TecnicoModel)

    @classmethod
    def get_all_names(cls):
        return super().get_all_names(TecnicoModel)