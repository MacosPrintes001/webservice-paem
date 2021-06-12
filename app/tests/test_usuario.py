from .base_test import BaseTest
from ..resources import UsuarioResource
#teste route to usuario


def run_test_usuario():
    
    tag = input("\nTesting USUARIO route type enter to continue:")


    URL = BaseTest.get_url(UsuarioResource.ROUTE)

    # add query strings
    payload = {}

    body_post = { 
            "login": "foo3",
            "email": "foo3@test.com",
            "senha":"foo3",
            "tipo":2,
        }

    body_put ={ 
        "login": "bar",
        "email": "bar@test.com",
        "senha":"bar",
        "tipo":2,
    }


    payload['id_usuario'] = BaseTest.post(URL, body_post)
    body_put['id_usuario'] = payload['id_usuario']
    
    BaseTest.put(URL, body_put)

    BaseTest.get(URL, payload)

    BaseTest.delete(URL, payload)