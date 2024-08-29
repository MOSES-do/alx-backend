#!/usr/bin/env python3
"""Setup Babel functionality in our flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request
app = Flask(__name__)


class Config:
    """Int'l Config for our app"""

    """Babel's default locale/utc"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""Treat same word routes the same regardless of an ending /"""
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns best match of supported language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def homepage():
    """Sites homepage"""

    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
