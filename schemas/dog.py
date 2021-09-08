from flask import url_for
from typing import AsyncGenerator
from marshmallow import (
    Schema,
    fields,
    post_dump,
    validate,
    validates,
    ValidationError
)
from schemas.user import UserSchema
from schemas.pagination import PaginationSchema

def validate_age(n):
        if n < 1:
            raise ValidationError('Age must be greater than 0')
        if n >= 20:
            raise ValidationError("There's no way your dog is that old...")

class DogSchema(Schema):
    class Meta:
        ordered=True
    
    author = fields.Nested(UserSchema, attribute='user', dump_only=True, exclude=('email',))
    id = fields.Integer(dump_only=True)

    name = fields.String(required=True, validate=[validate.Length(max=30)])
    age = fields.Integer(validate=validate_age)
    color = fields.String(validate=[validate.Length(max=30)])
    cat_friendly = fields.Boolean()
    cover_url = fields.Method(serialize='dump_cover_url')
    small_dog_friendly = fields.Boolean()
    description = fields.String(validate=[validate.Length(max=200)])

    is_publish = fields.Boolean(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    # NOT NEEDED, BECAUSE PAGINATION FUNCTION / SCHEMA

    # @post_dump(pass_many=True)
    # def wrap(self, data, many, **kwargs):
    #     if many:
    #         return {'date':data}
    #     return data

    def dump_cover_url(self, dog):
        if dog.cover_image:
            return url_for('static', filename='images/dogs/{}'.format(dog.cover_image), _external=True)
        else:
            return url_for('static', filename='images/assets/default-dog-cover.jpg', _external=True)

class DogPaginationSchema(PaginationSchema):
    data = fields.Nested(DogSchema, attribute='items', many=True)