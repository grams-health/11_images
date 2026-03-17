import os
from io import BytesIO


def test_upload_image_success(client, setup_images_dir):
    data = {"file": (BytesIO(b"fake image"), "test.jpg"), "prefix": "foods"}
    response = client.post("/images", data=data, content_type="multipart/form-data")
    assert response.status_code == 201
    body = response.get_json()
    assert body["status"] == "success"
    assert body["image_path"] == "foods/test.jpg"
    assert os.path.isfile(os.path.join(str(setup_images_dir), "foods", "test.jpg"))


def test_upload_image_no_prefix(client, setup_images_dir):
    data = {"file": (BytesIO(b"fake image"), "test.png")}
    response = client.post("/images", data=data, content_type="multipart/form-data")
    assert response.status_code == 201
    body = response.get_json()
    assert body["image_path"] == "test.png"


def test_upload_image_no_file(client, setup_images_dir):
    response = client.post("/images", data={}, content_type="multipart/form-data")
    assert response.status_code == 400
    body = response.get_json()
    assert body["status"] == "error"


def test_upload_image_invalid_extension(client, setup_images_dir):
    data = {"file": (BytesIO(b"fake"), "test.exe"), "prefix": "foods"}
    response = client.post("/images", data=data, content_type="multipart/form-data")
    assert response.status_code == 400
    body = response.get_json()
    assert body["status"] == "error"
