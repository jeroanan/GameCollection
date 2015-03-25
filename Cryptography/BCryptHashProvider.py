import bcrypt

from Cryptography.HashProvider import HashProvider


class BCryptHashProvider(HashProvider):

    def hash_text(self, text):
        encrypted = bcrypt.hashpw(text.encode("utf-8"), bcrypt.gensalt())
        return encrypted

    def verify_password(self, entered_password, hashed_password):
        return bcrypt.hashpw(entered_password.encode("utf-8"), hashed_password.encode("utf-8"))