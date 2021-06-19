from .base_controller import BaseHasNameController, BaseHasUsuarioController
from ..model import DiscenteModel
from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class DiscenteController(BaseHasUsuarioController):
    
    @classmethod
    def get_by_matricula(cls, matricula):

        discente = DiscenteModel.find_by_matricula(matricula)
        if not discente:
            return {"message":"Not found this discente."}, NOT_FOUND_REQUEST
      
        return discente.serialize(), OK

    @classmethod
    def get(cls, id):
        return super().get_by_id(id, DiscenteModel)

    @classmethod
    def post(cls, body, usuario):
        return super().post(body, DiscenteModel, usuario=usuario)

    @classmethod
    def put(cls, body):
        return super().put(body, DiscenteModel)

    @classmethod
    def delete(cls, id_discente):
        return super().delete(id_discente, DiscenteModel)

    @classmethod
    def get_all_names(cls):
        return super().get_all_names(DiscenteModel)