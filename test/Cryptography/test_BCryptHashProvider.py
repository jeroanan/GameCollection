"""Unit tests for BCryptHashProvider."""

import unittest
from Cryptography.bcrypt_hash_provider import BCryptHashProvider
from Cryptography.hash_provider import HashProvider

class TestBCryptHashProvider(unittest.TestCase):
    """Unit tests for BCryptHashProvider."""

    def test_is_hash_provider(self):
        """BCryptHashProvider is a HashProvider."""
        target = BCryptHashProvider()
        self.assertIsInstance(target, HashProvider)
