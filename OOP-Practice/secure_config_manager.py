# Secure Config Manager

class DBConfig:
    def __init__(self, host, user):
        self.host = host
        self.user = user
        self._password = None

    @property
    def password(self):
        return self._password[:2] + "*" * (len(self._password) - 2)

    @password.setter
    def password(self, new_pass):
        if len(new_pass) < 8:
            raise ValueError("Password too short!")
        self._password = new_pass

    def __str__(self):
        return f"DB Config [Host: {self.host}, User: {self.user}]"

my_db = DBConfig("localhost", "admin")

print(my_db)
my_db.password = "12345789AAA"
print(my_db.password)