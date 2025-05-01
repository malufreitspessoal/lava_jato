import streamlit as st

from Controller.cliente_controller import confirmar_cliente
from Controller.veiculo_controller import adicionar_veiculo, verificar_placa

def menu_check_in():
    if 'exibir_checkin' not in st.session_state:
        st.session_state.exibir_checkin = False
    if st.session_state.exibir_checkin:
        st.subheader("Informações do Veículo para Check-in")
        placa = st.text_input('Placa:', key="placa_key").upper().strip()
        tamanho = st.selectbox("Tamanho", ["Selecione", "P", "M", "G"], key="tamanho_key")
        tipo = st.selectbox("Tipo", ["Selecione", "Carro", "Moto"], key="tipo_key")
        cpf = st.text_input('Cliente (CPF)', key="cpf_cliente_key")

        if st.button("Salvar Check-in", key="confirmar_checkin"):
            if verificar_placa(placa) == False:
                st.warning('Placa inválida')
            if tamanho != "Selecione" and tipo != "Selecione" and verificar_placa(placa)== True and confirmar_cliente(cpf) != False:
                id_cliente = confirmar_cliente(cpf)
                adicionar_veiculo(placa, tamanho, tipo, id_cliente.id_cliente)
                st.success(f"Veículo com placa '{placa}' check-in feito ✅!")
                st.session_state.exibir_checkin = False
            else:
                st.warning("Por favor, preencha todos os campos.")
                
def botao_menu_check_in():
    if st.button("Check-in ✅", key="check_in"):
        st.session_state.exibir_checkin = True
        st.session_state.exibir_check_out = False
        st.session_state.exibir_veiculos = False
        st.session_state.exibir_adm = False
        st.session_state.infos_clientes = False              