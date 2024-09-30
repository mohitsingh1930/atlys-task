from bs4 import BeautifulSoup
from typing import List
from scraper import DentalStallScraper, download_html
from schemas import ScrapeSettings
from cache_db.product_cache import ProductCache
from db.json_driver import JsonDriver
from repository.product import ProductRepo
from notifier import Notifier
from constants import JobStatus, DENTAL_BASE_URL, PRODUCTS_JSON

# Responsible for scrape all pages as provided in settings
class ScrapingManager:
    processing: bool = False

    @classmethod
    def get_status(cls):
        if cls.processing:
            return JobStatus.processing
        else:
            return JobStatus.idle
        
    def __init__(self, settings: ScrapeSettings) -> None:
        self.page_count = settings.page_count
        self.proxy = settings.proxy
        self._products: List[ProductRepo] = []
        self._db = JsonDriver(PRODUCTS_JSON)
        self._notifier = Notifier(["console"])

    def run(self):
        # run scraper for all pages
        self._process_pages()
        # add retry mechanism if http request fails
        ScrapingManager.processing = True
        # stores all data once collected
        self._save_products()
        # Notify when data is processed and when the data failed to generated due to http failures
        self._send_notification()
        ScrapingManager.processing = False

    def _process_pages(self) -> None:
        for i in range(self.page_count):
            url = DENTAL_BASE_URL + str(i+1)
            print(url)
            page = download_html(url)
            if isinstance(page, BeautifulSoup):
                product_models = DentalStallScraper(page).extract_product_data()
                self._products += [ProductRepo(self._db, product=p) for p in product_models]
            else:
                # add retry mechanism here
                pass

    def _save_products(self) -> None:
        for product in self._products:
            cache = ProductCache(product.id)
            if product.save(cache):
                cache.store_item()

    def _send_notification(self) -> None:
        notifier = Notifier()
        notifier.compose(self._products)
        notifier.notify()