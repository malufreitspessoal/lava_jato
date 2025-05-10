# Ao clicar no botão "clientes"

import streamlit as st

from Controller.cliente_controller import adicionar_cliente, mostrar_clientes, verificar_credenciais
    
def botao_menu_cliente():
    if st.button("Clientes 👨‍👨‍👦‍👦", key="exibir_info_clientes"):
        st.session_state.infos_clientes = True
        st.session_state.exibir_checkin = False
        st.session_state.exibir_check_out = False
        st.session_state.infos_veiculos = False
        st.session_state.exibir_adm = False    

def menu_cliente(): 
    if 'infos_clientes' not in st.session_state:
        st.session_state.infos_clientes = False   
    
    if getattr(st.session_state, "infos_clientes", False):  
            st.subheader("Informações do Cliente")

            # Estado para controlar a exibição do formulário de cadastro
            if 'exibir_formulario_cadastro' not in st.session_state and 'exibir_todos_clientes' not in st.session_state and 'editar_cliente_por_cpf' not in st.session_state and 'excluir_cliente_por_cpf' not in st.session_state:
                st.session_state.exibir_formulario_cadastro = False
                st.session_state.exibir_todos_clientes = False
                st.session_state.editar_cliente_por_cpf = False
                st.session_state.excluir_cliente_por_cpf = False

            if st.button('Cadastrar novo cliente 🆕', key='cadastrar_novo_cliente'):
                st.session_state.exibir_formulario_cadastro = True
                st.session_state.exibir_todos_clientes = False
                st.session_state.editar_cliente_por_cpf = False
                st.session_state.excluir_cliente_por_cpf = False

            # Exibir o formulário de cadastro se o estado for True
            if st.session_state.exibir_formulario_cadastro:
                nome = st.text_input('Nome:', key="nome_input").strip().upper()
                email = st.text_input('Email:', key='email_input').strip().lower()
                cpf = st.text_input('CPF:', key='cpf_input').strip()
                telefone = st.text_input('Telefone:', key='telefone_input').strip()
                mes_nascimento = st.text_input('Mês de nascimento (1 a 12):', key='mes_nascimento_input').strip()

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Salvar Cliente", key="confirmar_cliente"):
                        if not verificar_credenciais(email, cpf, telefone, mes_nascimento):
                            st.warning('Preencha todos os campos com valores válidos.')
                        elif adicionar_cliente(nome, email, cpf, telefone, mes_nascimento) == True:
                            st.success('Cliente cadastrado com sucesso!')
                            st.session_state.exibir_formulario_cadastro = False
                            st.session_state.infos_clientes = False
                        else:
                            st.error('Erro ao cadastrar cliente.')
                with col2:
                    if st.button("Cancelar", key="cancelar_cadastro"):
                        st.session_state.exibir_formulario_cadastro = False
            
            elif st.button('Ver clientes 🔍', key= 'exibir_clientes'):
                st.session_state.exibir_todos_clientes = True
                st.session_state.exibir_formulario_cadastro = False
                st.session_state.editar_cliente_por_cpf = False
                st.session_state.excluir_cliente_por_cpf = False
                
                if st.session_state.exibir_todos_clientes:
                   clientes = mostrar_clientes()
                   for cliente in clientes:
                        st.write(f'Nome: {cliente.nome} Email: {cliente.email} CPF: {cliente.cpf} Telefone: ({cliente.telefone})  Mês de nascimento: {cliente.mes_nascimento} ')
                    
            elif st.button('Atualizar cliente 🔄', key= 'atualizar_cliente'):
                st.success('Atualizar clientes')
            elif st.button('Deletar cliente ⛔', key= 'deletar_cliente'):
                st.success('Deletando cliente')

