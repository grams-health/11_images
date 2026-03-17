# Image Service API Contract

**Port**: 6031

## Health Check

```
GET /
→ 200 {"status": "healthy", "service": "images"}
```

## Upload Image

```
POST /images
Content-Type: multipart/form-data

Fields:
  file: <binary>        (required) .jpg, .jpeg, .png, .gif, .webp
  prefix: <string>      (optional) e.g. "foods", "implements"

→ 201 {"status": "success", "message": "Image uploaded", "image_path": "foods/test.jpg"}
→ 400 {"status": "error", "message": "...", "image_path": ""}
```

## Serve Image

```
GET /images/<path:image_path>

→ 200 (binary image data with appropriate Content-Type)
→ 404 {"status": "error", "message": "Image not found"}
```

## Remove Image

```
DELETE /images/<path:image_path>

→ 200 {"status": "success", "message": "Image removed"}
→ 404 {"status": "error", "message": "..."}
```

## Security

- Allowed extensions: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
- Filenames sanitized via `werkzeug.utils.secure_filename`
- Path traversal prevented via `os.path.realpath()` check
- Overwrites existing files on re-upload (no conflict errors)
