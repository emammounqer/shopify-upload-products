import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")
    

# path = "./example_image/ALL LEGENDS FRONT.png"
# with open('img', "w") as file:
#     decoded = image_to_base64(path)
#     file.write(decoded)