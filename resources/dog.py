import os
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (get_jwt_identity, jwt_required, jwt_optional)
from http import HTTPStatus
from extensions import image_set
from utils import save_image

from models.dog import Dog
from schemas.dog import DogSchema, DogPaginationSchema

from webargs import fields
from webargs.flaskparser import use_kwargs

dog_pagination_schema = DogPaginationSchema()
dog_cover_schema = DogSchema(only=('cover_url', ))
dog_schema = DogSchema()
dog_list_schema = DogSchema(many=True)

class DogCoverUploadResource(Resource):

    @jwt_required
    def put(self, dog_id):

        file = request.files.get('cover')

        # EXISTS?
        if not file:
            return {'message': 'Not a valid image'}, HTTPStatus.BAD_REQUEST
        # FILE EXTENSION PERMITTED?
        if not image_set.file_allowed(file, file.filename):
            return {'message': 'File type not allowed'}, HTTPStatus.BAD_REQUEST

        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'Dog not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != dog.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        if dog.cover_image:
            cover_path = image_set.path(folder='dogs', filename=dog.cover_image)
            if os.path.exists(cover_path):
                os.remove(cover_path)

        filename = save_image(image=file, folder='dogs')

        dog.cover_image = filename
        dog.save()

        return dog_cover_schema.dump(dog).data, HTTPStatus.OK
            

class DogListResource(Resource):

    @use_kwargs({
        'q': fields.Str(missing=''),
        'page': fields.Int(missing=1),
        'per_page': fields.Int(missing=20),
        'sort': fields.Str(missing='created_at'),
        'order': fields.Str(missing='desc')
        })
    def get(self, q, page, per_page, sort, order):
        
        if sort not in ['created_at', 'age', 'updated_at']:
            sort = 'created_at'
        
        if order not in ['asc','desc']:
            order = 'desc'

        paginated_dogs = Dog.get_all_published(q, page, per_page, sort, order)

        return dog_pagination_schema.dump(paginated_dogs).data, HTTPStatus.OK

    @jwt_required
    def post(self):

        json_data = request.get_json()
        current_user = get_jwt_identity()
        data, errors = dog_schema.load(data=json_data)

        if errors:
            return {'message': "Validation errors", 'errors': errors}, HTTPStatus.BAD_REQUEST

        dog = Dog(**data)
        dog.user_id = current_user
        dog.save()

        return dog_schema.dump(dog).data, HTTPStatus.CREATED


class DogResource(Resource):

    @jwt_optional
    def get(self, dog_id):

        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'Dog is not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if dog.is_publish == False and dog.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return dog_schema.dump(dog).data, HTTPStatus.OK

    @jwt_required
    def put(self, dog_id):

        json_data = request.get_json()

        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'Dog not found'}, HTTPStatus.NOT_FOUND

        dog.name = json_data['name']
        dog.age = json_data['age']
        dog.color = json_data['color']
        dog.cat_friendly = json_data['cat_friendly']
        dog.small_dog_friendly = json_data['small_dog_friendly']
        dog.description = json_data['description']

        dog.save()

        return dog.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, dog_id):

        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'Dog is not found'}, HTTPStatus.NOT_FOUND

        # RIP Bear
        if dog.id == 1:
            return {'message': "Can't delete Bear. He'll bite you."}, HTTPStatus.FORBIDDEN

        current_user = get_jwt_identity()

        if current_user != dog.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        dog.delete()

        return {}, HTTPStatus.NO_CONTENT

    # WON'T PATCH BOOLEAN VALUES. 9/5/2021
    @jwt_required
    def patch(self, dog_id):

        json_data = request.get_json()

        data, errors = dog_schema.load(data=json_data, partial=('name',))

        if errors:
            return {'message': 'Validation errors','errors':errors}, HTTPStatus.BAD_REQUEST

        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'Dog not found'}, HTTPStatus.NOT_FOUND

        if dog.id == 1:
            return {'message': "Bear won't change. He'll bite you."}, HTTPStatus.FORBIDDEN

        current_user = get_jwt_identity()

        if current_user != dog.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        dog.name = data.get('name') or dog.name
        dog.age = data.get('age') or dog.age
        dog.color = data.get('color') or dog.color
        dog.location = data.get('location') or dog.location
        dog.cat_friendly = data.get('cat_friendly') or dog.cat_friendly
        dog.small_dog_friendly = data.get('small_dog_friendly') or dog.small_dog_friendly
        dog.description = data.get('description') or dog.description

        dog.save()

        return dog_schema.dump(dog).data, HTTPStatus.OK


class DogPublishResource(Resource):

    @jwt_required
    def put(self, dog_id):
        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'dog not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != dog.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        dog.is_publish = True
        dog.save()

        return {}, HTTPStatus.NO_CONTENT

    @jwt_required
    def delete(self, dog_id):
        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'dog not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user != dog.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        dog.is_publish = False
        dog.save()
        
        return {}, HTTPStatus.NO_CONTENT
