import os
from io import BytesIO
from werkzeug.datastructures import FileStorage

from .....core.typing.primitives import Prefix
from .. import upload_image


def _make_file(filename="test.jpg", content=b"fake image data"):
    return FileStorage(stream=BytesIO(content), filename=filename, content_type="image/jpeg")


def test_upload_image_success(setup_images_dir):
    result = upload_image(_make_file(), Prefix("foods"))
    assert result
    assert result.data["image_path"] == "foods/test.jpg"
    assert os.path.isfile(os.path.join(str(setup_images_dir), "foods", "test.jpg"))


def test_upload_image_no_prefix(setup_images_dir):
    result = upload_image(_make_file(), Prefix(""))
    assert result
    assert result.data["image_path"] == "test.jpg"
    assert os.path.isfile(os.path.join(str(setup_images_dir), "test.jpg"))


def test_upload_image_invalid_extension(setup_images_dir):
    result = upload_image(_make_file("test.exe"), Prefix("foods"))
    assert not result
    assert result.message == "File type .exe not allowed"


def test_upload_image_no_file(setup_images_dir):
    result = upload_image(None, Prefix("foods"))
    assert not result
    assert result.message == "No file provided"


def test_upload_image_empty_filename(setup_images_dir):
    f = FileStorage(stream=BytesIO(b"data"), filename="", content_type="image/jpeg")
    result = upload_image(f, Prefix("foods"))
    assert not result


def test_upload_image_overwrite(setup_images_dir):
    upload_image(_make_file(content=b"first"), Prefix("foods"))
    result = upload_image(_make_file(content=b"second"), Prefix("foods"))
    assert result
    path = os.path.join(str(setup_images_dir), "foods", "test.jpg")
    with open(path, "rb") as f:
        assert f.read() == b"second"


def test_upload_allowed_extensions(setup_images_dir):
    for ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
        result = upload_image(_make_file(f"img{ext}"), Prefix(""))
        assert result, f"Extension {ext} should be allowed"
