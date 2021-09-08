from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_uploads import UploadSet, IMAGES
from flask_caching import Cache

cache = Cache()
jwt = JWTManager()
db = SQLAlchemy()
image_set = UploadSet('images', IMAGES)
