client = pymongo.MongoClient(
    Config.CONNECTION_STRING,
    server_api=ServerApi('1'))
db = client.e_commerce