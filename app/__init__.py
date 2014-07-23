import logging

from flask import Flask

from app.controllers import pages

"""
An instance of Flask will be our WSGI application.
The first argument is the name of the application's module.
If you are using a single module (as in this example),
you should use __name__ because depending on if it's started as
application or imported as module the name will be different
('__main__' versus the actual import name).
For more information, have a look at the Flask documentation.
"""


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    app.register_blueprint(pages)

    app.logger.setLevel(logging.NOTSET)
    app.logger.addHandler(logging.StreamHandler())

    return app
