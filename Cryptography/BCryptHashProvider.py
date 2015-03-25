import bcrypt

from Cryptography.HashProvider import HashProvider


class BCryptHashProvider(HashProvider):

    def hash_text(self, text):
        salt = bcrypt.gensalt()
        encrypted = bcrypt.hashpw(text.encode("utf-8"), salt)
        return encrypted