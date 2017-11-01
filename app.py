# coding:utf-8
"""
this is a entry module
"""

from flask import Flask
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)


@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'


if __name__ == '__main__':
    app.run()
