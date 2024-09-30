import json
import base64
from schemas import Product
from db.json_driver import JsonDriver
from cache_db.product_cache import ProductCache

class ProductRepo:
    def __init__(self, db: JsonDriver, product: Product, saved: bool = False):
        self._db = db
        self.data = product
        self._id = base64.b64encode(product.title.encode()).decode()
        self.saved = saved

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val: str):
        self._id = base64.b64encode(val.encode())

    def save(self, cache: ProductCache) -> bool:
        if cache.get_item():
            print("item {title} already cached".format(title=self.data.title))
            # skipping if not expired from cache
            return False
        else:
            print("item {title} saved with id {id}".format(title=self.data.title, id=self.id))
            self._db.set(self.id, json.loads(self.data.model_dump_json()))
            self.saved = True
            return self.saved
