#!/usr/bin/env python3
"""Setup Babel functionality in our flask app"""
from flask_babel import Babel
from flask import Flask, render_template, request, g
app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    """retrieves query parameter from URL - locale=fr
         and converts it to a list = ['locale=fr']
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    """Returns best match of supported language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request() -> None:
    """carries out routines before each request's resolution.
    """
    user = get_user()
    g.user = user


def get_user():
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.route("/")
def homepage():
    """Sites homepage"""

    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
