# My Project - https://francisduval.github.io/presentation_stage_cegep_ste_foy/#/title-slide

Este projeto é .

BizCodeActivity
BizCodeAssistant

## Como executar

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute o arquivo principal: `python my_project/main.py`
4. Installar os pacotes listados no setup.py pip install scripts/setup.py

## Testes

1. Para rodar os testes, utilize o comando:
python -m unittest tests/test_module.py
2. pytest
3. Instalando dependencias de desenvolvimento listadas no extras_require pip install .[dev]

# Como usar api flask
1. Subir o servidor Flask: Execute o script com: python api.py
2. Fazer uma requisição GET curl :curl "http://localhost:5000/scrape?url=https://www.exemplo.com"
3. Ou com Postman, enviando uma requisição GET para:http://localhost:5000/scrape?url=https://www.exemplo.com
{
  "content": "Texto extraído da página web..."
}
{
  "error": "Não foi possível obter conteúdo"
}

# Como rodar o flask
1. Instale o pacote localmente (usando o setup.py):
python setup.py install
2. Rode a aplicação Flask
python app.py
3. Acesse a API via curl ou Postman:
http://localhost:5000/scrape?url=https://www.exemplo.com


# Usando Docker

1. Construir a imagem Docker: Execute o comando para construir a imagem a partir do Dockerfile
docker-compose build
2. Subir o container: Depois de construir a imagem, você pode iniciar o container com o seguinte comando
docker-compose up
3. Parar o container: Para parar o container, use:
docker-compose down

# Usando Docker para testes

1. docker-compose run my_project pytest


## Como executar setup.sh

1. chmod +x setup.sh
2. ./setup.sh
3. Saida do whl 
dist/
  ├── my_project-0.1.0-py3-none-any.whl
4. Instalar o pacote no seu ambiente python
pip install dist/my_project-0.1.0-py3-none-any.whl




```bash
python -m unittest discover tests/



