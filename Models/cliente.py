from sqlalchemy import Column, Integer, String
from DAO.conexao_base import Base
from sqlalchemy.orm import relationship


class Cliente(Base):
    
    __tablename__ = 'cliente'
    
    id_cliente = Column('id_cliente', Integer, primary_key=True)
    nome = Column('nome',String)
    email = Column('email',String)
    cpf = Column('cpf',String)
    telefone = Column('telefone',String)
    mes_nascimento = Column('mes_nascimento',Integer)
    veiculos = relationship("Veiculo", back_populates="cliente", cascade="all, delete-orphan")
    
    def __init__(self, nome, email, cpf, telefone, mes_nascimento):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        self.mes_nascimento = mes_nascimento
        
