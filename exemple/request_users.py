# Request token and then gte request users list

import requests

res = requests.get("http://localhost:5000/api.paem/usuarios")

print("status_code: ",res.status_code)
print("headers: ", res.headers)
print("encoding: ", res.encoding)
print("text: ", res.text)
print("json: ", res.json())