import os
from io import BytesIO
from werkzeug.datastructures import FileStorage

from src.core.typing.primitives import ImagePath, Prefix
from src.core.own.image import upload_image, serve_image


def _make_file(filename="test.jpg", content=b"fake image data"):
    return FileStorage(stream=BytesIO(content), filename=filename, content_type="image/jpeg")


def test_serve_existing_image(setup_images_dir):
    upload_image(_make_file(), Prefix("foods"))
    result = serve_image(ImagePath("foods/test.jpg"))
    assert result is not None
    assert result.endswith("test.jpg")
    assert os.path.isfile(result)


def test_serve_nonexistent_image(setup_images_dir):
    result = serve_image(ImagePath("foods/nope.jpg"))
    assert result is None


def test_serve_traversal_attack(setup_images_dir):
    result = serve_image(ImagePath("../../etc/passwd"))
    assert result is None
