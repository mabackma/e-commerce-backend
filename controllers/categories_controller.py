from flask.views import MethodView
from flask import request, jsonify
from models import Publication
from validators.validation_publications import validate_add_publication
from flask_jwt_extended import jwt_required, get_jwt

class CategoriesRouteHandler(MethodView):

    def post(self):
    def get(self):

"""
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
    # /api/categories/<_id>/products
    def get(self, _id):
        pass
        # _id on valitun kateogorian _id
        # voit vaihtoehtoisesti käyttää route_handlerina funktion sijasta MethodView-perivää classia
        # classin käytöstä saat lisäpisteitä

        # tee tähän koodi, joka hakee Categories.get_products-metodia käyttäen ainoastaan valitun kategorian tuotteet
    def delete(self, _id):
        pass

    def patch(self, _id):
        pass

    def put(self, _id):
        pass