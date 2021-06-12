
from .base_test import BaseTest
from ..resources import DiscenteResource


def run_test_discente():
    
    #teste route to solicitacao_acesso
    tag = input("\nTesting discente route type enter to continue:")

    URL =BaseTest.get_url(route=DiscenteResource.ROUTE)

    payload = {"matricula":"123456789"}

    body_post = { 
        "matricula": payload["matricula"],
        "nome": "Test Discente 1",
        "curso_id_curso":2,
        "cpf":"22222222222",
        "entrada":"2021",
        "semestre":1,
        "endereco":"endereço teste",
        "grupo_risco":0,
        "status_covid":0,
        "status_permissao":1,
        "usuario_id_usuario":5
    }

    body_put = { 
        "matricula": payload["matricula"],
        "nome": "Test Discente 2",
        "curso_id_curso":3,
        "cpf":"22222222222",
        "entrada":"2021",
        "semestre":1,
        "endereco":"endereço teste Updated",
        "grupo_risco":0,
        "status_covid":0,
        "status_permissao":1,
        "usuario_id_usuario":5
    }

    id_discente = BaseTest.post(URL, body_post)

    BaseTest.put(URL, body_put)

    BaseTest.get(URL, payload)

    BaseTest.delete(URL, {"id_discente":id_discente})