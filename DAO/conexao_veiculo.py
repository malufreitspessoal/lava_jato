from sqlalchemy.exc import SQLAlchemyError
from Models.cliente import Cliente
from Models.presenca import Presenca
from Models.veiculo import Veiculo
from DAO.setup_db import Session

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
    # Obtém todos os veículos
    veiculos = session.query(Veiculo.placa, Veiculo.tamanho, Veiculo.tipo, Veiculo.id_cliente).all()
    
    # Obtém todos os clientes e cria um dicionário para mapear id_cliente -> nome
    clientes_dict = {id_cliente: nome for id_cliente, nome in session.query(Cliente.id_cliente, Cliente.nome).all()}
    
    # Substitui o ID do cliente pelo nome correspondente
    todos_veiculos_identificados = [
        (veiculo[0], veiculo[1], veiculo[2], clientes_dict.get(veiculo[3], "Cliente não encontrado"))
        for veiculo in veiculos
    ]
    
    return todos_veiculos_identificados


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
