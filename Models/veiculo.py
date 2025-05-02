from sqlalchemy import Column, ForeignKey, Integer, String
from DAO.conexao_base import Base
from sqlalchemy.orm import relationship


class Veiculo(Base):

    __tablename__ = 'veiculo'  #sqlalchemy precisa relacionar com o nome da minha tabela

    id_veiculo = Column("id_veiculo", Integer, primary_key= True)  # chamo a classe Column do slqalchemy para associar a coluna da minha tabela com o atributo da minha classe chamo de primary key
    id_cliente = Column(Integer, ForeignKey('cliente.id_cliente')) # aqui ele sempre se relaciona com a chave primaria da tabela cliente.
    placa =  Column('placa', String(60))
    tamanho =  Column('tamanho', String(60))
    tipo = Column('tipo', String(60))
    cliente = relationship("Cliente", back_populates="veiculos")
    check_ins = relationship("Presenca", back_populates="veiculo")
    
    def __init__(self, id_cliente, placa, tamanho, tipo):
        self.placa = placa
        self.tamanho = tamanho 
        self.tipo = tipo
        self.id_cliente = id_cliente