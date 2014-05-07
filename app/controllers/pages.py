"""

controllers.pages
~~~~~~~~~~~~~~~~~

Serves static pages.

"""
from flask import render_template, Blueprint


pages = Blueprint('pages', __name__)


@pages.route('/')
def index():
    return render_template("pages/index.html")
