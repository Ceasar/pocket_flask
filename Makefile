.PHONY: virtualenv init all

ENV = env

virtualenv:
	virtualenv $(ENV)

server:
	foreman start

install:
	pip install -r requirements.txt
	gem install foreman

deploy:
	git push heroku master

heroku:
	if [[ "$(shell git remote)" =~ heroku ]]; then \
		echo "heroku exists"; \
	else \
		heroku create $(filter-out $@, $(MAKECMDGOALS)); \
	fi
	heroku ps:scale web=1
	heroku ps
	heroku logs
	heroku open
