# AudiBUN

[![Build Status](https://travis-ci.org/orlandosaraivajr/AudiBUN.svg?branch=master)](https://travis-ci.org/orlandosaraivajr/AudiBUN)
[![Code Health](https://landscape.io/github/orlandosaraivajr/autobun/master/landscape.svg?style=flat)](https://landscape.io/github/orlandosaraivajr/autobun/master)

Sistema "Auditoria Básica UNificada"

### Como desenvolver ?

1. Clone o repositório
2. Crie um virtualenv 
3. Ative a virtualenv
4. Instale as dependências
5. Configure a instância com o .env 
6. Execute os testes

```console
git clone https://github.com/orlandosaraivajr/AudiBUN.git
cd AudiBUN/
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt 
cp contrib/env-sample .env
python manage.py test
python manage.py runserver
```
