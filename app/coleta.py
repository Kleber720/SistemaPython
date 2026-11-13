import requests

URL_BASE = "https://pokeapi.co/api/v2/pokemon"

class PokemonNaoEncontrado(Exception):
    pass

class ErroDeApi(Exception):
    pass

def buscar_pokemon(nome: str) -> dict:
    try:
        resposta = requests.get(f"{URL_BASE}/{nome.lower()}", timeout=10)

    except requests.RequestException as erro:
        raise ErroDeApi(f"Falha na conexão: {erro}")from erro

    if resposta.status_code == 404:
        raise PokemonNaoEncontrado(nome)

    if resposta.status_code != 200:
        raise ErroDeApi(f"Status inesperado: {resposta.status_code}")

    return resposta.json()

def extrair_dados(payload: dict) -> dict:
    total = sum(item["base_stat"] for item in payload["stats"])

    return {
        "id": payload["id"],
        "nome": payload["name"],
        "tipos": [t["type"]["name"] for t in payload["types"]],
        "total_stats": total,
    }