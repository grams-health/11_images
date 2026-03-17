import os

from ....core.typing.primitives import ImagePath
from . import config


def serve_image(image_path: ImagePath) -> str | None:
    assert isinstance(image_path, ImagePath)

    full_path = os.path.realpath(os.path.join(config.IMAGES_DIR, str(image_path)))
    images_root = os.path.realpath(config.IMAGES_DIR)

    if not full_path.startswith(images_root + os.sep) and full_path != images_root:
        return None

    if not os.path.isfile(full_path):
        return None

    return full_path
