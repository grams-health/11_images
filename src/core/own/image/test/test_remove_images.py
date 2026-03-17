import os
from io import BytesIO
from werkzeug.datastructures import FileStorage

from .....core.typing.primitives import ImagePath, Prefix
from .. import upload_image, remove_image


def _make_file(filename="test.jpg", content=b"fake image data"):
    return FileStorage(stream=BytesIO(content), filename=filename, content_type="image/jpeg")


def test_remove_existing_image(setup_images_dir):
    upload_image(_make_file(), Prefix("foods"))
    result = remove_image(ImagePath("foods/test.jpg"))
    assert result
    assert not os.path.isfile(os.path.join(str(setup_images_dir), "foods", "test.jpg"))


def test_remove_nonexistent_image(setup_images_dir):
    result = remove_image(ImagePath("foods/nope.jpg"))
    assert not result
    assert result.message == "Image not found"


def test_remove_traversal_attack(setup_images_dir):
    result = remove_image(ImagePath("../../etc/passwd"))
    assert not result
    assert result.message == "Invalid image path"
