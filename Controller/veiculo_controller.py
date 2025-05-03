from datetime import datetime
from DAO.conexao_veiculo import adicionar_veiculo_bd, remover_veiculo_bd_por_placa, listar_veiculos_bd
from Models.presenca import Presenca
from Models.veiculo import Veiculo
import re


    

def adicionar_veiculo(placa, tamanho, tipo, id_cliente_cpf):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    hora_entrada = datetime.now().strftime(mascara_ptbr)
    veiculo = Veiculo(placa=placa, tamanho=tamanho, tipo=tipo, id_cliente= id_cliente_cpf)
    presenca = Presenca(hora_entrada, id_veiculo= veiculo.id_veiculo)
    adicionar_veiculo_bd(veiculo, presenca)

def remover_veiculo(placa):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    saida = datetime.now().strftime(mascara_ptbr)
    removido = remover_veiculo_bd_por_placa(placa, saida)
    if not removido:
        return False
    return True
    

def listar_veiculos():
    return listar_veiculos_bd()


def verificar_placa(placa):
    padrao_mercosul = r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$'
    padrao_antigo = r'^[A-Z]{3}[0-9]{4}$'
    
    if re.match(padrao_mercosul, placa) or re.match(padrao_antigo, placa):
        return True
    else:
        return False
