from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from http import HTTPStatus

from models.dog import Dog
from schemas.dog import DogSchema

dog_schema = DogSchema()
dog_list_schema = DogSchema(many=True)

class DogListResource(Resource):

    def get(self):

        dogs = Dog.get_all_published()

        return dog_list_schema.dump(dogs).data, HTTPStatus.OK

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
        dog.cat_friendly = data.get('cat_friendly') or dog.cat_friendly
        dog.small_dog_friendly = data.get('small_dog_friendly') or dog.small_dog_friendly
        dog.description = data.get('description') or dog.description

        dog.save()

        return dog_schema.dump(dog).data, HTTPStatus.OK


class DogResource(Resource):

    @jwt_optional
    def get(self, dog_id):

        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'Dog is not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if dog.is_publish == False and dog.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return dog.data(), HTTPStatus.OK

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
