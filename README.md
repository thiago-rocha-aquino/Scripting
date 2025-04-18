<strong>Gerenciador de Ambiente Virtual e Dependências Python</strong>

Este script Python automatiza a configuração do seu ambiente de desenvolvimento Python para este projeto. Ele realiza duas tarefas principais:

1.  **Cria um ambiente virtual (`venv`)**: Isola as dependências deste projeto das outras instalações Python no seu sistema, evitando conflitos.
2.  **Instala as dependências**: Utiliza o `pip` para instalar todas as bibliotecas listadas no arquivo `requirements.txt`, que são necessárias para executar o projeto.

## Como Usar:

1.  **Clone o repositório:** Faça o clone deste projeto para o seu computador.
2.  **Navegue até o diretório do projeto:** Abra o seu terminal ou prompt de comando e vá para a pasta raiz do projeto.
3.  **Execute o script:** Rode o seguinte comando, substituindo `<diretorio_do_projeto>` pelo caminho da pasta do projeto:

    ```bash
    python seu_script.py <diretorio_do_projeto>
    ```

    **Exemplo:**

    ```bash
    python install_deps.py .
    ```

    (O `.` representa o diretório atual, caso você esteja dentro da pasta do projeto).

## Explicação Detalhada do Código:

* **`import os`**: Permite interagir com o sistema operacional (criar pastas, verificar arquivos, etc.).
* **`import subprocess`**: Permite executar outros programas (como `virtualenv` e `pip`) a partir do script Python.
* **`import sys`**: Fornece acesso aos argumentos de linha de comando passados ao script.

### Função `instalar_dependencias(diretorio_projeto, exigemints_file)`:

* Verifica se o arquivo `requirements.txt` existe. Se não existir, informa o usuário e encerra a função.
* Tenta ativar o ambiente virtual localizado em `diretorio_projeto/venv/bin/activate`. **Observação:** A ativação feita desta forma dentro do script pode não persistir para a execução subsequente do projeto. Geralmente, a ativação é feita manualmente no terminal.
* Utiliza o `pip install -r` para instalar todas as bibliotecas listadas no arquivo `requirements.txt`.
* Informa o usuário sobre o sucesso ou a falha na instalação das dependências.

### Função `criar_ambiente(diretorio_projeto)`:

* Verifica se o diretório do projeto especificado existe. Se não existir, informa o usuário e encerra a função.
* Define o caminho para a pasta onde o ambiente virtual será criado (`diretorio_projeto/venv`).
* Verifica se o ambiente virtual já existe. Se sim, informa o usuário e encerra a função.
* Utiliza o comando `virtualenv <caminho_do_venv>` para criar um novo ambiente virtual. **Observação:** Este script assume que o pacote `virtualenv` está instalado no seu sistema. Caso não esteja, você precisará instalá-lo com `pip install virtualenv` antes de executar o script pela primeira vez.
* Informa o usuário sobre o sucesso ou a falha na criação do ambiente virtual.

### Função `main()`:

* Obtém o caminho do diretório do projeto como o primeiro argumento de linha de comando.
* Define o caminho esperado para o arquivo `requirements.txt`.
* Chama a função `criar_ambiente()` para garantir que o ambiente virtual exista.
* Chama a função `instalar_dependencias()` para instalar as dependências no ambiente virtual.

### Bloco `if __name__ == "__main__":`:

* Garante que a função `main()` seja executada somente quando o script for executado diretamente.

## Próximos Passos (Após Executar o Script):

1.  **Ative o ambiente virtual manualmente** no seu terminal antes de executar o projeto:
    * **No Linux/macOS:** `source venv/bin/activate`
    * **No Windows (Git Bash):** `source venv/Scripts/activate`
    * **No Windows (CMD):** `venv\Scripts\activate`
    * **No Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
2.  Agora você pode executar o projeto com as dependências corretas instaladas no ambiente isolado.
