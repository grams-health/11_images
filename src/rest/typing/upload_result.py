from dataclasses import dataclass


@dataclass
class UploadResult:
    status: str
    message: str
    image_path: str
