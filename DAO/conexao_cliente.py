from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from Models.cliente import Cliente
from DAO.setup_db import Session

session = Session()

def adicionar_cliente_bd(cliente):
    try:
        # Adicionar à sessão
        session.add(cliente)
        # Confirmar a transação
        session.commit()
        print(f"Cliente '{cliente.nome}' adicionado com sucesso (em conexao_cliente.py).")
        return True
    except SQLAlchemyError as e:
        print(f"Erro ao adicionar cliente ao banco de dados (em conexao_cliente.py): {e}")
        session.rollback()
        return False


def excluir_cliente_bd(cpf):
    try:
        cliente_removido = session.query(Cliente).filter(Cliente.cpf == cpf).first() # Retorna o primeiro cliente que corresponde ao filtro
       
        if cliente_removido:
            session.delete(cliente_removido)
        # Confirmar a transação
            session.commit()
            print(f"Cliente com CPF {cpf} removido com sucesso (em conexao_cliente.py).")
            return True
        else:
            print(f"Nenhum cliente encontrado com o CPF: {cpf} (em conexao_cliente.py).")
            return False
    
    except SQLAlchemyError as e:
        print(f"Erro ao adicionar cliente ao banco de dados (em conexao_cliente.py): {e}")
        session.rollback()
        return False

def editar_cliente_bd(cpf, cliente_editado:Cliente):
    try:
        cliente = session.query(Cliente).filter(Cliente.cpf == cpf).first()
        
        if cliente:
            cliente.nome = cliente_editado.nome
            cliente.email = cliente_editado.email
            cliente.cpf = cliente_editado.cpf
            cliente.telefone = cliente_editado.telefone
            cliente.mes_nascimento = cliente_editado.mes_nascimento
            session.commit()
            print(f"Cliente com CPF {cpf} atualizado com sucesso (em conexao_cliente.py).")
            return True
        else:
            print(f"Nenhum cliente encontrado com o CPF: {cpf} (em conexao_cliente.py).")
            return False
    
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar cliente (em conexao_cliente.py): {e}")
        session.rollback()
        return False

def listar_clientes_bd(): 
    '''
    retorna uma lista de objetos da classe Cliente
    '''
    clientes = session.query(Cliente).all()

    return clientes

def mostrar_cpf_filtrado(cpf):
    lista_filtrada_por_cpf = session.query(Cliente).filter(Cliente.cpf.like(f'%{cpf}%')).all()   
    
    if lista_filtrada_por_cpf:
        return lista_filtrada_por_cpf
    return False

