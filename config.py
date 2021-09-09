class Config:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://apfugAdmin:12345@localhost/apfug"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'super-secret-key'
    
    JWT_ERROR_MESSAGE_KEY = 'message'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    UPLOADED_IMAGES_DEST = 'static/images'
    MAX_CONTENT_LENGTH = 10485760

    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 10*60

    RATELIMIT_HEADERS_ENABLED = True
