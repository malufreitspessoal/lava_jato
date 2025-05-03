import streamlit as st

from Controller.cliente_controller import confirmar_cliente
from Controller.veiculo_controller import verificar_placa
from Controller.presenca_controller import fazer_check_in

def menu_check_in():
    if 'exibir_checkin' not in st.session_state:
        st.session_state.exibir_checkin = False
    if st.session_state.exibir_checkin:
        st.subheader("Informações do Veículo para Check-in")
        placa = st.text_input('Placa:', key="placa_key").upper().strip()
        
        
        # Aui tenho que arrumar para sempre que adicionar a plca, pega do banco as informaçõese e faz apenas o check-in
        if st.button("Salvar Check-in", key="confirmar_checkin"):
                if fazer_check_in(placa):
                    st.success(f"Veículo com placa '{placa}' check-in feito ✅!")
                    st.session_state.exibir_checkin = False
        
                else:
                        st.warning("Veículo não encontrado ou já está no Lava-Jato.")
                        
def botao_menu_check_in():
    if st.button("Check-in ✅", key="check_in"):
        st.session_state.exibir_checkin = True
        st.session_state.exibir_check_out = False
        st.session_state.infos_veiculos = False
        st.session_state.exibir_adm = False
        st.session_state.infos_clientes = False              