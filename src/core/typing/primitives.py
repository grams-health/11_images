class ImagePath(str):
    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected str, got {type(value).__name__}")
        if not value.strip():
            raise ValueError("ImagePath cannot be empty")
        return super().__new__(cls, value.strip())


class Prefix(str):
    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError(f"Expected str, got {type(value).__name__}")
        return super().__new__(cls, value.strip())
