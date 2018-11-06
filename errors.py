class ValidationError(Exception):
    def __init__(self, message, validator):
        super(ValidationError, self).__init__(message)
        self.validator = validator

class CSVHandlerError(Exception):
    pass