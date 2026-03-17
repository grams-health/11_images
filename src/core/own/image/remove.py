import os

from ....core.typing.primitives import ImagePath
from ....core.typing.status import Status
from . import config


def remove_image(image_path: ImagePath) -> Status:
    assert isinstance(image_path, ImagePath)

    full_path = os.path.realpath(os.path.join(config.IMAGES_DIR, str(image_path)))
    images_root = os.path.realpath(config.IMAGES_DIR)

    if not full_path.startswith(images_root + os.sep) and full_path != images_root:
        return Status("error", "Invalid image path")

    if not os.path.isfile(full_path):
        return Status("error", "Image not found")

    os.remove(full_path)
    return Status("success", "Image removed")
