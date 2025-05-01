# conexao_sql.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from DAO.setup_db import Session


engine = create_engine('sqlite:///DAO/controle_checkin_checkout.db', echo=True)  # echo=True mostra os comandos SQL

# Cria uma base para os modelos
Base = declarative_base()

# Cria as tabelas no banco
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
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
