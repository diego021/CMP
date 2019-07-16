#!/usr/bin/env python3
import os
from flask import Flask
from youtube.engine import YoutubeSong

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        MONGO_URI = 'mongodb://localhost:27017/CMP'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/welcome')
    def welcome():
        return 'Welcome to CMP!!'

    return app

if __name__ == '__main__':
    my_song = YoutubeSong('behind blue eyes')
    my_song.search()
    my_song.download()

