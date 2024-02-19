from abc import ABC, abstractmethod


class User(ABC):

    def __init__(self):
        self._members = []
        self._notifications = []



    @abstractmethod
    def like(self):
        pass

    @abstractmethod
    def upload(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def follow(self, member):
        self._members.append(member)

    def unfollow(self, member):
        self._members.remove(member)

    def notify(self, notification):
        for member in self._members:
            member.update(notification)

    @abstractmethod
    def update(self, notification):
        pass
