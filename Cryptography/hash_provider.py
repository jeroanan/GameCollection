"""Hash provider interface."""

class HashProvider:
    """Hash provider interface."""

    def hash_text(self, text: str) -> str:
        """Hash the given text."""
        raise NotImplementedError

    def verify_password(self, entered_password: str, hashed_password: str) -> bool:
        """Verify the entered password against the hashed password."""
        raise NotImplementedError
