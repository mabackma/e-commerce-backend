from flask import Flask, jsonify
from controllers.home_controller import home_route_handler
from controllers.products_controller import ProductsRouteHandler, ProductRouteHandler
from controllers.categories_controller import CategoryProductsRouteHandler, CategoriesRouteHandler, \
    CategoryRouteHandler
from errors.validation_error import ValidationError
from errors.not_found import NotFound

app = Flask(__name__)
app.config.from_object('config.Config')

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
                 methods=["GET", "DELETE", "PATCH"])

app.add_url_rule("/api/categories", view_func=CategoriesRouteHandler.as_view('categories_route_handler'),
                 methods=['GET', 'POST'])
app.add_url_rule("/api/categories/<_id>", view_func=CategoryRouteHandler.as_view('category_route_handler'),
                 methods=["GET", "DELETE", "PATCH"])
app.add_url_rule("/api/categories/<_id>/products",
                 view_func=CategoryProductsRouteHandler.as_view('category_products_route_handler'),
                 methods=["GET", "DELETE", "PATCH"])


app.run(debug=True)



