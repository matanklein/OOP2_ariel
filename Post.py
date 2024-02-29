from abc import ABC, abstractmethod
import matplotlib.image as img
import matplotlib.pyplot as plt


class Post(ABC):

    def __init__(self, owner):
        self._owner = owner

    def like(self, member):
        if self._owner.username != member.username:
            print(f"notification to {self._owner.username}: {member.username} liked your post")
            self._owner.add_notification(f"{member.username} liked your post")

    def comment(self, member, comment):
        if self._owner.username != member.username:
            print(f"notification to {self._owner.username}: {member.username} commented on your post: {comment}")
            self._owner.add_notification(f"{member.username} commented on your post")

    @abstractmethod
    def __str__(self):
        pass


class TextPost(Post):

    def __init__(self, owner, text):
        self.text = text
        super().__init__(owner)

    def __str__(self):
        return f"{self._owner.username} published a post:\n\"{self.text}\"\n"


class ImagePost(Post):

    def __init__(self, owner, image):
        self.image = image
        super().__init__(owner)

    def __str__(self):
        return f"{self._owner.username} posted a picture\n"

    def display(self):
        print("Shows picture")
        picture = img.imread(self.image)
        plt.imshow(picture)
        plt.show()


class SalePost(Post):

    def __init__(self, owner, *data):
        self.description = data[0]
        self.price = data[1]
        self.location = data[2]
        self.is_available = True
        super().__init__(owner)

    def __str__(self):
        if self.is_available:
            return f"{self._owner.username} posted a product for sale:\nFor sale! {self.description}, price: {self.price}, pickup from: {self.location}\n"
        return f"{self._owner.username} posted a product for sale:\nSold! {self.description}, price: {self.price}, pickup from: {self.location}\n"

    def sold(self, password):
        if self._owner.password != password:
            raise Exception
        self.is_available = False
        print(f"{self._owner.username}'s product is sold")

    def discount(self, discount, password):
        if self._owner.password != password:
            raise Exception
        if discount < 0 or discount > 100:
            raise Exception
        self.price = self.price - (discount/100)*self.price
        print(f"Discount on {self._owner.username} product! the new price is: {self.price}")
