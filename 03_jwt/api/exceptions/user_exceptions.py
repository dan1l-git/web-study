class UserNotFoundError(Exception):
    """Raised when user doesn't exist"""
    pass

class UserAlreadyExistsError(Exception):
    """Raised when user already exists"""
    pass

class InvalidCredentialsError(Exception):
    """Raised when invalid credentials are provided"""
    pass

class InvalidTokenError(Exception):
    """Raised when token is invalid or expired"""
    pass