#!/usr/bin/env python3
"""Setup Babel functionality in our app"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Int'l Config for our app"""

    """Babel's default locale/utc"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFUALT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

@app.route("/")
def first_meth():
    """basic homepage"""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
