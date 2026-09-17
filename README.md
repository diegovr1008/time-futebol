# Catálogo de Times de Futebol

Sistema web feito em Django onde o usuário se cadastra, faz login e gerencia uma lista pessoal de times de futebol que acompanha ou quer passar a acompanhar.

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- CSS próprio

## Pré-requisitos

- Python 3.10 ou superior

## Como Instalar e Rodar

```bash
git clone https://github.com/diegovr1008/time-futebol.git
cd time-futebol
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Depois, acesse http://127.0.0.1:8000/cadastro/ para criar uma conta e começar a usar o catálogo.

## Funcionalidades do Sistema

- Cadastro de usuário
- Login e logout
- Página do catálogo protegida (exige login)
- Listagem dos times cadastrados
- Adicionar novo time
- Editar time existente
- Excluir time (com confirmação)
- Cada usuário só vê e gerencia os próprios times

## Autor

DIEGO VINICIUS RODRIGUES — TECNICO DE DESENVOLVIMENTO DE SISTEMAS