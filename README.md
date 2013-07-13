

# ennihilator

Create web apps out of nothing.

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
git clone https://github.com/Ceasar/ennihilator
cd ennihilator
git remote rm origin
git remote add origin <the location of my new git repository>
git push -u origin master
```

# Usage

Run the project via `foreman start`.

```
$ foreman start
00:44:48 web.1  | started with pid 6949
00:44:49 web.1  |  * Running on http://0.0.0.0:5000/
00:44:49 web.1  |  * Restarting with reloader
```

Then navigate to [localhost](http://localhost:5000/) to see the running app.

## Automation

The project comes with a fabfile that is useful for automating common tasks (such as creating a heroku app) as well as providing more user-friendly commands to people not familiar with standard web tools.
