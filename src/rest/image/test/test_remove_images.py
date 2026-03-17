import os
from io import BytesIO


def test_remove_existing_image(client, setup_images_dir):
    data = {"file": (BytesIO(b"image content"), "test.jpg"), "prefix": "foods"}
    client.post("/images", data=data, content_type="multipart/form-data")

    response = client.delete("/images/foods/test.jpg")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == "success"
    assert not os.path.isfile(os.path.join(str(setup_images_dir), "foods", "test.jpg"))


def test_remove_nonexistent_image(client, setup_images_dir):
    response = client.delete("/images/foods/nope.jpg")
    assert response.status_code == 404
    body = response.get_json()
    assert body["status"] == "error"
