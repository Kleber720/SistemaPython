import pytest
import requests

from app.coleta import(
ErroDeApi,
PokemonNaoEncontrado,
buscar_pokemon,
extrair_dados,
)

PAYLOAD_FAKE = {
    "id": 25,
    "name": "pikachu",
    "types": [{"type": {"name": "eletric"}}],
    "stats": [
        {"base_stat": 35}, {"base_stat": 55},{"base_stat": 40},
        {"base_stat": 50}, {"base_stat": 50}, {"base_stat": 90}
    ],
}

def test_extrair_dados():
    dados = extrair_dados(PAYLOAD_FAKE)
    assert dados == {
        "id": 25,
        "nome": "pikachu",
        "tipos": [{"type": {"name": "eletric"}}],
        "total_stats": 320,
    }

def test_buscar_pokemon_sucesso(mocker):
        resposta = mocker.Mock(status_code=200)
        resposta.json.return_value = PAYLOAD_FAKE
        mocker.patch("app.coleta.requests.get", return_value=resposta)

        assert buscar_pokemon("Pikachu")["name"] == "pikachu"

def test_buscar_pokemon_nao_encontrado(mocker):
    mocker.patch("app.coleta.requests.get", return_value = mocker.Mock(status_code=404))

    with pytest.raises(PokemonNaoEncontrado):
        buscar_pokemon("digimon")


def test_buscar_pokemon_erro_de_conexao(mocker):
    mocker.patch(
        "app.coleta.requests.get",
        side_effect=requests.ConnectionError("sem rede"),
    )
    with pytest.raises(ErroDeApi):
        buscar_pokemon("pikachu")