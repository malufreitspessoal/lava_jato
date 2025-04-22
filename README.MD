proximos passos:
    - como vou mostrar que hrs o dono pode ir buscar 
    - valor da lavagem 


# para mais tarde
- colocar outra tabela com o nome do cliente e quem sabe mandar email promocional


# instalar os requeriments.txt
pip install -r requeriments.txt

# Lava-Tudo: Sistema de Gerenciamento para Lava Jato

Este é um sistema simples de gerenciamento para um lava jato, desenvolvido utilizando Python com Streamlit para a interface do usuário e SQLite para o armazenamento de dados.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

* **Check-in de Veículos:** Permite registrar a entrada de um veículo no lava jato, coletando informações como placa, tamanho e tipo. A data e hora de entrada são registradas automaticamente.
* **Check-out de Veículos:** Permite marcar a saída de um veículo, registrando a data e hora de saída.
* **Listagem de Veículos:** Exibe todos os veículos atualmente registrados no sistema, mostrando suas informações de entrada e, se aplicável, saída.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Streamlit:** Framework Python para criar interfaces web interativas de forma rápida e fácil.
* **SQLite:** Banco de dados leve e auto-contido para armazenar os dados dos veículos.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:
Markdown

# Lava-Tudo: Sistema de Gerenciamento para Lava Jato

Este é um sistema simples de gerenciamento para um lava jato, desenvolvido utilizando Python com Streamlit para a interface do usuário e SQLite para o armazenamento de dados.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:

* **Check-in de Veículos:** Permite registrar a entrada de um veículo no lava jato, coletando informações como placa, tamanho e tipo. A data e hora de entrada são registradas automaticamente.
* **Check-out de Veículos:** Permite marcar a saída de um veículo, registrando a data e hora de saída.
* **Listagem de Veículos:** Exibe todos os veículos atualmente registrados no sistema, mostrando suas informações de entrada e, se aplicável, saída.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Streamlit:** Framework Python para criar interfaces web interativas de forma rápida e fácil.
* **SQLite:** Banco de dados leve e auto-contido para armazenar os dados dos veículos.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

Lava-Tudo/
├── DAO/
│   └── conexao_sqlite.py     # Lógica de conexão e acesso ao banco de dados SQLite
├── Controller/
│   └── veiculo_controller.py # Lógica de controle das operações dos veículos
├── Models/
│   └── veiculo.py            # Definição da classe Veiculo (se houver)
├── menu_view.py              # Script principal da interface Streamlit
└── README.md                 # Este arquivo


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





