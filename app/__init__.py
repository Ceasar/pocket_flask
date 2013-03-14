from flask import Flask

"""
An instance of Flask will be our WSGI application.
The first argument is the name of the application's module.
If you are using a single module (as in this example),
you should use __name__ because depending on if it's started as
application or imported as module the name will be different
('__main__' versus the actual import name).
For more information, have a look at the Flask documentation.
"""
app = Flask(__name__)

from app.views import general
