class HashProvider(object):

    def hash_text(self, text):
        raise NotImplementedError

    def verify_password(self, entered_password, hashed_password):
        raise NotImplementedError
