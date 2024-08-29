#!/usr/bin/env python3
"""Setup Babel functionality in our flask app"""
from flask_babel import Babel
from flask import Flask, render_template
app = Flask(__name__)


class Config:
    """Int'l Config for our app"""

    """Babel's default locale/utc"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
def first_meth():
    """basic homepage"""

    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
