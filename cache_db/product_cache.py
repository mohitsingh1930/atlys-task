from .client import Redis
from constants import PRODUCT_CACHE_REDIS_KEY, PRODUCT_CACHE_EXPIRY

class ProductCache:
    def __init__(self, product_id: str) -> None:
        self.conn = Redis.get_connection()
        self.redis_key = self.__redis_key(product_id)

    def store_item(self) -> bool:
        print("storing item at {redis_key}".format(redis_key=self.redis_key))
        self.conn.set(self.redis_key, 1, PRODUCT_CACHE_EXPIRY)

    def get_item(self) -> bool:
        return self.conn.get(self.redis_key)

    def __redis_key(self, id: str) -> str:
        return PRODUCT_CACHE_REDIS_KEY.format(id = id)
