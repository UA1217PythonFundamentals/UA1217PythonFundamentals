class User:
    max_id = -1
    def __init__(self, pk, username, email, password):
        if self.max_id < pk:
            self.__class__.max_id = pk
        self.pk = pk
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "user_id": self.pk,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
    @classmethod
    def create(cls, username, email, password):
        return User(cls.max_id+1, username, email, password)
        

    

USERS = [
    User(1, "user1", "user1@example.com", "password1"),
    User(2, "user2", "user2@example.com", "password2"),
    User(3, "user3", "user3@example.com", "password3"),
    User(4, "user4", "user4@example.com", "password4"),
    User(5, "user5", "user5@example.com", "password5"),
    User(6, "user6", "user6@example.com", "password6"),
    User(7, "user7", "user7@example.com", "password7"),
    User(8, "user8", "user8@example.com", "password8"),
    User(9, "user9", "user9@example.com", "password9"),
    User(10, "user10", "user10@example.com", "password10")
]