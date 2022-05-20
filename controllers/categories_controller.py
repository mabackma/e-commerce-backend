from flask.views import MethodView
from flask import request, jsonify
from models import Category, Product
from validators.validation_categories import validate_categories_route_handler

class CategoryProductsRouteHandler(MethodView):

    def get(self, _id):
        category = Category.get_by_id(_id)
        products_list = category.get_products()
        return jsonify(products=Product.list_to_json(products_list))


class CategoriesRouteHandler(MethodView):

    @validate_categories_route_handler
    def post(self):
        request_body = request.get_json()

        name = request_body['name']
        category = Category(name)
        category.create()

        return jsonify(category=category.to_json())

    def get(self):
        categories = Category.get_all()

        return jsonify(categories=Category.list_to_json(categories))


class CategoryRouteHandler(MethodView):
    # /api/categories/<_id>/
    def get(self, _id):
        category = Category.get_by_id(_id)
        return jsonify(category=category.to_json())

    def delete(self, _id):
        Category.delete_by_id(_id)
        return jsonify("category deleted")

    @validate_categories_route_handler
    def patch(self, _id):
        request_body = request.get_json()
        category = Category.get_by_id(_id)
        category.name = request_body.get('name', category.name)
        category.update()
        return jsonify(category=category.to_json())