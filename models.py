from json import JSONEncoder
from img_base64 import image_to_base64

class Image:
    def __init__(self, path):
        self.attachment = image_to_base64(path)

class Option:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def __json__(self):
        return self.__dict__
    
class Variant:
    def __init__(self, title, price, option1 = None, option2 = None, option3 = None):
        self.title = title
        self.price = price
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3

class Product:
    def __init__(self, title: str, variants : list[Variant], options : list[Option], images: list[Image]):
        self.title = title
        self.body_html ="<p data-mce-fragment=\"1\">Introducing our premium T-shirt - the epitome of comfort and style. Crafted with the finest materials and meticulous attention to detail, this T-shirt is designed to elevate your wardrobe.</p>\n<p data-mce-fragment=\"1\"><strong data-mce-fragment=\"1\">Key Features:</strong></p>\n<ul data-mce-fragment=\"1\">\n<li data-mce-fragment=\"1\">\n<strong data-mce-fragment=\"1\">Supreme Comfort:</strong> Our T-shirt is made from ultra-soft, breathable fabric that feels heavenly against your skin. It's perfect for all-day wear.</li>\n<li data-mce-fragment=\"1\">\n<strong data-mce-fragment=\"1\">Classic Design:</strong> The timeless design of our T-shirt ensures it's a versatile addition to your closet. Pair it with jeans, shorts, or layer it under a jacket for a stylish look.</li>\n<li data-mce-fragment=\"1\">\n<strong data-mce-fragment=\"1\">Exceptional Durability:</strong> We've reinforced the stitching to ensure your T-shirt stands the test of time, even after numerous washes.</li>\n<li data-mce-fragment=\"1\">\n<strong data-mce-fragment=\"1\">Variety of Colors:</strong> Choose from a range of classic and vibrant colors to suit your personal style.</li>\n</ul>\n<p data-mce-fragment=\"1\">Whether you're lounging at home or heading out for a night on the town, this T-shirt is your go-to choice. It's a wardrobe essential that combines comfort, quality, and style effortlessly.</p>\n<p data-mce-fragment=\"1\">Elevate your casual wardrobe with our premium T-shirt. Add it to your cart now and experience the ultimate in comfort and style.</p>"
        self.vendor = "Footballgy"
        self.variants = variants
        self.options = options
        self.images = images

    def toJSON(self) -> str:
        dict =  {
            "product": {
                "title": self.title,
                "body_html": self.body_html,
                "vendor": self.vendor,
                "product_type": "T-Shirt",
                "variants": [vars(variant) for variant in self.variants],
                "options": [vars(option) for option in self.options],
                "images": [vars(image) for image in self.images]
            }
        }

        return JSONEncoder().encode(dict)

