# request a discente in data base by matricula param.
import requests

# change TOKEN to valide token
token="TOKEN"
headers = {"Authorization":f"Bearer {token}"}
payload = {"matricula":"2019013473"}

#teste route to solicitacao_acesso
tag = input("\nTesting discente route type enter to continue:")

URL_BASE = "http://localhost:5000/api.paem{route}"
URL_DISCENTE = URL_BASE.format(route="/discentes/discente")
URL_DISCENTES = URL_BASE.format(route="/discentes")

post = input("\ntesting POST request. Type enter or any key to do not. ")

if not post:

    dict_discente = { 
        "matricula": "11111111111",
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

    resp_post = requests.post(
        url=URL_DISCENTE, 
        json=dict_discente,
        headers=headers
    )

    print(resp_post.url)
    print("status_code: ",resp_post.status_code)
    print("headers: ", resp_post.headers)
    print("json: ", resp_post.json())

put = input("\ntesting PUT request. Type enter or any key to do not. ")
if not put:

    dict_discente = { 
        "matricula": "11111111111",
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

    resp_post = requests.put(
        url=URL_DISCENTE, 
        json=dict_discente,
        headers=headers
    )

    print(resp_post.url)
    print("status_code: ",resp_post.status_code)
    print("headers: ", resp_post.headers)
    print("json: ", resp_post.json())


get = input('\ntesting GET request. type Type enter or any key to do not. ')

payload = {'matricula': '11111111111'}

if not get:
    

    resp_get = requests.get(
        URL_DISCENTE,
        params=payload,
        headers=headers
    )

    print(resp_get.url)
    print("status_code: ",resp_get.status_code)
    print("headers: ", resp_get.headers)
    print("text: ", resp_get.json())

delete = input('\ntesting DELETE request. Type enter or any key to do not. ')

if not delete:
    
    resp_del = requests.delete(
        URL_DISCENTE, 
        params=payload,
        headers=headers
    )

    print(resp_del.request)
    print("status_code: ",resp_del.status_code)
    print("headers: ", resp_del.headers)
    print("text: ", resp_del.text)
