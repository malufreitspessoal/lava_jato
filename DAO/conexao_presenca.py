from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from Models.presenca import Presenca
from DAO.setup_db import Session
from Models.veiculo import Veiculo

session = Session()


def fazer_check_in_bd(placa, hora_entrada):
    try:
        if  confirmar_veiculo_check_in(placa):
            print(f"Veículo com placa {placa} tem check-in ativo ou não existe.")
            return False
            # Se o veículo já existe, apenas registrar o check-in
        
        veiculo_localizado = session.query(Veiculo).filter_by(placa=placa).first()
        if veiculo_localizado:
            novo_checkin = Presenca(hora_entrada, veiculo_localizado.id_veiculo)
            session.add(novo_checkin)
            session.commit()
            print(f"✅ Check-in realizado para {veiculo_localizado.placa} às {hora_entrada}.")
            return True
        return False
    
    except SQLAlchemyError as e:
        print(f"Erro ao dar check in no veículo (em conexao_sql.py): {e}")
        session.rollback()
        return False

def fazer_check_out_bd(placa, saida):
    try:
        # RETORNA O OBJETO JÁ CONFIRMADO NO BANCO 
        veiculo_localizado = confirmar_veiculo_check_in(placa) # tenho o objeto da PRESENÇA
        
        if not veiculo_localizado:
            print(f"Veículo com placa {placa} não tem check-in ativo ou não existe.")
            return False
            # Atualizar a coluna saida do veículo com a placa fornecida
        veiculo_localizado.check_out = saida
        session.commit()
        print(f"✅ Check-out realizado para {placa} às {saida}.")
        return True

    except SQLAlchemyError as e:
        print(f"Erro ao dar checkout no veículo (em conexao_sql.py): {e}")
        session.rollback()
        return False
    
def confirmar_veiculo_check_in(placa):
    '''
    Quero confirmar se o veiculo está constando no check-in 
    Só que tenho que filtrar por veiculo na tabela checkin_check_out
    '''
    try:
        # Verificar se existe um carro com a placa fornecida
        veiculo = session.query(Veiculo).filter_by(placa=placa).first()
        if not veiculo:
                print(f"Veículo com placa {placa} não encontrado na tabela Veiculo.")
                return None
        resultado = session.query(Presenca).filter_by(id_veiculo = veiculo.id_veiculo, check_out=None).first()
        
        return resultado  
    
    except SQLAlchemyError as e:
        print(f"Erro ao confirmar veículo (em conexao_lava_jato.py): {e}")
        return False
    
def listar_veiculos_check_in_bd():
    consulta = (
    session.query(Veiculo.placa, Veiculo.tamanho, Veiculo.tipo, Presenca.check_in, Presenca.check_out)
    .join(Presenca, Veiculo.id_veiculo == Presenca.id_veiculo)
    .all()
)

 
    return consulta

