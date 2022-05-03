
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__pass_hasher(password)

    def __str__(self):
        stringed = f"{self.username}, {self.email}, {self.password}"
        return stringed

    def __pass_hasher(self, password):
        hashed = hash(password) % len(self.username)

        return hashed

    def get_user(self):
        return self.username, self.email, self.password
