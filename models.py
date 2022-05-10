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
    def __init__(self, name, cateogory, _id=None):
        # name on tuotteen nimi, tieto on pakollinen
        # category on sen kategorian _id-kentän arvo, johon kyseinen tuote kuuluu. Tieto on pakollinen, eli jokaisen tuotteen täytyy kuulua kateogoriaan
        # _id on tuotteen oma _id, tieto ei ole pakollinen, koska se saadaan vasta create-metodissa sen jälkeen, kun uusi tuote on tallennettu tietokantaan

        if _id is not None:
            _id = str(_id)
        self._id = _id
        self.name = name
        self.category = str(category)

    # luo tähän CRUD:n mukaiset metodit, kuten modeliin kuuluu

    def create(self):
        pass
        # lisää tähän koodi, jolla tallennat tuotteen tietokantaan (katso mallia toisesta projektista)

    @staticmethod
    def get_by_id(_id):
        pass
        # lisää tähän koodi, joka hakee _id:n perusteella yhden tuotteen ja palauttaa sen
        # jos tuotetta ei löydy, heitä NotFoud exception

    @staticmethod
    def get_all():
        pass
        # lisää tähän koodi. joka hakee kaikki tuotteet. Luuppaa ne läpi ja lisää listaan Product-tietotyypin muuttujia. Palauta lista sen jälkeen

    def update(self):
        pass
        # lisää tähän koodi, joka päivittää tuotteen nimen ja kateogorian

    def delete(self):
        pass
        # lisää tähän koodi, joka poistaa tuotteen

    def to_json(self):
        pass
        # lisää tähän koodi, joka palauttaa yksittäisen tuotteen tiedot dictionaryna (jotta jsonify osaa palauttaa tuotteen tiedot jsonina)

    @staticmethod
    def list_to_json(products):
# lisää tähän koodi, joka luuppaa kaikki products-listan tuotteet läpi ja kutsuu jokaisen yksittäisen tuotteen kohdalla yo. to_json-metodia. Lisää to_jsonin tulos listaan ja palauta lista


class Category:
    def __init__(self, name, _id=None):
        if _id is not None:
            _id = str(_id)
        self._id = _id
        self.name = name

        # name on kategorian nimi. Tieto on pakollinen
        # _id on kateogorian _id MongoDB-tietokannassa

    def create(self):

    # kutsu tässä ennen lisäystä
    # _is_unique-metodia, jolla tarkistat, onko self.name:n arvolla lähetetty

    # unique = self._is_unique()

    # jos unique on True, voit jatkaa uuden kategorian tallentamista
    # jos unique on False, heitä tästä omatekoinen ValidationError, joka keskeyttää tallennuksen
    # kerro ValidationErrorin messagessa, että kategorian pitää olla uniikki ValidationError(message='Category name must be unique')

    # kirjoita tähän Product-classissa olevat vastaavat CRUD:n metodia kategorioille

    # Product-classista löytyvien metodien lisäksi kirjoita myös ao. metodi

    def get_products(self):

    # kirjoita tähän koodi, joka hakee kaikki tuotteet, joilla category-avaimen arvo on self._id (eli valitun kategorian _id)
    # palauta tuotteet listassa, joka sisältää Product-tietotyypin muuttujia (eli [Product, Product Product...])

    def _is_unique(self):

    # kirjoita lisäksi koodi, joka hakee ensimmäisen (find_one) cateogorian, jonka name on self.namen arvo
    # tätä metodia kutsutaan  create-metodin sisällä tarkistamaan, onko lisättävän kategorian nimi uniikki vai ei
    # jos find_one-funktio palauttaa None, silloin toista samannimistä kategoriaa ei ole olemassa
    # jos find_one-funktio löytää self.namen arvolla kateogorian, silloin uuden kategorian nimi ei ole uniikki (eikä sitä voi lisätä)

    # jos find_one palauttaa None
    # palauta True
    # jos find_one palauttaa Kategorian palauta False

    def delete(self):
# HUOM! Kun poistat kategorian, muista poistaa myös siihen kuuluvat tuotteet ennen kategorian poistoa
# voit käyttää tässä self.find_products-metodia

# luuppaa kaikki find_products-metodin palauttamat tuotteet ja kutsu yksittäiselle productille product.delete-metodia



