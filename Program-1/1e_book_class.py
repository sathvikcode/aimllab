class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("\nBook Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

b1 = Book("Python Programming", "Guido", 850)
b2 = Book("Machine Learning", "Tom Mitchell", 1200)

b1.display()
b2.display()
