from User import User
from abc import ABC, abstractmethod
import matplotlib.image as img
import matplotlib.pyplot as plt


class Post(ABC):

    def like(self):
        pass

    def comment(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class TextPost(Post):

    def __init__(self, text):
        self.text = text

    def __str__(self):
        print(self.text)


class ImagePost(Post):

    def __init__(self, image):
        self.image = image

    def __str__(self):
        picture = img.imread(self.image)
        plt.imshow(picture)


class SalePost(Post):

    def __init__(self, *data):
        self.description = data[0]
        self.price = data[1]
        self.location = data[2]
        self.is_available = True

    def __str__(self):
        pass

    def sold(self, password):
        pass


class ConcreteUser(User):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.isonline = True
        super().__init__()

    def like(self):
        pass

    def upload(self):
        pass

    def __str__(self):
        pass

    def update(self, notification):
        pass

    def publish_post(self, post_type, *data):
        if post_type == "Text":
            return TextPost(data[0])
        if post_type == "Image":
            return ImagePost(data[0])
        if post_type == "Sale":
            return SalePost(*data)
        raise Exception
