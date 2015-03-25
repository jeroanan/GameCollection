class User(object):

    def __init__(self):
        self.__user_id = ""
        self.__password = ""

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, val):
        self.__user_id = val

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, val):
        self.__password = val
