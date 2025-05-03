from sqlalchemy.exc import SQLAlchemyError
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
    veiculos = session.query(Veiculo.placa, Veiculo.id_cliente).all()
    return veiculos


    


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
    pass
    # try:
    #     # Verificar se o veículo existe
    #     if confirmar_veiculo(placa):
    #         # Atualizar a coluna saida do veículo com a placa fornecida
    #         veiculo = session.query(Veiculo).filter_by(placa=placa).first()
    #         veiculo.saida = saida
    #         session.commit()
    #         return True
    #     else:
    #         return False
    # except SQLAlchemyError as e:
    #     print(f"Erro ao dar checkout no veículo (em conexao_sql.py): {e}")
    #     session.rollback()
    #     return False
