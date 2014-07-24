.PHONY: virtualenv

ENV = development
VENV = config/$(ENV)/env
export PYTHONPATH := $(PYTHONPATH):.

# Run a local web server
server: $(VENV)
	. $(VENV)/bin/activate; python wsgi.py

config/%/env: config/%/requirements.txt
	virtualenv $@
	. $@/bin/activate && pip install --requirement $<

shell:
	python shell.py

test: $(VENV)
	. $(VENV)/bin/activate; py.test tests/
