from datetime import datetime
from DAO.conexao_lava_jato import adicionar_veiculo_bd, remover_veiculo_bd_por_placa, listar_veiculos_bd
from Models.veiculo import Veiculo
import streamlit as st

def adicionar_veiculo(placa, tamanho, tipo):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    entrada = datetime.now().strftime(mascara_ptbr)
    veiculo = Veiculo(placa=placa, tamanho=tamanho, entrada=entrada, tipo=tipo)
    adicionar_veiculo_bd(veiculo)

def remover_veiculo(placa):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    saida = datetime.now().strftime(mascara_ptbr)
    removido = remover_veiculo_bd_por_placa(placa, saida)
    if not removido:
        return False
    return True
    

def listar_veiculos():
    return listar_veiculos_bd()