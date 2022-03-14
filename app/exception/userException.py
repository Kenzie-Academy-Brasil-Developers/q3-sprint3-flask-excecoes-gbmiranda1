
class IsNumericError(Exception):
    def __init__(self, message=None, status_code=400):

        if not message:
            self.message = f"numbers where they should be strings"
        else:
            self.message = message

        self.status_code = status_code

class EmailExistError(Exception):
    def __init__(self, message=None, status_code=409):

        if not message:
            self.message = f"This email already exists"
        else:
            self.message = message

        self.status_code = status_code
