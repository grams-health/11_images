import pytest
from src.core.own.image import config
from src.app.app import app


@pytest.fixture(autouse=True)
def setup_images_dir(tmp_path):
    original = config.IMAGES_DIR
    config.set_images_dir(str(tmp_path))
    yield tmp_path
    config.set_images_dir(original)


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
