from ConcreteUser import ConcreteUser


class SocialNetwork:
    __instance = None

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.users = []
        self.name = name
        print("The social network " + self.name + " was created!")

    def __str__(self):
        result = f"{self.name} social network:"
        for member in self.users:
            result += f"\nUser name: {member.username}, Number of posts: {member.number_of_posts}, Number of followers: {member.number_of_followers}"
        return result

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

    def log_in(self, username, password):
        for member in self.users:
            if member.username == username and member.password == password:
                member.isonline = True
