- Não estou conseguindo apertar o botao veiculo e aparecer as coias 
- quero no botrao check in ele busque no BD a placa e faça o check_in. Só é possivel fazer check_in dps que cadastrar o veiculo

- o veiculo so pode fazer check_in se nao tiver nenhum checkout em aberto



# Lava-Tudo: Sistema de Gerenciamento para Lava Jato 🚗🏍🧽


Este é um sistema simples de gerenciamento para um lava jato, desenvolvido utilizando Python com Streamlit para a interface do usuário, SQLAlchemy e SQLite para o gerenciamento e armazenamento de dados.


# instalar os requeriments.txt
pip install -r requeriments.txt

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

* **Check-in, Check-out e listagem de Veículos:** Permite registrar a entrada de um veículo no lava jato, coletando informações como placa, tamanho e tipo. A data e hora de entrada são registradas automaticamente.

* **Cadastramento de Clientes:** CRUDE para Clientes e tabelas relacionadas no banco de dados.\

## 🚀 Tecnologias Utilizadas
- 🐍 **Python**
- 🌐 **Streamlit** (Interface Web interativa)
- 🏛️ **SQLAlchemy** (ORM para manipulação do banco de dados)
- 📦 **SQLite** (Banco de dados leve).



# proximos passos:
    - colocar outra tabela com o nome do cliente e quem sabe mandar email promocional
    - como vou mostrar que hrs o dono pode ir buscar 
    - valor da lavagem 


## Como Executar

1.  **Certifique-se de ter o Python instalado em sua máquina.**
2.  **Instale as bibliotecas necessárias:**

    ```bash
    pip install streamlit sqlite3
    ```

    Se você tiver um arquivo `requirements.txt`, pode instalar todas as dependências com:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Navegue até o diretório raiz do projeto (`Lava-Tudo/`) no seu terminal.**
4.  **Execute o aplicativo Streamlit:**

    ```bash
    streamlit run menu_view.py
    ```

    Isso abrirá o sistema Lava-Tudo no seu navegador web padrão.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão de melhoria, correção de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma Issue ou enviar um Pull Request.





