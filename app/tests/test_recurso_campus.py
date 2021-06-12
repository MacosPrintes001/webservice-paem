
from .base_test import BaseTest
from ..resources import RecursoCampusResource


def run_test_recurso_campus():
    
    #teste route to solicitacao_acesso
    tag = input("\nTesting discente route type enter to continue:")

    URL =BaseTest.get_url(route=RecursoCampusResource.ROUTE)

    payload = {}

    body_post = { 
        'nome': "FOO Recurso",
        'capacidade': 13,
        'descricao':'Foo recruso to test post',
        'inicio_horario_funcionamento':'10:14:00',
        'fim_horario_funcionamento':'12:23:00',
        'campus_id_campus':2
    }

    body_put = { 
        'nome': "BAR Recurso",
        'capacidade': 13,
        'descricao':'Bar recurso to test put',
        'inicio_horario_funcionamento':'11:14:00',
        'fim_horario_funcionamento':'12:23:00',
        'campus_id_campus':2
    }

    id_recurso_campus = BaseTest.post(URL, body_post)
    id_recurso_campus = 15
    BaseTest.put(URL, body_put)

    BaseTest.get(URL, payload)

    BaseTest.delete(URL, {"id_recurso_campus":id_recurso_campus})