#!/bin/bash

# Saída em caso de erro
set -e

# Clonando o repositório Fairseq
git clone https://github.com/pytorch/fairseq.git
cd fairseq

# Instalando as dependências
pip install -r requirements.txt

# Construindo e instalando o Fairseq
python setup.py build develop

# Voltando ao diretório original
cd ..

#to execute - https://ai.meta.com/tools/fairseq/
#https://pytorch.org/hub/pytorch_fairseq_translation/
#chmod +x setup.sh
#./setup.sh
