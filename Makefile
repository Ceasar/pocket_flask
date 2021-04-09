.PHONY: server shell test

export ENV = development
PYTEST_OPTIONS = -vv --exitfirst -n 8
VENV = config/$(ENV)/env
export PYTHONPATH := $(PYTHONPATH):.

# Run a local web server
server: $(VENV)
	. $(VENV)/bin/activate; python wsgi.py

config/%/env: config/%/requirements.txt
	python3 -m venv $@
	. $@/bin/activate && pip install --requirement $<

shell:
	python shell.py

test: $(VENV)
	. $(VENV)/bin/activate; py.test $(PYTEST_OPTIONS) tests/
