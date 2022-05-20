from flask.views import MethodView
from flask import request, jsonify
from models import Category, Product
from validators.validation_categories import validate_add_category

class CategoryProductsRouteHandler(MethodView):

    def get(self, _id):
        category = Category.get_by_id(_id)
        products_list = category.get_products()
        return jsonify(products=Product.list_to_json(products_list))


class CategoriesRouteHandler(MethodView):

 #   @validate_add_category
    def post(self):
        request_body = request.get_json()

        name = request_body['name']
        category = Category(name)
        category.create()

        return jsonify(category=category.to_json())

    def get(self):
        categories = Category.get_all()

        return jsonify(categories=Category.list_to_json(categories))

"""
    # /api/categories/<_id>/products
    def category_products_route_handler(_id):
        pass
        # _id on valitun kateogorian _id 
    
    
        # tee tähän koodi, joka hakee Categories.get_products-metodia käyttäen ainoastaan valitun kategorian tuotteet



    # /api/categories
    @validate_categories_route_handler
    def categories_route_handler():
        pass
        # routehandler vastaa sekä GET että POST request methodeihin.

        # get hakee kaikki kategoriat ja palauttaa ne jsonina Cateogry.get_all()

        # post lisää uuden kategorian

        # huomaa, että lisättäessä kateogorian nimi on pakollinen,
        # huomaa myös, että esimerkissä on käytetty @validate_categories_route_handler-dekoraattoria

        # tämä @validate_categories_route_handler on omatekoinen dekoraattori, jolla tarkistat,
        # että pakolliset tiedot löytyvät request_bodysta.

        # jos name ei ole request_bodyssa, nosta ValidationError,
        # jolla ilmoitat käyttäjälle, että name on pakollinen tieto


    # /api/categories/<_id>

    @validate_category_route_handler
    def category_route_handler(_id):
        pass
        # tämä route handler vastaa request methodeihin: GET. PATCH, DELETE

        # GET hakee _id:n perusteella valitun categorian
        # PATCH muokkaa nimeä
        # DELETTE poistaa valitun kateogorian

        # huomaa custom dekoraattori: @validate_category_route_handler. Käytä tätä patchissa varmistamaan,
        # että name löytyy request_bodysta. Voit toki käyttää samaa dekoraattoria kuin uuden lisäyksessä,
        # koska logiikka on sama
    
"""

class CategoryRouteHandler(MethodView):
    # /api/categories/<_id>/
    def get(self, _id):
        category = Category.get_by_id(_id)
        return jsonify(category=category.to_json())

    def delete(self, _id):
        Category.delete_by_id(_id)
        return jsonify("category deleted")

    def patch(self, _id):
        request_body = request.get_json()
        category = Category.get_by_id(_id)
        category.name = request_body.get('name', category.name)
        category.update()
        return jsonify(category=category.to_json())