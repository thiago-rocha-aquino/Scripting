import os
import subprocess
import sys

def instalar_dependencias(diretorio_projeto, requeremints_file):
    if not os.path.exists(requeremints_file):
        print("o arquivo requerements.txt não existe")
        return
    
    venv_path = os.path.join(diretorio_projeto, 'venv', 'bin', 'activate')
    subprocess.run(['source', venv_path], shell=True)

    try:
        subprocess.run(['pip', 'install', '-r', requeremints_file], check=True)
        print("depêndencias instaladas com sucesso")
    except subprocess.CalledProcessError as e:
        print(f"erro ao installar as dependencias: {e}")    

def criar_ambiente(diretorio_projeto):
    if not os.path.exists(diretorio_projeto):
        print(f"o diretorio informado não existe")
        return
    
    venv_path = os.path.join(diretorio_projeto, 'venv')

    if os.path.exists(venv_path):
        print("O ambiente virtual já existe")
        return
    try:
        subprocess.run(['virtualenv', venv_path], check=True)
        print("ambiente criado com exito")

    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o ambiente: {e}")    

def main():
    diretorio_projeto = sys.arg[1]
    requerements_file = os.path.join(diretorio_projeto, 'requirements.txt')
    criar_ambiente(diretorio_projeto)
    instalar_dependencias(diretorio_projeto, requerements_file)

if __name__ == "__main__":
     main()    