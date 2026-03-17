from io import BytesIO


def test_serve_existing_image(client, setup_images_dir):
    data = {"file": (BytesIO(b"image content"), "test.jpg"), "prefix": "foods"}
    client.post("/images", data=data, content_type="multipart/form-data")

    response = client.get("/images/foods/test.jpg")
    assert response.status_code == 200
    assert response.data == b"image content"


def test_serve_nonexistent_image(client, setup_images_dir):
    response = client.get("/images/foods/nope.jpg")
    assert response.status_code == 404
    body = response.get_json()
    assert body["status"] == "error"


def test_serve_traversal_attack(client, setup_images_dir):
    response = client.get("/images/../../etc/passwd")
    assert response.status_code == 404


def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_json()
    assert body["status"] == "healthy"
