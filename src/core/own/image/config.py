import os

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "images")
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}


def set_images_dir(path: str):
    global IMAGES_DIR
    IMAGES_DIR = path
