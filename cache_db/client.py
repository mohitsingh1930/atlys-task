import os
import redis

from settings import get_settings

class Redis:
    CONNECTION = None
    @classmethod
    def get_connection(cls) -> redis:
        if cls.CONNECTION:
            return cls.CONNECTION
        else:
            cls.CONNECTION = redis.Redis(
                host=get_settings().redis_host,
                port=get_settings().redis_port,
                db=get_settings().redis_db,
                password=get_settings().redis_password
            )
            return cls.CONNECTION
