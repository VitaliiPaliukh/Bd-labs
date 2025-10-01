class UserDTO:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "password": self.password
        }
