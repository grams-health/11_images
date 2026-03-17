import os

from flask import Flask, jsonify

app = Flask(__name__)

from ..core.own.image import config
os.makedirs(config.IMAGES_DIR, exist_ok=True)

from ..rest.image import handle_upload_image, handle_serve_image, handle_remove_image


@app.route("/")
def health_check():
    return jsonify({"status": "healthy", "service": "images"})


app.add_url_rule("/images", "upload_image", handle_upload_image, methods=["POST"])
app.add_url_rule("/images/<path:image_path>", "serve_image", handle_serve_image, methods=["GET"])
app.add_url_rule("/images/<path:image_path>", "remove_image", handle_remove_image, methods=["DELETE"])
