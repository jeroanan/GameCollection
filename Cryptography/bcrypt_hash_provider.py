"""
Provides functionality for making BCrypt hashes, and comparing them.
"""
import bcrypt

from Cryptography.hash_provider import HashProvider


class BCryptHashProvider(HashProvider):
    """
    Provides functionality for making BCrypt hashes, and comparing them.
    """

    def hash_text(self, text):
        """Hashes the given text using BCrypt."""
        encrypted = bcrypt.hashpw(text.encode("utf-8"), bcrypt.gensalt())
        return encrypted

    def verify_password(self, entered_password, hashed_password):
        """Verifies that the entered password matches the hashed password."""
        this_hashed = bcrypt.hashpw(entered_password.encode("utf-8"), hashed_password)
        return this_hashed == hashed_password
