
from .base_test import BaseTest
from ..resources import AcessoPermitidoResource

def run_test_acesso_permitido():
    #teste route to acesso_permitido
    tag = input("\nTesting ACESSO_PERMITIDO route type enter to continue:")

    URL = BaseTest.get_url(route=AcessoPermitidoResource.ROUTE)

    payload = {}

    body_post = { 
        'id_acesso_permitido':4, 
        'temperatura':33.6,
        'hora_entrada':'10:30:38',
        'hora_saida':'11:20:00',
        'solicitacao_acesso_id_solicitacao_acesso':3
    }

    body_put = { 
        'id_acesso_permitido':4, 
        'temperatura':36.6,
        'hora_entrada':'11:30:38',
        'hora_saida':'12:20:00',
        'solicitacao_acesso_id_solicitacao_acesso':3
    }

    payload["id_acesso_permitido"] = BaseTest.post(URL, body_post)

    BaseTest.put(URL, body_put)

    BaseTest.get(URL, payload)

    BaseTest.delete(URL, payload)