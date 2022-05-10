from flask.views import MethodView
from flask import request, jsonify
from models import Publication
from validators.validation_publications import validate_add_publication
from flask_jwt_extended import jwt_required, get_jwt


# /api/products
@validate_products_route_handler
def products_route_handler():
    pass
    # tämä routehandler vastaa request methodeihin GET ja POST
    # getillä haet kaikki tuotteet kategoriasta riippumatta
    # post lisää uuden tuotteen

    # huomaa, että tässä käytetään  @validate_products_route_handler dekoraattoria. Tarkista uutta tuotetta lisättäessä, että request_body sisältää namen ja categoryn


@validate_product_route_handler
def product_route_handler(_id):
# kuten category_route_handlerkin, tämä route_handler vastaa request methodeihin GET, PATCH ja DELETE

# get hakee yksittäisen tuotteen tiedot
# patch muokkaa yksittäisen tuotteen tietoja
# delete poistaa yksittäisen tuotteen

# huom. käytä patchissa @validate_product_route_handleria tarkistamaan että muokkauksessa requst_body sisältää namen ja categoryn


