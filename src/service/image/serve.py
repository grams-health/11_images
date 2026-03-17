from ...core.own.image import serve_image as core_serve_image
from ...core.typing.primitives import ImagePath as CoreImagePath


def serve_image(image_path: str) -> str | None:
    core_path = CoreImagePath(image_path)
    return core_serve_image(core_path)
