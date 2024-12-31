# Custom Exception Class
class NotFoundException(Exception):
    def __init__(self, message="Not found"):
        self.message = message
        super().__init__(self.message)
