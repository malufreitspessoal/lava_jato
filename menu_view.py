import streamlit as st
from View.menu_view_adm import botao_menu_adm, menu_adm
from View.menu_view_checkin import botao_menu_check_in, menu_check_in
from View.menu_view_checkout import botao_menu_check_out, menu_check_out
from View.menu_view_clientes import botao_menu_cliente, menu_cliente
from View.menu_view_veiculos import botao_menu_veiculo, menu_veiculo

# Garante que a tabela seja criada no início

st.title('Lava-Tudo 🚗🏍🧽')
st.markdown('## O que você quer fazer?')

cliente, check_in, check_out, listar_todos, adm = st.columns(5)

with cliente:
    botao_menu_cliente()

with check_in:
    botao_menu_check_in()

with check_out:
    botao_menu_check_out()

with listar_todos:
    botao_menu_veiculo()
        
with adm :
    botao_menu_adm()
        
# # Ao clicar no botão "clientes"
menu_cliente()

# Ao clicar no botão "check-in"
menu_check_in()

# Ao clicar no botão "check-out"
menu_check_out()

# Ao clicar no botão "veiculos"
menu_veiculo()

# Ao clicar no botão "ADM"
menu_adm()