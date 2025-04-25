# conexao_sql.py
import sqlite3 as sql
import os
# from Models.veiculo import Veiculo 

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "carro.db")

def conectar_bd():
    """Cria e retorna uma nova conexão com o banco de dados."""
    try:
        conexao = sql.connect(DATABASE_PATH)
        return conexao
    except sql.Error as e:
        print(f"Erro ao conectar ao banco de dados (em conexao_sql.py): {e}")
        return None

def criar_tabela_se_nao_existe():
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS carro (
                    id_carro INTEGER PRIMARY KEY,
                    placa TEXT NOT NULL,
                    tamanho TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    entrada TEXTE,
                    saida TEXT

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

def adicionar_veiculo_bd(veiculo):
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            cursor.execute('''
                INSERT INTO carro(
                    placa, tamanho, tipo, entrada, saida)
                VALUES(?, ?, ?, ?, ?)
            ''', (veiculo.placa, veiculo.tamanho, veiculo.tipo, veiculo.entrada, veiculo.saida))
            conexao.commit()
            print(f"Veículo com placa '{veiculo.placa}' adicionado com sucesso (em conexao_sql.py).")
    except sql.Error as e:
        print(f"Erro ao adicionar veículo ao banco de dados (em conexao_sql.py): {e}")
        if conexao:
            conexao.rollback()
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def listar_veiculos_bd():
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM carro")
            veiculos = cursor.fetchall()
            return veiculos
    except sql.Error as e:
        print(f"Erro ao listar veículos (em conexao_sql.py): {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def confirmar_veiculo(placa):
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT placa from carro WHERE placa=?", (placa,))
            resultado = cursor.fetchone()  # Busca a primeira linha do resultado
            if resultado:
                return True  # A placa existe no banco de dados
            else:
                return False # A placa não foi encontrada
        else:
            return False
    except sql.Error as e:
        print(f"Erro ao confirmar veículo (em conexao_lava_jato.py): {e}")
        return False # Em caso de erro, retorna False por segurança
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def remover_veiculo_bd_por_placa(placa, saida):
    conexao = conectar_bd()
    cursor = None
    try:
        if conexao:
            cursor = conexao.cursor()
            if confirmar_veiculo(placa):
                cursor.execute("UPDATE carro SET saida=? WHERE placa=?", (saida, placa))
                conexao.commit()
                if cursor.rowcount > 0:
                    return True
            else:
                return False
    except sql.Error as e:
        print(f"Erro ao dar checkout no veículo (em conexao_sql.py): {e}")
        if conexao:
            conexao.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
            