from dataclasses import asdict

from flask import jsonify

from ...service.image import remove_image


def handle_remove_image(image_path):
    """DELETE /images/<path:image_path> — remove an image file."""
    result = remove_image(image_path)
    if result.status == "success":
        return jsonify(asdict(result)), 200
    return jsonify(asdict(result)), 404
