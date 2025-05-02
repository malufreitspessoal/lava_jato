from sqlalchemy import Column, ForeignKey, Integer, String
from DAO.conexao_base import Base
from sqlalchemy.orm import relationship


class Presenca(Base):
    
    __tablename__ = 'check_in_check_out'  #sqlalchemy precisa relacionar com o nome da minha tabela

    id__presenca = Column("id_presenca", Integer, primary_key= True)
    id_veiculo = Column (Integer, ForeignKey('veiculo.id_veiculo'))  # chamo a classe Column do slqalchemy para associar a coluna da minha tabela com o atributo da minha classe chamo de primary key
    check_in = Column('check_in', String(60)) # igual ao de cima, exatamente o nome da minha coluna. passando a string pra avisar que ele recebrá str
    check_out = Column('check_out', String(60)) # igual ao de cima, exatamente o nome da minha coluna. passando a string pra avisar que ele recebrá str
    veiculo = relationship("Veiculo", back_populates="check_ins")

    
    
    def __init__(self, check_in, id_veiculo, check_out = None):
        self.check_in = check_in
        self.id_veiculo = id_veiculo
        self.check_out = check_out
        