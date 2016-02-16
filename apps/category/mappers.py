from marshmallow import (Schema, fields, post_load, validates_schema)
from contracts.category import (PostCategoryRequest, PutCategoryRequest, DeleteCategoryRequest)
from contracts.category import (CATEGORY_ID, NAME, SLUG)
from apps.base.mappers import _check_include_fields


# Request

class CategorySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    slug = fields.Str()


class PostCategoryRequestSchema(CategorySchema):
    @post_load
    def make_contract(self, data):
        return PostCategoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [NAME, SLUG]
        include_key = [NAME, SLUG]
        _check_include_fields(data, require_key, include_key)


class PutCategoryRequestSchema(CategorySchema):
    @post_load
    def make_contract(self, data):
        return PutCategoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [CATEGORY_ID]
        include_key = [CATEGORY_ID, NAME, SLUG]
        _check_include_fields(data, require_key, include_key)


class DeleteCategoryRequestSchema(CategorySchema):
    @post_load
    def make_contract(self, data):
        return DeleteCategoryRequest(**data)

    @validates_schema
    def check_require_include_fields(self, data):
        require_key = [CATEGORY_ID]
        include_key = []
        _check_include_fields(data, require_key, include_key)


# Response

class PostCategoryResponseSchema(CategorySchema):
    pass


class PutCategoryResponseSchema(CategorySchema):
    pass


class DeleteCategoryResponseSchema(CategorySchema):
    pass
