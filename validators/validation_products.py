from flask import request
from errors.validation_error import ValidationError

def validate_product_route_handler(products_route_handler):
    def validate_product_route_handler_wrapper(*args, **kwargs):
        request_body = request.get_json()
        if "name" in request_body and "category" in request_body:
            return products_route_handler(*args, **kwargs)
        raise ValidationError(message="name and category are required")
    return validate_product_route_handler_wrapper

