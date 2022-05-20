from flask.views import MethodView
from flask import request, jsonify
from models import Product
from validators.validation_products import validate_product_route_handler

class ProductsRouteHandler(MethodView):

    @validate_product_route_handler
    def post(self):
        request_body = request.get_json()

        name = request_body['name']
        category = request_body['category']
        product = Product(name, category)
        product.create()

        return jsonify(product=product.to_json())

    def get(self):
        products = Product.get_all()

        return jsonify(products=Product.list_to_json(products))

class ProductRouteHandler(MethodView):

    def get(self, _id):
        product = Product.get_by_id(_id)
        return jsonify(product=product.to_json())

    def delete(self, _id):
        product = Product.get_by_id(_id)
        product.delete()
        return jsonify("product deleted")

    @validate_product_route_handler
    def patch(self, _id):
        request_body = request.get_json()
        product = Product.get_by_id(_id)
        product.name = request_body.get('name', product.name)
        product.category = request_body.get('category', product.category)
        product.update()
        return jsonify(product=product.to_json())



