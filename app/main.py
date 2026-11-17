import sys

from app.classificacao import classificar_poder
from app.coleta import ErroDeApi, PokemonNaoEncontrado, buscar_pokemon, extrair_dados

def main(nome: str) -> int:
    try:
        dados = extrair_dados(buscar_pokemon(nome))
    except PokemonNaoEncontrado:
        print(f"Pokémon '{nome}' não encontrado")
        return 1
    except ErroDeApi as erro:
        print(f"Erro ao consultar a API: {erro}")
        return 2

    categoria = classificar_poder(dados["total_stats"])
    tipos = ",".join(dados["tipos"])
    print(f"{dados["nome"]} | tipos: {tipos} | total: {dados['total_stats']} |  {categoria}")
    return 0 # servidores leiem como numeros a saida


if __name__ == "__main__":
    nome=sys.argv[1] if len(sys.argv) > 1 else "pikachu"
    sys.exit(main(nome))