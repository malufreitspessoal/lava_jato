import streamlit as st

from Controller.adm_controller import CREDENCIAIS
cliente, check_in, check_out, listar_todos, adm = st.columns(5)


def menu_adm():
    if "exibir_adm" not in st.session_state:
        st.session_state.exibir_adm = False
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
                
def column_adm():
    with adm :
        if "exibir_adm" not in st.session_state:
            st.session_state.exibir_adm = False
        
        if st.button('ADM 🔒', key= 'administradores'):
            st.session_state.exibir_adm = True
            st.session_state.exibir_check_out = False
            st.session_state.exibir_checkin = False
            st.session_state.exibir_veiculos = False
            st.session_state.infos_clientes = False
            
def botao_menu_adm():
    if st.button('ADM 🔒', key= 'administradores'):
        st.session_state.exibir_adm = True
        st.session_state.exibir_check_out = False
        st.session_state.exibir_checkin = False
        st.session_state.exibir_veiculos = False
        st.session_state.infos_clientes = False        