import os
import re

class Config:

    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    UPLOADED_IMAGES_DEST = 'static/images'
    MAX_CONTENT_LENGTH = 10485760

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 10*60

    database_path = os.environ['DATABASE_URL']
    if database_path.startswith('postgres://'):
        database_path = database_path.replace('postgres://', 'postgresql://', 1)

    SQLALCHEMY_DATABASE_URI = database_path

class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://apfugAdmin:12345@localhost/apfug"
    SECRET_KEY = 'super-secret-key'

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    database_path = os.environ['DATABASE_URL']
    if database_path.startswith('postgres://'):
        database_path = database_path.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI = database_path

class StagingConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    database_path = os.environ['DATABASE_URL']
    if database_path.startswith('postgres://'):
        database_path = database_path.replace('postgres://', 'postgresql://', 1)
        
    SQLALCHEMY_DATABASE_URI = database_path
