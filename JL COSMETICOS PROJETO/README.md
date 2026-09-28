# JL COSMETICOS — Projeto NAP2

Projeto de desenvolvimento web em Django para uma loja virtual de cosméticos.

## Requisitos atendidos
- Banco SQLite
- Models e migrations do Django
- CRUD de Produtos, Clientes e Pedidos
- Integração Models, Views, URLs, Templates e banco
- HTML, CSS e Bootstrap
- JavaScript básico
- Painel administrativo Django

## Como executar
1. Instale Python 3.11+.
2. Abra o terminal nesta pasta.
3. Crie um ambiente virtual: `python -m venv venv`
4. Ative o ambiente virtual.
5. Instale: `pip install -r requirements.txt`
6. Execute: `python manage.py makemigrations`
7. Execute: `python manage.py migrate`
8. Crie administrador: `python manage.py createsuperuser`
9. Rode: `python manage.py runserver`
10. Acesse `http://127.0.0.1:8000/`

## Estrutura
- `jl_cosmeticos/` configurações do projeto
- `loja/` aplicação principal
- `models.py` entidades do sistema
- `views.py` regras das páginas e CRUD
- `forms.py` formulários
- `urls.py` rotas
- `templates/` interface
- `static/` CSS e JavaScript
