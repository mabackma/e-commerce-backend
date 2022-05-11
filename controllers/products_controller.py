from flask.views import MethodView
from flask import request, jsonify
from models import Product
from validators.validation_products import validate_add_product

class ProductsRouteHandler(MethodView):

    def post(self):
    def get(self):

"""
# /api/products
@validate_products_route_handler
def products_route_handler():
    pass
    # tämä routehandler vastaa request methodeihin GET ja POST
    # getillä haet kaikki tuotteet kategoriasta riippumatta
    # post lisää uuden tuotteen

    # huomaa, että tässä käytetään  @validate_products_route_handler dekoraattoria. Tarkista uutta tuotetta lisättäessä, että request_body sisältää namen ja categoryn
"""

class ProductsRouteHandler(MethodView):

    def get(self, _id):
        pass

    def delete(self, _id):
        pass

    def patch(self, _id):
        pass

    def put(self, _id):
        pass

""" 
@validate_product_route_handler
def product_route_handler(_id):
# kuten category_route_handlerkin, tämä route_handler vastaa request methodeihin GET, PATCH ja DELETE

# get hakee yksittäisen tuotteen tiedot
# patch muokkaa yksittäisen tuotteen tietoja
# delete poistaa yksittäisen tuotteen

# huom. käytä patchissa @validate_product_route_handleria tarkistamaan että muokkauksessa requst_body sisältää namen ja categoryn
"""
