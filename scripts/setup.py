import os
import subprocess
import sys

def run_command(command):
    """Executa um comando no terminal"""
    subprocess.run(command, shell=True, check=True)

def setup_fairseq():
    """Clona, instala dependências e configura o Fairseq"""
    if not os.path.exists("fairseq"):
        print("Clonando o repositório Fairseq...")
        run_command("git clone https://github.com/pytorch/fairseq.git")

    os.chdir("fairseq")
    print("Instalando dependências...")
    run_command(f"{sys.executable} -m pip install -r requirements.txt")

    print("Construindo e instalando Fairseq...")
    run_command(f"{sys.executable} setup.py build develop")

    os.chdir("..")
    print("Fairseq instalado com sucesso!")

if __name__ == "__main__":
    setup_fairseq()
