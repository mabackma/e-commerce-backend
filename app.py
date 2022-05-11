from flask import Flask, jsonify
from controllers.auth_controller import RegisterRouteHandler, LoginRouteHandler
from controllers.home_controller import home_route_handler
from controllers.publications_controller import PublicationsRouteHandler, PublicationRouteHandler
from controllers.users_controller import UsersRouteHandler, UserRouteHandler
from errors.validation_error import ValidationError
from errors.not_found import NotFound
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config.Config')
jwt = JWTManager(app)

@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err=err.args), 400

@app.errorhandler(NotFound)
def handle_not_found_error(err):
    return jsonify(err=err.args), 404

app.add_url_rule("/", view_func=home_route_handler)

app.add_url_rule("/api/products", view_func=ProductsRouteHandler.as_view('products_route_handler'),
                 methods=['GET', 'POST'])
app.add_url_rule("/api/products/<_id>", view_func=ProductRouteHandler.as_view('product_route_handler'),
                 methods=["GET", "DELETE", "PATCH", "PUT"])

app.add_url_rule("/api/categories", view_func=CategoriesRouteHandler.as_view('categories_route_handler'),
                 methods=['GET', 'POST'])
app.add_url_rule("/api/categories/<_id>", view_func=CategoryRouteHandler.as_view('category_route_handler'),
                 methods=["GET", "DELETE", "PATCH", "PUT"])

app.run(debug=True)