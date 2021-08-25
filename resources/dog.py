from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.dog import Dog, dog_list


class DogListResource(Resource):

    def get(self):
        data = []
        for dog in dog_list:
            if dog.is_publish is True:
                data.append(dog.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        dog = Dog(name=data['name'],
                  age=data['age'],
                  color=data['color'],
                  cat_friendly=data['cat_friendly'],
                  small_dog_friendly=data['small_dog_friendly'],
                  description=data['description'])

        dog_list.append(dog)

        return dog.data, HTTPStatus.CREATED


class DogResource(Resource):

    def get(self, dog_id):
        dog = next((dog for dog in dog_list if dog.id ==
                    dog_id and dog.is_publish == True), None)

        if dog is None:
            return {'message': 'dog is not found'}, HTTPStatus.NOT_FOUND

        return dog.data, HTTPStatus.OK

    def put(self, dog_id):
        data = request.get_json()

        dog = next((dog for dog in dog_list if dog.id ==
                    dog_id), None)

        if dog is None:
            return {'message': 'dog not found'}, HTTPStatus.NOT_FOUND

        dog.name = data['name']
        dog.age = data['age']
        dog.color = data['color']
        dog.cat_friendly = data['cat_friendly']
        dog.small_dog_friendly = data['small_dog_friendly']
        dog.description = data['description']

        return dog.data, HTTPStatus.OK


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
