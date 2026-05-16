"""Persistence Exception definitions"""
class GameNotFoundException(Exception):
    """Exception raised when a game is not found in the database.
    """

class HardwareNotFoundException(Exception):
    """Exception raised when a hardware item is not found in the database.
    """

class UnrecognisedFieldNameException(Exception):
    """Exception raised when an unrecognised field name is encountered.
    """
