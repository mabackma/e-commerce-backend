import pymongo
from pymongo.server_api import ServerApi
from config import Config
from bson.objectid import ObjectId
from errors.not_found import NotFound
from errors.validation_error import ValidationError

client = pymongo.MongoClient(
    Config.CONNECTION_STRING,
    server_api=ServerApi('1'))
db = client.e_commerce


class Product:
    def __init__(self, name, category, _id=None):
        if _id is not None:
            _id = str(_id)
        self._id = _id
        self.name = name
        self.category = str(category)

    def create(self):
        result = db.products.insert_one({
            'name': self.name,
            'category': self.category
        })
        self._id = str(result.inserted_id)

    def update(self):
        _filter = {'_id': ObjectId(self._id)}
        _update = {
            '$set': {'name': self.name, 'category': self.category}
        }
        db.products.update_one(_filter, _update)

    # Palauttaa dictionaryn
    def to_json(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'category': self.category
        }

    # Palauttaa jsonin
    @staticmethod
    def list_to_json(product_list):
        products = []
        for product in product_list:
            products.append(product.to_json())
        return products

    @staticmethod
    def get_all():
        products_cursor = db.products.find()
        products_list = list(products_cursor)
        products = []
        for product in products_list:
            product_object = Product(product['name'], product['category'], _id=product['_id'])
            products.append(product_object)
        return products

    @staticmethod
    def get_by_id(_id):
        product_dictionary = db.products.find_one({'_id': ObjectId(_id)})
        if product_dictionary is None:
            raise NotFound(message="product not found.")
        product = Product(product_dictionary['name'], product_dictionary['category'], _id=product_dictionary['_id'])
        return product
        # jos tuotetta ei löydy, heitä NotFoud exception

    def delete(self):
        result = db.products.delete_one({'_id': ObjectId(self._id)})
        if result.deleted_count == 0:
            raise NotFound(message="product not found")

class Category:
    def __init__(self, name, _id=None):
        if _id is not None:
            _id = str(_id)
        self._id = _id
        self.name = name

    # Luo uuden uniikin kategorian
    def create(self):
        unique = self._is_unique()
        if unique:
            result = db.categories.insert_one({
                'name': self.name
            })
            self._id = str(result.inserted_id)
        else:
            raise ValidationError(message="Category name must be unique!")

    def update(self):
        _filter = {'_id': ObjectId(self._id)}
        _update = {
            '$set': {'name': self.name}
        }
        db.categories.update_one(_filter, _update)

    # Palauttaa dictionaryn
    def to_json(self):
        return {
            '_id': str(self._id),
            'name': self.name
        }

    # Palauttaa jsonin
    @staticmethod
    def list_to_json(category_list):
        categories = []
        for category in category_list:
            categories.append(category.to_json())
        return categories

    @staticmethod
    def get_all():
        categories_cursor = db.categories.find()
        categories_list = list(categories_cursor)
        categories = []
        for category in categories_list:
            category_object = Category(category['name'], _id=category['_id'])
            categories.append(category_object)
        return categories

    @staticmethod
    def get_by_id(_id):
        category_dictionary = db.categories.find_one({'_id': ObjectId(_id)})
        if category_dictionary is None:
            raise NotFound(message="category not found.")
        category = Category(category_dictionary['name'], _id=category_dictionary['_id'])
        return category

    def get_products(self):
        products_cursor = db.products.find({'category': self._id})
        products_list = list(products_cursor)
        products = []
        for product in products_list:
            product_object = Product(product['name'], product['category'], _id=product['_id'])
            products.append(product_object)
        return products

    # Tarkistaa onko saman nimistä kategoriaa jo olemassa
    def _is_unique(self):
        category = db.categories.find_one({'name': self.name})
        if category is not None:
            return False
        return True

    def delete(self):

        # Poistetaan kaikki kategorian tuotteet
        category = Category.get_by_id(self._id)
        products_list = category.get_products()
        for product in products_list:
            product.delete()

        # Poistetaan kategoria
        result = db.categories.delete_one({'_id': ObjectId(self._id)})
        if result.deleted_count == 0:
            raise NotFound(message="category not found")

