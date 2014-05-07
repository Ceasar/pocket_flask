.PHONY: virtualenv init all

ENV = env

virtualenv:
	virtualenv $(ENV)

server:
	python wsgi.py

shell:
	python shell.py

install:
	pip install -r requirements.txt
	gem install foreman
