from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from config import Config
from extensions import db, jwt
from resources.user import UserListResource
from resources.dog import DogListResource, DogResource, DogPublishResource


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_resources(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)


def register_resources(app):
    api = Api(app)

    api.add_resource(UserListResource, '/users')
    api.add_resource(DogListResource, '/dogs')
    api.add_resource(DogResource, '/dogs/<int:dog_id>')
    api.add_resource(DogPublishResource, '/dogs/<int:dog_id>/publish')


if __name__ == '__main__':
    app = create_app()
    app.run()
