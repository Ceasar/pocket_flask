
# Pocket Flask

Tool to scaffold for Flask apps.

Design Goals:

- Speed. Application setup time should be minimized.
- Easy. Non-programmers should be able to deploy an application locally.

Application Stack:

- Bootstrap
- Flask
- Heroku

# Installation

- Download [Heroku Toolbelt](https://toolbelt.heroku.com/)
- Install [pip](http://www.pip-installer.org/en/latest/installing.html)
- Install [virtualenv](http://www.virtualenv.org/en/latest/#installation)
- Install fabric. (`pip install fabric`)

# Bootstrapping

```
git clone https://github.com/Ceasar/pocket_flask
cd pocket_flask
git remote rm origin
git remote add origin <the location of my new git repository>
git push -u origin master
```

# Usage

Run the project via `make server`, then navigate to
[localhost](http://localhost:5000/) to see the running app.
