Recomendo utilizar um ambiente virtual para instalar as dependências do projeto.

A criação do ambiente e a instalação pode ser feita assim:
Dentro da raiz do repositório crie o ambiente virtual
python3 -m venv .venv
Ativar com
source .venv/bin/activate
Instale os requerimentos
pip install -r requirements.txt

Para rodar localmente:
python3 manage.py runserver

Quando terminar desative ambiente virtual com
deactivate
