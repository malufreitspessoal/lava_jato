import re
import pandas as pd
from Models.cliente import Cliente
from DAO.conexao_cliente import adicionar_cliente_bd, editar_cliente_bd, listar_clientes_bd, excluir_cliente_bd, mostrar_cpf_filtrado

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


def mostrar_cpf_filtrado_cliente(cpf):
    if mostrar_cpf_filtrado(cpf):
        return True
    return False



def mostrar_clientes():
    clientes = listar_clientes_bd() # lista de obj
    
    if clientes:
        clientes_dict = [vars(cliente) for cliente in clientes]  # Convertendo a lista de objetos para uma lista de dicionários
        df = pd.DataFrame(clientes_dict)
        return df
    
def confirmar_cliente(cpf):
    lista_filtrada = mostrar_cpf_filtrado(cpf)
    if lista_filtrada:
        return lista_filtrada[0]
    return False