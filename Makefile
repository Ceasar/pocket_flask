.PHONY: virtualenv

ENV = env

install:
	export PIP_DOWNLOAD_CACHE=.pip_download_cache; pip install --requirement requirements.txt
	# gem install foreman

virtualenv:
	test -d $(ENV) || virtualenv $(ENV)

# Run a local web server
server:
	make virtualenv
	. $(ENV)/bin/activate; make install; python wsgi.py

shell:
	python shell.py

test:
	. $(ENV)/bin/activate; make install; py.test tests/
