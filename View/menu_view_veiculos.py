import streamlit as st
from Controller.veiculo_controller import listar_veiculos

def menu_veiculo():
    if "exibir_veiculos" not in st.session_state:
        st.session_state.exibir_veiculos = False

    if st.session_state.exibir_veiculos:
        veiculos = listar_veiculos()
        if veiculos:
            st.write("## Veículos no Lava-Jato:")
            for veiculo in veiculos:
                st.write(f"Placa: {veiculo[1]}, Tamanho: {veiculo[2]}, Tipo: {veiculo[3]}, Entrada: {veiculo[4]}, Saída: {veiculo[5]}")
        else:
            st.info("Nenhum veículo no lava-jato.")
            
def botao_menu_veiculo():
    if st.button('Veículos 🚗', key="todos_veiculos"):
        st.session_state.exibir_veiculos = True
        st.session_state.exibir_check_out = False
        st.session_state.exibir_checkin = False
        st.session_state.exibir_adm = False
        st.session_state.infos_clientes = False
                  