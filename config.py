import os


class Config:
    # Flask config
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = False
    
    # SQLAlchemy config
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    
    # Twilio config
    TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
    TWILIO_FROM_NUMBER = os.environ['TWILIO_FROM_NUMBER']