"""Exceptions for interactors."""

class InteractorFactoryNotSetException(Exception):
    """Raised when the interactor factory is not set before use."""

class PersistenceException(Exception):
    """Raised when there is an error related to data persistence."""

class UnrecognisedInteractorTypeException(Exception):
    """Raised when an unrecognised interactor type is requested from the InteractorFactory."""

class UserExistsException(Exception):
    """Raised when a user with the same username already exists in the database."""
