from ...core.own.image import remove_image as core_remove_image
from ...core.typing.primitives import ImagePath as CoreImagePath
from ...rest.typing.status import Status as RestStatus


def remove_image(image_path: str) -> RestStatus:
    core_path = CoreImagePath(image_path)
    result = core_remove_image(core_path)
    return RestStatus(status=result.status, message=result.message)
