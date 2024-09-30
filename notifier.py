from repository.product import ProductRepo
from typing import List

class Notifier:
    def __init__(self, mediums=["console"]) -> None:
        self.mediums = mediums
        self.message = (
            "Products Processed: {processed}\n"
            "Products Saved: {saved}\n"
            "Cached Products: {cached}\n"
        )

    def notify(self) -> None:
        for medium in self.mediums:
            if medium == "console":
                self.push_to_console()
            elif medium == "email":
                # email notify
                pass
            else:
                raise NotImplementedError


    def compose(self, products: List[ProductRepo]):
        saved = 0
        processed = len(products)
        saved = sum([int(product.saved) for product in products])

        cached = processed - saved
        self.message = self.message.format(processed = processed, saved = saved, cached = cached)
    
    def push_to_console(self, message=None):
        print(message or self.message)
