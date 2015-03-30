import bcrypt

from Cryptography.HashProvider import HashProvider


class BCryptHashProvider(HashProvider):

    def hash_text(self, text):
        encrypted = bcrypt.hashpw(text.encode("utf-8"), bcrypt.gensalt())
        print("text: " + text)
        print("encrypted: " + str(encrypted))
        return encrypted

    def verify_password(self, entered_password, hashed_password):        
        print("Entered: " + str(entered_password))
        print("hashed: " + str(hashed_password))
        this_hashed = bcrypt.hashpw(entered_password.encode("utf-8"), hashed_password)        
        return this_hashed == hashed_password
