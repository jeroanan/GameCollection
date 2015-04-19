from User import User

class ResultToUserMapper(object):
    
    def map(self, result):
        if result is None:
            return User()

        u = User()
        u.id = result.get("_id", "")
        u.user_id = result.get("_User__user_id", "")
        u.password = result.get("_User__password", "")
        return u
