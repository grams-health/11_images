import os

from werkzeug.utils import secure_filename

from ....core.typing.primitives import ImagePath, Prefix
from ....core.typing.status import Status
from . import config


def upload_image(file_storage, prefix: Prefix) -> Status:
    assert isinstance(prefix, Prefix)

    if not file_storage or not file_storage.filename:
        return Status("error", "No file provided")

    filename = secure_filename(file_storage.filename)
    if not filename:
        return Status("error", "Invalid filename")

    ext = os.path.splitext(filename)[1].lower()
    if ext not in config.ALLOWED_EXTENSIONS:
        return Status("error", f"File type {ext} not allowed")

    if str(prefix):
        target_dir = os.path.join(config.IMAGES_DIR, str(prefix))
    else:
        target_dir = config.IMAGES_DIR

    os.makedirs(target_dir, exist_ok=True)

    file_path = os.path.join(target_dir, filename)
    file_storage.save(file_path)

    if str(prefix):
        image_path = f"{prefix}/{filename}"
    else:
        image_path = filename

    return Status("success", "Image uploaded", data={"image_path": image_path})
