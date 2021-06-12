# make login request and get a token to access ather routes with it.
import requests
from requests.auth import HTTPBasicAuth

res = requests.get(
    url="http://localhost:5000/appi.paem/auth", 
    auth=HTTPBasicAuth("username", "password")
)

print(res.json().get("token"))
