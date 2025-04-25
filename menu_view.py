import streamlit as st
from Controller.adm_controller import CREDENCIAIS
from Controller.veiculo_controller import adicionar_veiculo, remover_veiculo, listar_veiculos, verificar_placa
from DAO.conexao_carro import *

# Garante que a tabela seja criada no início
criar_tabela_se_nao_existe()


st.title('Lava-Tudo 🚗🏍🧽')
st.markdown('## O que você quer fazer?')

cliente, check_in, check_out, listar_todos, adm = st.columns(5)

with check_in:
    if 'exibir_checkin' not in st.session_state:
        st.session_state.exibir_checkin = False

    if st.button("Check-in ✅", key="check_in"):
        st.session_state.exibir_checkin = True
        st.session_state.exibir_check_out = False
        st.session_state.exibir_veiculos = False
        st.session_state.exibir_adm = False
        
        
        

with check_out:
    if "exibir_check_out" not in st.session_state:
        st.session_state.exibir_check_out = False
        

    if 'placa_checkout' not in st.session_state:
        st.session_state.placa_checkout = ""

    if st.button("Check-out ❌", key="check_out"):
        st.session_state.exibir_check_out = True
        st.session_state.exibir_checkin = False
        st.session_state.exibir_veiculos = False
        st.session_state.exibir_adm = False
        
        

with listar_todos:
    if "exibir_veiculos" not in st.session_state:
        st.session_state.exibir_veiculos = False

    if st.button('Veículos 🚗', key="todos_veiculos"):
        st.session_state.exibir_veiculos = True
        st.session_state.exibir_check_out = False
        st.session_state.exibir_checkin = False
        st.session_state.exibir_adm = False
        
        
with adm :
    if "exibir_adm" not in st.session_state:
        st.session_state.exibir_adm = False
    
    if st.button('ADM 🔒', key= 'administradores'):
        st.session_state.exibir_adm = True
        st.session_state.exibir_check_out = False
        st.session_state.exibir_checkin = False
        st.session_state.exibir_veiculos = False
        
with cliente:
    if 'infos_clientes' not in st.session_state:
        st.session_state.infos_clientes = False

    if st.button("Clientes 👨‍👨‍👦‍👦", key="exibir_info_clientes"):
        st.session_state.infos_clientes = True
        st.session_state.exibir_checkin = False
        st.session_state.exibir_check_out = False
        st.session_state.exibir_veiculos = False




if st.session_state.exibir_checkin:
    st.subheader("Informações do Veículo para Check-in")
    placa = st.text_input('Placa:', key="placa_key").upper().strip()
    tamanho = st.selectbox("Tamanho", ["Selecione", "P", "M", "G"], key="tamanho_key")
    tipo = st.selectbox("Tipo", ["Selecione", "Carro", "Moto"], key="tipo_key")

    if st.button("Salvar Check-in", key="confirmar_checkin"):
        if verificar_placa(placa) == False:
            st.warning('Placa inválida')
        if tamanho != "Selecione" and tipo != "Selecione" and verificar_placa(placa)== True:
            adicionar_veiculo(placa, tamanho, tipo)
            st.success(f"Veículo com placa '{placa}' check-in feito ✅!")
            st.session_state.exibir_checkin = False
        else:
            st.warning("Por favor, preencha todos os campos.")



if st.session_state.exibir_check_out:
    st.subheader("Informações do Veiculo para Checkout")
    placa_checkout = st.text_input('Informe a placa do veículo').upper().strip()
    if st.button("Confirmar Check-out", key= "confirmar_check_out"):
        if placa_checkout:
            if remover_veiculo(placa_checkout):
                st.success(f"Checkout para veículo com placa '{placa_checkout}' realizado!")
                st.session_state.exibir_check_out = False
            elif remover_veiculo(placa_checkout) == False:
                st.warning('Veículo não encontrado')
        else:
            st.warning("Por favor, informe a placa do veículo para checkout.")



if st.session_state.exibir_veiculos:
    veiculos = listar_veiculos()
    if veiculos:
        st.write("## Veículos no Lava-Jato:")
        for veiculo in veiculos:
            st.write(f"Placa: {veiculo[1]}, Tamanho: {veiculo[2]}, Tipo: {veiculo[3]}, Entrada: {veiculo[4]}, Saída: {veiculo[5]}")
    else:
        st.info("Nenhum veículo no lava-jato.")


if st.session_state.exibir_adm:
    st.title('Login')
    user = st.text_input('User: ', key= 'user_login').upper().strip()
    pwr = st.text_input('Senha: ', key= "password_login")
    if st.button("Entrar", key= "entrar_adm"):
        adm = next(iter(CREDENCIAIS))
        
    
        if user == adm and pwr == CREDENCIAIS[f'{user}']:
            st.session_state.exibir_adm = False
            st.success('Bem vindo')
        
                    
            financeiro = st.columns(2)

                    

            with financeiro:
                if "infos_financeira" not in st.session_state:
                    st.session_state.infos_financeira = False
                    

                if st.button("Financeiro 💲", key="exibir_infos_financeira"):
                    st.session_state.infos_financeira = True
                    st.session_state.exibir_checkin = False        
                    st.session_state.exibir_checkin = False
                    st.session_state.exibir_check_out = False
                    st.session_state.exibir_veiculos = False
        
        else:
            st.warning('Credenciais inválidas')