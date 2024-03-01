from ConcreteUser import ConcreteUser


class SocialNetwork:
    __instance = None

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        # Checks if name already set/created
        if not hasattr(self, 'name'):
            self.name = name
            print("The social network " + self.name + " was created!")
        self.users = []

    def __str__(self):
        print(f"{self.name} social network:")
        for user in self.users:
            print(user)
        return ""

    def sign_up(self, username, password):
        for member in self.users:
            if member.username == username:
                raise Exception
        if len(password) < 4 or len(password) > 8:
            raise Exception

        member = ConcreteUser(username, password)
        self.users.append(member)
        return member

    def log_out(self, username):
        for member in self.users:
            if member.username == username:
                member.isonline = False
                print(f"{member.username} disconnected")

    def log_in(self, username, password):
        for member in self.users:
            if member.username == username and member.password == password:
                member.isonline = True
                print(f"{member.username} connected")
