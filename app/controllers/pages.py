from flask import render_template, Blueprint


pages = Blueprint('general', __name__)


@pages.route('/')
def index():
    return render_template("index.html")
