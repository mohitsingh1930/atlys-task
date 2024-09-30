from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from typing import List

from schemas import Product

class DentalStallScraper:
    def __init__(self, page: BeautifulSoup):
        self.page = page
        self.products: List[Product] = []

    def extract_product_data(self) -> List[Product]:
        product_divs = self.page.find_all('div', class_='product-inner')
        for div in product_divs:
            title = div.find('h2', class_='woo-loop-product__title').a.string
            price = div.find('span', class_='woocommerce-Price-amount').bdi.contents[1]
            image_url = div.find('img', class_='attachment-woocommerce_thumbnail')['data-lazy-src']

            self.products.append(Product(title=title, price=price, url=image_url))

        return self.products


def download_html(url) -> BeautifulSoup:
    try:
        response = urlopen(url)
        html = response.read().decode('utf-8')

        return BeautifulSoup(html, 'html.parser')
    except HTTPError as e:
        return e

