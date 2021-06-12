
from .base_test import BaseTest
from ..resources import SolicitacaoAcessoResource


def run_test_solicitacao_acesso():

    #teste route to solicitacao_acesso
    tag = input("\nTesting SOLICITACEO_ACESSO route type enter to continue:")

    URL = BaseTest.get_url(route=SolicitacaoAcessoResource.ROUTE)

    payload = {}

    body_post = { 
        'id_solicitacao_acesso':4,
        'para_si':0,
        'data':'23-04-2021',
        'hora_inicio':'17:30:34',
        'hora_fim':'18:00:00',
        'status_acesso':'1',
        'nome':'Caros',
        'fone':'(91)983878675',
        'usuario_id_usuario':5,
        'discente_id_discente':2,
        'recurso_campus_id_recurso_campus':6
    }


    body_put = { 
        'id_solicitacao_acesso':4,
        'para_si':0,
        'data':'01-10-2018',
        'hora_inicio':'17:30:34',
        'hora_fim':'18:00:00',
        'status_acesso':'1',
        'nome':'Caros',
        'fone':'(91)983878675',
        'usuario_id_usuario':5,
        'discente_id_discente':2,
        'recurso_campus_id_recurso_campus':6
    }

    payload["id_solicitacao_acesso"] = BaseTest.post(URL, body_post)
    BaseTest.put(URL, body_put)

    print('payload: ', payload)
    BaseTest.get(URL, payload)

    BaseTest.delete(URL, payload)