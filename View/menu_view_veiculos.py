import streamlit as st
from Controller.cliente_controller import confirmar_cliente
from Controller.veiculo_controller import adicionar_veiculo, verificar_placa, listar_veiculos
'''
tem que cadastrar o veiculo e no check_in so pedir a placa.
'''


def botao_menu_veiculo():
    if st.button('Veículos 🚗', key="todos_veiculos"):
        st.session_state.infos_veiculos = True
        st.session_state.exibir_check_out = False
        st.session_state.exibir_checkin = False
        st.session_state.exibir_adm = False
        st.session_state.infos_clientes = False
                  
                  
def menu_veiculos():
    
    if 'infos_veiculos' not in st.session_state:
        st.session_state.infos_veiculos = False
    
    if getattr(st.session_state, "infos_veiculos", False):  
            st.subheader("Informações do Veiculo")

            if 'exibir_formulario_cadastro_carro' not in st.session_state and 'exibir_todos_veiculos' not in st.session_state:
                st.session_state.exibir_formulario_cadastro_carro = False
                st.session_state.exibir_todos_veiculos = False
                
                
            if st.button('Exibir Veículos 🆕', key='exibir_veiculo'):
                st.session_state.exibir_todos_veiculos = True
                st.session_state.exibir_formulario_cadastro_carro = False
                
                
            if st.session_state.exibir_todos_veiculos:
                veiculos = listar_veiculos()
                if veiculos:
                    st.write("## Veículos Cadastrados:")
                    st.table(veiculos)
                    # for veiculo in veiculos:
                    #     st.write(f"Placa: {veiculo[0]}, Tamanho: {veiculo[1]}, Tipo: {veiculo[2]}, Entrada: {veiculo[3]}, Saída: {veiculo[4]}")
                else:
                    st.info("Nenhum veículo no lava-jato.")

            if st.button('Cadastrar novo Veículo 🆕', key='cadastrar_novo_veiculo'):
               st.session_state.exibir_formulario_cadastro_carro = True
               st.session_state.exibir_todos_veiculos = False
            
                
                
                        
            if st.session_state.exibir_formulario_cadastro_carro:
                st.subheader("Informações do Veículo para Check-in")
                placa = st.text_input('Placa:', key="placa_key").upper().strip()
                tamanho = st.selectbox("Tamanho", ["Selecione", "P", "M", "G"], key="tamanho_key")
                tipo = st.selectbox("Tipo", ["Selecione", "Carro", "Moto"], key="tipo_key")
                cpf = st.text_input('Cliente (CPF)', key="cpf_cliente_key")
                if st.button("Salvar Check-in", key="confirmar_cadastro"):
                        if verificar_placa(placa) == False:
                            st.warning('Placa inválida')
                        if tamanho != "Selecione" and tipo != "Selecione" and verificar_placa(placa)== True and confirmar_cliente(cpf) != False:
                            id_cliente = confirmar_cliente(cpf)
                            adicionar_veiculo(placa, tamanho, tipo, id_cliente.id_cliente)
                            st.success(f"Veículo cadastrado com sucesso ✅!")
                            st.session_state.exibir_checkin = False
                        else:
                            st.warning("Por favor, preencha todos os campos.")
                        
