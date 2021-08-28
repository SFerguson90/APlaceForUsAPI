class Config:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://apfugAdmin:12345@localhost/apfug"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'
