from app import coleta

class RespostaFalsa:
    status_code = 200

    def json(self):
        return {"id": 25, "name": "pikachu"}


def get_falso(url,timeout):
    print("Chamaram o get falso com a URL:", url)


coleta.requests.get = get_falso

resultado = coleta.buscar_pokemon("Pikachu")

print(resultado)