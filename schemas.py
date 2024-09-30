from pydantic import BaseModel, HttpUrl
from typing import Optional

class Product(BaseModel):
    title: str
    price: float
    url: HttpUrl

class ScrapeSettings(BaseModel):
    page_count: Optional[int] = 1
    proxy: Optional[str] = None
