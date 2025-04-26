import streamlit as st
from Controller.veiculo_controller import remover_veiculo

def menu_check_out():
    if "exibir_check_out" not in st.session_state:
        st.session_state.exibir_check_out = False
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
                
def botao_menu_check_out():
    if st.button("Check-out ❌", key="check_out"):
        st.session_state.exibir_check_out = True
        st.session_state.exibir_checkin = False
        st.session_state.exibir_veiculos = False
        st.session_state.exibir_adm = False
        st.session_state.infos_clientes = False                  