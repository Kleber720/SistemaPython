import requests

resposta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu", timeout=10)
print(resposta.status_code)

dados = resposta.json()

print(type(dados))
print(dados["name"])
print(dados["stats"][0])