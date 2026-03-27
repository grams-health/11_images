import pytest
from src.core.own.image import config


@pytest.fixture(autouse=True)
def setup_images_dir(tmp_path):
    original = config.IMAGES_DIR
    config.set_images_dir(str(tmp_path))
    yield tmp_path
    config.set_images_dir(original)
