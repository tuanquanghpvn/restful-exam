from contracts.category import (GetCategoryRequest, GetCategoryResponse,
                                DetailCategoryRequest, DetailCategoryResponse,
                                PostCategoryRequest, PostCategoryResponse,
                                PutCategoryRequest, PutCategoryResponse,
                                DeleteCategoryRequest, DeleteCategoryResponse)
from .repository import CategoryRepository


class CategoryServiceAgent(object):
    @classmethod
    def get_category(cls, request_obj: GetCategoryRequest, path: str) -> GetCategoryResponse:
        category_list, total_count = CategoryRepository.get_category(limit=request_obj.limit,
                                                                     offset=request_obj.offset,
                                                                     sort=request_obj.sort)
        return GetCategoryResponse(request=request_obj, response=category_list, path=path, total_count=total_count)

    @classmethod
    def detail_category(cls, request_obj: DetailCategoryRequest) -> DetailCategoryResponse:
        category = CategoryRepository.detail_category(id=request_obj.id)
        return DetailCategoryResponse(**category.__dict__)

    @classmethod
    def post_category(cls, request_obj: PostCategoryRequest) -> PostCategoryResponse:
        category = CategoryRepository.post_category(name=request_obj.name, slug=request_obj.slug)
        return PostCategoryResponse(**category.__dict__)

    @classmethod
    def put_category(cls, request_obj: PutCategoryRequest) -> PutCategoryResponse:
        category = CategoryRepository.put_category(id=request_obj.id, name=request_obj.name, slug=request_obj.slug)
        return PutCategoryResponse(**category.__dict__)

    @classmethod
    def delete_category(cls, request_obj: DeleteCategoryRequest) -> DeleteCategoryResponse:
        category = CategoryRepository.delete_category(id=request_obj.id)
        return DeleteCategoryResponse(category)
