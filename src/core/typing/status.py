class Status:
    def __init__(self, status: str, message: str, error: str = "", data: dict = None):
        self.status = status
        self.message = message
        self.error = error
        self.data = data or {}

    def __bool__(self):
        return self.status == "success"
