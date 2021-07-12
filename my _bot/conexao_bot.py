import re
import requests
import json
from requests.auth import HTTPBasicAuth

token = ' '
rota_base = 'http://localhost:5000/api.paem'

#/ pergar o nome e id do discente atraves cpf
#/ saber de qual campus a pessoa é

def login(cpf):
     global token
     try:
          #conexão para pegar o token (funcionado)
          headers = {"Authentication": f"CPF {cpf}"}
          response = requests.post(url=f"{rota_base}/auth.bot", headers=headers)
          token = json.loads(response.content).get('token')
          if token is not None:
               print("Fiz coenxão com o banco")
               dados = search_dados(token, cpf)
               print(dados)
               
          else:
               print("Não Fiz Conexão")
               return False
     except EOFError:#problema de conexão
          return "erro"

def search_dados(token, cpf):
     try:
          bearer_token = f"Bearer {token}"
          payload = {"Authorization":bearer_token}
          res = requests.get(
          url=f"{rota_base}/usuarios",
          headers=payload
          )

          #print(res.json())

          lista = res.json()
          my_cpf = str(cpf)
          for i in lista:
               if my_cpf in i.values():
                    i['id']
                    res_discente = requests.get(url=f"{rota_base}/discentes", headers=payload)
                    print(res_discente.json())
                    break
                    """
                    MENSAGEM PARA EU DO FUTURO: tentar achar o discente so com os dados que tem em usuario
                    
                    """
                    
                    
               else:
                    print("não achei o nome")
                    return False
     except EOFError:
          print("Deu problema")
     

def search_campus():
     bearer_token = f"Bearer {token}"
     payload = {"Authorization":bearer_token}
     res = requests.get(
     url=f"{rota_base}/campus",
     headers=payload
     )
     
     print(res.json())


"""
def envia_dados():
     pass"""

login(11111111111)