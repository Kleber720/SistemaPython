import os

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "pokedex"),
    )

def criar_tabelas(conexao):
    cursor = conexao.cursor() # cursor é utilizado para executar comandos no SQL
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon (
          id INT PRIMARY KEY,
          nome VARCHAR(50) NOT NULL,
          total INT NOT NULL,
          classificacao VARCHAR(20) NOT NULL
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tipo_pokemon (
          pokemon_id INT NOT NULL,
          tipo VARCHAR(30) NOT NULL,
          PRIMARY KEY (pokemon_id, tipo),
          FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
        )
        """
    )
    conexao.commit()
    cursor.close()

def salvar_pokemon(conexao, id_pokemon, nome, total, classificacao, tipos):
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO pokemon (id, nome, total, classificacao)
            VALUES (%s, %s, %s, %s) ON DUPLICATE KEY
            UPDATE
                nome = %s,
                total = %s,
                classificacao = %s
            """,
            (id_pokemon, nome, total, classificacao, nome, total, classificacao),
        )
        for tipo in tipos:
            cursor.execute(
                "INSERT IGNORE INTO tipo_pokemon (pokemon_id, tipo) VALUES (%s, %s)",
                (id_pokemon, tipo),
            )
            conexao.commit()
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()


def ranking_por_tipo(conexao):
    cursor = conexao.cursor()
    cursor.execute(
        """
        SELECT t.tipo, AVG(p.total) AS media_total, COUNT(*) AS quantidade
        FROM pokemon p 
        JOIN tipo_pokemon t ON t.pokemon_id = p.id
        GROUP BY t.tipo
        ORDER BY media_total DESC
        """
    )
    linhas = cursor.fetchall()
    cursor.close()
    return linhas

