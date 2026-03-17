from dataclasses import asdict

from flask import request, jsonify

from ...rest.typing.upload_result import UploadResult
from ...service.image import upload_image


def handle_upload_image():
    """POST /images — upload an image file."""
    if "file" not in request.files:
        return jsonify(asdict(UploadResult("error", "No file provided", ""))), 400

    file = request.files["file"]
    prefix = request.form.get("prefix", "")

    result = upload_image(file, prefix)
    if result.status == "success":
        return jsonify(asdict(result)), 201
    return jsonify(asdict(result)), 400
