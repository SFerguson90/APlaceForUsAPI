import os

from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Api
from flask_uploads import configure_uploads

from config import Config
from extensions import (
    db,
    jwt,
    image_set,
    cache,
    limiter)

from resources.user import (
    UserListResource,
    UserResource,
    MeResource,
    UserDogListResource,
    UserActivateResource,
    UserAvatarUploadResource)

from resources.token import (
    TokenResource,
    RefreshResource,
    RevokeResource,
    black_list)

from resources.dog import (
    DogListResource,
    DogResource,
    DogPublishResource,
    DogCoverUploadResource)

@limiter.request_filter
def ip_whitelist():
    return request.remote_addr == '127.0.0.1'

def create_app():

    env = os.environ.get('ENV', 'Development')

    if env == 'Production':
        config_str = 'config.ProductionConfig'
    elif env == 'Staging':
        config_str = 'config.StagingConfig'
    else:
        config_str = 'config.DevelopmentConfig'

    app = Flask(__name__)
    app.config.from_object(config_str)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)
    configure_uploads(app, image_set)
    cache.init_app(app)
    limiter.init_app(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in black_list

def register_resources(app):

    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(UserDogListResource, '/users/<string:username>/dogs')
    api.add_resource(UserActivateResource, '/users/activate/<string:token>')
    api.add_resource(UserAvatarUploadResource, '/users/avatar')
    api.add_resource(MeResource, '/me')

    api.add_resource(TokenResource, '/token')
    api.add_resource(RefreshResource, '/refresh')
    api.add_resource(RevokeResource, '/revoke')

    api.add_resource(DogListResource, '/dogs')
    api.add_resource(DogResource, '/dogs/<int:dog_id>')
    api.add_resource(DogPublishResource, '/dogs/<int:dog_id>/publish')
    api.add_resource(DogCoverUploadResource, '/dogs/<int:dog_id>/cover')


if __name__ == '__main__':
    app = create_app()
    app.run()
