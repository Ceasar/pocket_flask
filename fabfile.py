from fabric.api import local


def boostrap():
    # Setup virtualenv
    local("virtualenv venv --distribute")
    local("source venv/bin/activate")
    # Install Flask
    local("pip install -r requirements.txt")
    # Create the Procfile
    local("echo 'web: python app.py' > Procfile")
    # Create the gitignore file
    local("echo 'venv' >> .gitignore")
    local("echo '*.pyc' >> .gitignore")
    # Commit everything with git
    local("git init")
    local("git add .")
    local("git commit -m 'first commit'")


def heroku():
    # Create a new Heroku app
    local("heroku create")
    # Push the app to Heroku's servers
    local("git push heroku master")
    # Deploy the app
    local("heroku ps:scale web=1")
    local("heroku ps")
    # Make sure everything is okay
    local("heroku logs")
    # Open the app!
    local("heroku open")


def run():
    local("python app.py")
