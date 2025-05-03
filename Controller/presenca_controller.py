
from datetime import datetime
from DAO.conexao_presenca import fazer_check_in_bd, fazer_check_out_bd
from Models.presenca import Presenca


def fazer_check_in(placa):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    hora_entrada = datetime.now().strftime(mascara_ptbr)
    
    if fazer_check_in_bd(placa, hora_entrada):
        return True
    return False
    


def fazer_check_out(placa_checkout):
    mascara_ptbr = '%d/%m/%Y %H:%M'
    hora_saida = datetime.now().strftime(mascara_ptbr)
    
    if fazer_check_out_bd(placa_checkout, hora_saida):
        return True
    return False
    
