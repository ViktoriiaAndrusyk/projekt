import os

project_folder = os.path.abspath(os.getcwd())

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///DB.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
