class InputNotValidException(Exception):
    def __init__(self, message="Input not valid"):
        self.message = message
        super().__init__(self.message)
