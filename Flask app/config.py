import os 
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://myuser:mypassword@localhost/my_local_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
