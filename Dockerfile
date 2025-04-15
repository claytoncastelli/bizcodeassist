# Usando uma imagem base do Python
FROM python:3.8-slim

# Definindo o diretório de trabalho no container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiando o arquivo de dependências (requirements.txt)
COPY requirements.txt .

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código do projeto para o container
COPY . .

# Expondo a porta que o aplicativo usará (não necessário para esse projeto, mas útil para web apps)
EXPOSE 8080

# Comando para rodar o projeto (no caso, main.py)
CMD ["python", "main.py"]
