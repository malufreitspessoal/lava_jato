import sqlite3 as sql
import os
# from Models.veiculo import Veiculo  # Pode ser usado nas funções

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "cliente.db")

def conectar_bd():
    """Cria e retorna uma nova conexão com o banco de dados."""
    try:
        conexao = sql.connect(DATABASE_PATH)
        return conexao
    except sql.Error as e:
        print(f"Erro ao conectar ao banco de dados (em conexao_cliente.py): {e}")
        return None

def criar_tabela_cliente_se_nao_existe():
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            # cursor.execute("PRAGMA foreign_keys = ON;")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id_cliente INTEGER PRIMARY KEY,
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

def adicionar_cliente_bd(cliente):
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO cliente(
                    nome, email, cpf, telefone, mes_nascimento)
                VALUES(?, ?, ?, ?, ?)
            ''', (cliente.nome, cliente.email, cliente.cpf, cliente.telefone, cliente.mes_nascimento))
            conexao.commit()
            print(f"Cliente '{cliente.nome}' adicionado com sucesso (em conexao_cliente.py).")
            return True
    except sql.Error as e:
        print(f"Erro ao adicionar cliente ao banco de dados (em conexao_cliente.py): {e}")
        if conexao:
            conexao.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def excluir_cliente_bd():
    pass

def editar_cliente_bd():
    pass

def listar_clientes():
    pass