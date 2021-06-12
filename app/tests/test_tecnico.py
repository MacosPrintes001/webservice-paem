
from .base_test import BaseTest
from ..resources import TecnicoResource


def run_test_tecnico():
    
    #teste route to solicitacao_acesso
    tag = input("\nTesting TECNICO route type enter to continue:")

    URL = BaseTest.get_url(route=TecnicoResource.ROUTE)

    payload = {}

    body_post = { 
        'siape':"12443", 
        'nome':"foo tecnico", 
        'data_nascimento':'12-12-2000', 
        "cargo":"Algum cargo",
        'status_covid':0, 
        'status_afastamento':0, 
        'usuario_id_usuario':2, 
        'campus_id_campus':1
    }

    body_put = { 
        'siape':"12443", 
        'nome':"bar tecnico", 
        'data_nascimento':'12-12-2000', 
        "cargo":"Algum cargo atualizado",
        'status_covid':1, 
        'status_afastamento':0, 
        'usuario_id_usuario':2, 
        'campus_id_campus':1
    }


    id = BaseTest.post(URL, body_post)

    payload["id_tecnico"] = 19

    BaseTest.put(URL, body_put)

    BaseTest.get(URL, payload)

    BaseTest.delete(URL, payload)