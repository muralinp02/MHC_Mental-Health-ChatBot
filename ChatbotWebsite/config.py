import os

# Config class to store all the configuration variables
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(32)
    # contain mysql database url with user and password
    #SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Murali%40123@localhost/chatbot' #mysql
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  #Alternative database if mysql not working
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
