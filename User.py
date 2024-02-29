from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self, username, password):
        self._members = []
        self._notifications = []
        self.username = username
        self.password = password
        self.number_of_followers = 0

    @abstractmethod
    def __str__(self):
        pass

    def follow(self, member):
        if not member.is_follower(self):
            member.addfollow(self)
            print(self.username + " started following " + member.username)

    def unfollow(self, member):
        member.removefollow(self)
        print(self.username + " unfollowed " + member.username)

    def notify(self, notification):
        for member in self._members:
            member.update(notification)

    @abstractmethod
    def update(self, notification):
        pass

    def addfollow(self, member):
        self._members.append(member)
        self.number_of_followers = self.number_of_followers + 1

    def removefollow(self, member):
        self._members.remove(member)
        self.number_of_followers = self.number_of_followers - 1

    def add_notification(self, notification):
        self._notifications.append(notification)

    def is_follower(self, member):
        return member in self._members
