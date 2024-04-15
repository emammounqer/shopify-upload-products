from models import Image, Option, Product, Variant
from post_product import post_shopify_products
from helpers import get_img_dict
from dotenv import dotenv_values

config = dotenv_values(".env")

shop = config["SHOP_NAME"]
access_token = config["ACCESS_TOKEN"]

def main():
    name_img_map =  get_img_dict("./new_image")
    errors = []

    print()
    print("===============Starting================")
    print()

    for name, img_paths in name_img_map.items():
        options = [Option("Size", ["S", "M", "L", "XL", "XXL"])]
        variants = [
            Variant("S", 19.99, "S"),
            Variant("M", 19.99, "M"),
            Variant("L", 19.99, "L"),
            Variant("XL", 19.99, "XL"),
            Variant("XXl", 19.99, "XXL"),
        ]
        images = [Image(img_path) for img_path in img_paths]
        product = Product(name, variants, options, images)

        # print(product.toJSON())
        resp = post_shopify_products(product.toJSON(), shop, access_token)

        print()
        print("====================================")
        print()

        if resp:
            print(f"Product {name} added successfully")
        else:
            print(f"Error adding {name}")
            errors.append(name)

    print()
    print("===============Finished================")
    print()

    if errors:
        print("Errors:")
        for error in errors:
            print(error)

if __name__ == "__main__":
    main()