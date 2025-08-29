#Week 5 python Assignment

#Question 1 solution.
# Parent class
class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"


# Child class (Inheritance)
class Novel(Book):
    def __init__(self, title, author, publication_year, genre):
        # Call parent constructor (Book)
        super().__init__(title, author, publication_year)
        self.genre = genre

    # Polymorphism: overriding get_book_info()
    def get_book_info(self):
        return f"Novel: {self.title} ({self.genre}), Author: {self.author}, Year: {self.publication_year}"


# Another child class to show polymorphism clearly
class Textbook(Book):
    def __init__(self, title, author, publication_year, subject):
        super().__init__(title, author, publication_year)
        self.subject = subject

    def get_book_info(self):
        return f"Textbook: {self.title} on {self.subject}, Author: {self.author}, Year: {self.publication_year}"


# Create objects
book1 = Book("Chasing Red", "Isabelle Ronin", 2017)
book2 = Novel("After", "Anna Todd", 2014, "Romance")
book3 = Textbook("Python Basics", "John Smith", 2022, "Computer Science")

# Demonstrate polymorphism (same method, different outputs)
print(book1.get_book_info())
print(book2.get_book_info())
print(book3.get_book_info())



#Question 2 solution.
# Polymorphism Challenge

class Animal:
    def move(self):
        return "Animals can move in different ways."


class Dog(Animal):   # Dog inherits from Animal
    def move(self):
        return "The dog runs on four legs"


class Bird(Animal):  # Bird inherits from Animal
    def move(self):
        return "The bird flies in the sky"


class Fish(Animal):  #  Fish inherits from Animal
    def move(self):
        return "The fish swims in the water"


# Demonstrating polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())



