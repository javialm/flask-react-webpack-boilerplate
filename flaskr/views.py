from . import app
from flask import Flask, render_template, g, request, redirect, url_for
from flask_babel import Babel, gettext

@app.route('/')
def index():
    # If not lang code defined, assign client lang code and redirect "home"
    g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'].keys())
    return redirect(url_for('home', lang_code=g.lang_code))


@app.route('/<lang_code>/')
def home(lang_code):
    g.lang_code = lang_code
    return render_template('index.html')