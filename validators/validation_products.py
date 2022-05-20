from flask import request
from errors.validation_error import ValidationError

def validate_add_product(products_route_handler):
    def validate_add_product_wrapper(*args, **kwargs):
        request_body = request.get_json()
        if "name" in request_body and "category" in request_body:
            return products_route_handler(*args, **kwargs)
        raise ValidationError(message="name and category are required")
    return validate_add_product_wrapper()

def validate_patch_product(product_route_handler):
    def validate_patch_product_wrapper(*args, **kwargs):
        request_body = request.get_json()
        if "name" in request_body and "category" in request_body:
            return product_route_handler(*args, **kwargs)
        raise ValidationError(message="name and category are required")
    return validate_patch_product_wrapper()