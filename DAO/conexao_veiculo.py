from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from Models import veiculo
from Models.presenca import Presenca
from Models.veiculo import Veiculo
from DAO.setup_db import Session

# engine = create_engine('sqlite:///DAO/veiculo.db', echo=True)  # echo=True mostra os comandos SQL

# # Cria as tabelas no banco
# Base.metadata.create_all(engine)

# # Cria uma sessão para interagir com o banco
# Session = sessionmaker(bind=engine)
session = Session()

def adicionar_veiculo_bd(veiculo:Veiculo, presensa:Presenca):
    try:
        # Verificar se o veículo já está no banco
        veiculo_localizado = session.query(Veiculo).filter_by(placa=veiculo.placa).first()

        if veiculo_localizado:
            # Se o veículo já existe, apenas registrar o check-in
            novo_checkin = Presenca(presensa.check_in, veiculo_localizado.id_veiculo)
            session.add(novo_checkin)
            session.commit()
            print(f"✅ Check-in realizado para {veiculo.placa} às {presensa.check_in}.")
        else:
            session.add(veiculo)
            session.commit()  # Commit para garantir que o ID seja gerado
            # Agora adicionamos o check-in
            novo_checkin = Presenca(id_veiculo=veiculo.id_veiculo, check_in=presensa.check_in)
            session.add(novo_checkin)
            session.commit()
            print(f"✅ Veículo {veiculo.placa} cadastrado e check-in realizado às {presensa.check_in}.")
        
        return True
    except SQLAlchemyError as e:
        print(f"❌ Erro ao adicionar veículo/check-in: {e}")
        session.rollback()
        return False

    
# Função para listar todos os veículos
def listar_veiculos_bd():
    consulta = (
    session.query(Veiculo.placa, Veiculo.tamanho, Veiculo.tipo, Presenca.check_in, Presenca.check_out)
    .join(Presenca, Veiculo.id_veiculo == Presenca.id_veiculo)
    .all()
)

 
    return consulta


    


    # try:
    #     # Consultar todos os registros da tabela carro
    #     veiculos = session.query(Veiculo).all()
    #     # Retornar uma lista de dicionários para manter compatibilidade com fetchall
    #     return veiculos
    # except SQLAlchemyError as e:
    #     print(f"Erro ao listar veículos (em conexao_sql.py): {e}")
    #     return []

# Função para confirmar se um veículo existe pela placa
def confirmar_veiculo(placa):
    try:
        # Verificar se existe um carro com a placa fornecida
        resultado = session.query(Veiculo).filter_by(placa=placa).first()
        return resultado is not None  # Retorna True se o carro existe, False caso contrário
    except SQLAlchemyError as e:
        print(f"Erro ao confirmar veículo (em conexao_lava_jato.py): {e}")
        return False

# Função para atualizar a data de saída de um veículo pela placa
def remover_veiculo_bd_por_placa(placa, saida):
    try:
        # Verificar se o veículo existe
        if confirmar_veiculo(placa):
            # Atualizar a coluna saida do veículo com a placa fornecida
            veiculo = session.query(Veiculo).filter_by(placa=placa).first()
            veiculo.saida = saida
            session.commit()
            return True
        else:
            return False
    except SQLAlchemyError as e:
        print(f"Erro ao dar checkout no veículo (em conexao_sql.py): {e}")
        session.rollback()
        return False

# def listar_veiculos_bd():
#     conexao = conectar_bd()
#     cursor = None
#     try:
#         if conexao:
#             cursor = conexao.cursor()
#             cursor.execute("SELECT * FROM carro")
#             veiculos = cursor.fetchall()
#             return veiculos
#     except sql.Error as e:
#         print(f"Erro ao listar veículos (em conexao_sql.py): {e}")
#         return []
#     finally:
#         if cursor:
#             cursor.close()
#         if conexao:
#             conexao.close()


# def confirmar_veiculo(placa):
#     conexao = conectar_bd()
#     cursor = None
#     try:
#         if conexao:
#             cursor = conexao.cursor()
#             cursor.execute("SELECT placa from carro WHERE placa=?", (placa,))
#             resultado = cursor.fetchone()  # Busca a primeira linha do resultado
#             if resultado:
#                 return True  # A placa existe no banco de dados
#             else:
#                 return False # A placa não foi encontrada
#         else:
#             return False
#     except sql.Error as e:
#         print(f"Erro ao confirmar veículo (em conexao_lava_jato.py): {e}")
#         return False # Em caso de erro, retorna False por segurança
#     finally:
#         if cursor:
#             cursor.close()
#         if conexao:
#             conexao.close()

# def remover_veiculo_bd_por_placa(placa, saida):
#     conexao = conectar_bd()
#     cursor = None
#     try:
#         if conexao:
#             cursor = conexao.cursor()
#             if confirmar_veiculo(placa):
#                 cursor.execute("UPDATE carro SET saida=? WHERE placa=?", (saida, placa))
#                 conexao.commit()
#                 if cursor.rowcount > 0:
#                     return True
#             else:
#                 return False
#     except sql.Error as e:
#         print(f"Erro ao dar checkout no veículo (em conexao_sql.py): {e}")
#         if conexao:
#             conexao.rollback()
#         return False
#     finally:
#         if cursor:
#             cursor.close()
#         if conexao:
#             conexao.close()
            