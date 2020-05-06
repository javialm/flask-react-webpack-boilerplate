from flask import Flask, render_template, g, request, redirect, url_for, flash
from flask_babel import Babel, gettext

# instance relative folder, then load config.py
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

babel = Babel(app)


@babel.localeselector
def get_locale():
    return g.lang_code


from . import views


if __name__ == '__main__':
    app.run()