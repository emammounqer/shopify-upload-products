from json import JSONEncoder
import requests
from img_base64 import image_to_base64
from dotenv import dotenv_values

def post_shopify_products(jsonData, shop, access_token):
    url = f"https://{shop}.myshopify.com/admin/api/2024-04/products.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": access_token
    }

    response = requests.post(url, data= jsonData, headers=headers)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

if __name__ == "__main__":
    # Replace placeholders with actual values
    config = dotenv_values(".env")

    shop = config["SHOP_NAME"]
    access_token = config["ACCESS_TOKEN"]

    data = {
        "product": {
            "title": "Burton Custom Freestyle 151",
            "body_html": "<strong>Good snowboard!</strong>",
            "vendor": "Burton",
            "product_type": "Snowboard",
            "status": "draft"
        }
    }

    path = "./example_image/ALL LEGENDS FRONT.png"
    data1 = {
        "product": {
            "title": "Burton Custom Freestyle 151",
            "body_html": "<strong>Good snowboard!</strong>",
            "vendor": "Burton",
            "product_type": "Snowboard",
            "images": [
                {
                    "attachment": image_to_base64(path)
                }
            ]
        }
    }

    data1Json = JSONEncoder().encode(data)

    product = post_shopify_products(data1Json,shop, access_token)
    if product:    
        print(product)