from ...core.own.image import upload_image as core_upload_image
from ...core.typing.primitives import Prefix as CorePrefix
from ...rest.typing.upload_result import UploadResult


def upload_image(file_storage, prefix: str) -> UploadResult:
    core_prefix = CorePrefix(prefix)
    result = core_upload_image(file_storage, core_prefix)
    image_path = result.data.get("image_path", "") if result else ""
    return UploadResult(status=result.status, message=result.message, image_path=image_path)
