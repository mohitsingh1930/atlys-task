import enum

class JobStatus(enum.Enum):
    processing = 1
    idle = 2
    failed = 3

DENTAL_BASE_URL = "https://dentalstall.com/shop/page/"

PRODUCTS_JSON = "db/products.json"

PRODUCT_CACHE_REDIS_KEY = "product_store:{id}"

PRODUCT_CACHE_EXPIRY = 24 * 60 * 60 # 1 day
# PRODUCT_CACHE_EXPIRY = 30 # 30 seconds
