from flask import render_template, Blueprint


general = Blueprint('general', __name__)


@general.route('/')
def index():
    return render_template("index.html")
