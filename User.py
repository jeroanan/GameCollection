class User(object):

    def __init__(self):
        self.__id = ""
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

    @property
    def id(self):
        return self.__id
        
    @id.setter
    def id(self, val):
        self.__id = val        

    def __eq__(self, other):
        return self.user_id==other.user_id
