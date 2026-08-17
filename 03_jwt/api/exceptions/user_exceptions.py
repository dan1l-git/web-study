class UserNotFoundError(Exception):
    """Raised when user doesn't exist"""
    pass

class UserAlreadyExistsError(Exception):
    """Raised when user already exists"""
    pass