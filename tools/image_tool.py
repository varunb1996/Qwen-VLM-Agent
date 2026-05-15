from PIL import Image

def load_image(image_path):

    image = Image.open(image_path)

    return image


def get_image_metadata(image_path):

    image = Image.open(image_path)

    return {
        "format": image.format,
        "mode": image.mode,
        "size": image.size
    }