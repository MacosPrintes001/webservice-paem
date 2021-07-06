# make login request and get a token to access ather routes with it.
import requests

payload = {"Authentication":"CPF 11111111111"}

BASE_ROUTE = "http://localhost:5000/api.paem"

res = requests.post(
    url=f"{BASE_ROUTE}/auth.bot", 
    headers=payload
)

token = res.json().get("token")
print(token)

bearer_token = f"Bearer {token}"

payload = {"Authorization":bearer_token}
res = requests.get(
    url=f"{BASE_ROUTE}/usuarios",
    headers=payload
)

print(res.json())

