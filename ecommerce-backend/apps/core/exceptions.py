class NotFoundException(Exception):
    pass

class ValidationException(Exception):
    pass

class AuthenticationException(Exception):
    pass

class AuthorizationException(Exception):
    pass

class DatabaseException(Exception):
    pass

class ServiceUnavailableException(Exception):
    pass