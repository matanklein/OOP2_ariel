from User import User
from Post import *


class ConcreteUser(User):

    def __init__(self, username, password):
        self.number_of_posts = 0
        self.isonline = True
        super().__init__(username, password)

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {self.number_of_posts}, Number of followers: {self.number_of_followers}"


    def update(self, notification):
        for member in self._members:
            member.add_notification(notification)

    def publish_post(self, post_type, *data):
        if post_type == "Text":
            post = TextPost(self, data[0])
            self.number_of_posts = self.number_of_posts + 1
            print(post)
            self.notify(self.username + " has a new post")
            return post

        if post_type == "Image":
            post = ImagePost(self, data[0])
            self.number_of_posts = self.number_of_posts + 1
            print(post)
            self.notify(self.username + " has a new post")
            return post

        if post_type == "Sale":
            post = SalePost(self, *data)
            self.number_of_posts = self.number_of_posts + 1
            print(post)
            self.notify(self.username + " has a new post")
            return post

        raise Exception

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for massage in self._notifications:
            print(massage)
