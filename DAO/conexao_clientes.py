import sqlite3 as sql
import os
from Models.veiculo import Veiculo  # Pode ser usado nas funções

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "clientes.db")

def conectar_bd():
    """Cria e retorna uma nova conexão com o banco de dados."""
    try:
        conexao = sql.connect(DATABASE_PATH)
        return conexao
    except sql.Error as e:
        print(f"Erro ao conectar ao banco de dados (em conexao_clientes.py): {e}")
        return None

def criar_tabela_se_nao_existe():
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    cpf TEXT NOT NULL,
                    telefone TEXT,
                    mes_nascimento TEXT
                );
            ''')
            conexao.commit()
    except sql.Error as e:
        print(f'Erro ao criar/verificar tabela (em conexao_sql.py): {e}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()