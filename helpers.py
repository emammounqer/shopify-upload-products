import os
import pprint

def get_all_png_paths_in_folder(folder_path):
    """
    Get all the paths of the PNG files in the folder
    """
    png_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".png"):
                png_paths.append(os.path.join(root, file))
    return png_paths
    
def remove_after_words(input_string, target_words):
    index = min(input_string.find(word) for word in target_words if word in input_string)

    if index != -1:
        return input_string[:index]

    return input_string

def get_img_dict(folder_path):
    words_set = ["FOLDED", "FRONT"]
    all_img_paths = get_all_png_paths_in_folder(folder_path)
    img_dict = {}

    for path in all_img_paths:
        base_name = os.path.basename(path)
        name = remove_after_words(base_name, words_set).strip()

        img_dict_value = img_dict.get(name, [])
        img_dict[name] = [*img_dict_value, path]
    return img_dict


# pprint.pprint(get_img_dict("./example_image"))