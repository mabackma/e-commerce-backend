from flask import request
from errors.validation_error import ValidationError

def validate_add_category(categories_route_handler):
    def validate_add_category_wrapper(*args, **kwargs):
        request_body = request.get_json()
        if "name" in request_body:
            return categories_route_handler(*args, **kwargs)
        raise ValidationError(message="name is required")
    return validate_add_category_wrapper()
