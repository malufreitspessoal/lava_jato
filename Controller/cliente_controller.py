import re
from Models.cliente import Cliente
from DAO.conexao_cliente import adicionar_cliente_bd, editar_cliente_bd, listar_clientes, excluir_cliente_bd

def adicionar_cliente(nome, email, cpf, telefone, mes_nascimento):
    cliente = Cliente(nome, email, cpf, telefone, mes_nascimento)
    if adicionar_cliente_bd(cliente) == True:
        return True
    return False

def verificar_credenciais(email, cpf, telefone, mes_nascimento):
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    padrao_cpf = r'^\d{11}$'
    padrao_telefone = r'^\d{2}(?:9\d{8}|\d{8})$'
    padrao_mes_nascimento = r'^(1[0-2]|[1-9])$'
    if re.match(padrao_email, email) and re.match(padrao_cpf, cpf) and re.match(padrao_telefone, telefone) and re.match(padrao_mes_nascimento, mes_nascimento):
        return True
    return False
