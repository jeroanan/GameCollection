import unittest
from Cryptography.BCryptHashProvider import BCryptHashProvider
from Cryptography.HashProvider import HashProvider


class TestBCryptHashProvider(unittest.TestCase):

    def test_is_hash_provider(self):
        target = BCryptHashProvider()
        self.assertIsInstance(target, HashProvider)

    def test_hash_text(self):
        target = BCryptHashProvider()
        target.hash_text("test")