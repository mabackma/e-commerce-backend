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