"""Hash provider interface."""

class HashProvider(object):
    """Hash provider interface."""

    def hash_text(self, text):
        """Hash the given text."""
        raise NotImplementedError

    def verify_password(self, entered_password, hashed_password):
        """Verify the entered password against the hashed password."""
        raise NotImplementedError
