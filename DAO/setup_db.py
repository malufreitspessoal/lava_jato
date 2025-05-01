from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DAO.conexao_base import Base
from Models.cliente import Cliente  # Importando Cliente
from Models.veiculo import Veiculo  # Importando Veiculo

# Criando um único banco de dados para todas as tabelas
engine = create_engine('sqlite:///DAO/lava_jato.db', echo=True)

# Criando todas as tabelas
Base.metadata.create_all(engine)

# Criando sessão para interagir com o banco
Session = sessionmaker(bind=engine)
session = Session()

print("Banco de dados configurado com sucesso!")
