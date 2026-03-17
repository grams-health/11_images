from flask import send_file, jsonify

from ...service.image import serve_image


def handle_serve_image(image_path):
    """GET /images/<path:image_path> — serve an image file."""
    full_path = serve_image(image_path)
    if full_path is None:
        return jsonify({"status": "error", "message": "Image not found"}), 404
    return send_file(full_path)
