class DuplicateEmailException(Exception):
    def __init__(self, message="Email is already in use"):
        self.message = message
        super().__init__(self.message)
