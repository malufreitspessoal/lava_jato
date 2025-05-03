import streamlit as st
from View.menu_view_adm import botao_menu_adm, menu_adm
from View.menu_view_checkin import botao_menu_check_in, menu_check_in
from View.menu_view_checkout import botao_menu_check_out, menu_check_out
from View.menu_view_clientes import botao_menu_cliente, menu_cliente
from View.menu_view_veiculos import botao_menu_veiculo, menu_veiculos

def inicializar_estado():
    defaults = {
        'infos_clientes': False,
        'exibir_checkin': False,
        'exibir_check_out': False,
        'infos_veiculos': False,
        'exibir_adm': False,
        'exibir_formulario_cadastro': False,
        'exibir_veiculos': False,
        'exibir_formulario_checkin': False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

inicializar_estado()

st.title('Lava-Tudo 🚗🏍🧽')
st.markdown('## O que você quer fazer?')

cliente, check_in, check_out, infos_veiculos, adm = st.columns(5)

with cliente:
    botao_menu_cliente()

with check_in:
    botao_menu_check_in()

with check_out:
    botao_menu_check_out()

with infos_veiculos:
    botao_menu_veiculo()

with adm:
    botao_menu_adm()

# Renderizar menus com base no estado
if st.session_state.infos_clientes:
    menu_cliente()

if st.session_state.exibir_checkin:
    menu_check_in()

if st.session_state.exibir_check_out:
    menu_check_out()

if st.session_state.infos_veiculos:
    menu_veiculos()

if st.session_state.exibir_adm:
    menu_adm()