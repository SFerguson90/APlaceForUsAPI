from typing import AsyncGenerator
from marshmallow import (
    Schema,
    fields,
    post_dump,
    validate,
    validates,
    ValidationError
)

class DogSchema(Schema):
    class Meta:
        ordered=True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[validate.Length(max=10)])
    age = fields.Integer(required=True, validate=[validate.Length()])
    color
    cat_friendly
    small_dog_friendly
    description = fields.String(validate=[validate.Length(max=200)])
