from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from http import HTTPStatus

from models.dog import Dog


class DogListResource(Resource):

    def get(self):

        dogs = Dog.get_all_published()

        data = []

        for dog in dogs:
            data.append(dog.data())

        return {'data': data}, HTTPStatus.OK

    @jwt_required
    def post(self):

        json_data = request.get_json()
        current_user = get_jwt_identity()
        dog = Dog(name=json_data['name'],
                  age=json_data['age'],
                  color=json_data['color'],
                  cat_friendly=json_data['cat_friendly'],
                  small_dog_friendly=json_data['small_dog_friendly'],
                  description=json_data['description'],
                  user_id=current_user)

        dog.save()

        return dog.data(), HTTPStatus.CREATED


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

        return dog.data, HTTPStatus.OK

    @jwt_required
    def delete(self, dog_id):

        dog = Dog.get_by_id(dog_id=dog_id)

        if dog is None:
            return {'message': 'Dog is not found'}, HTTPStatus.NOT_FOUND

        if dog.name.lower() == "bear":
            return {'message': "Can't delete Bear. He'll bite you."}, HTTPStatus.FORBIDDEN

        current_user = get_jwt_identity()

        if current_user != dog.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        dog.delete()

        return {}, HTTPStatus.NO_CONTENT


class DogPublishResource(Resource):

    def put(self, dog_id):
        dog = next((dog for dog in dog_list if dog.id == dog_id), None)

        if dog is None:
            return {'message': 'dog not found'}, HTTPStatus.NOT_FOUND

        dog.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, dog_id):
        dog = next((dog for dog in dog_list if dog.id == dog_id), None)

        if dog is None:
            return {'message': 'dog not found'}, HTTPStatus.NOT_FOUND

        dog.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
