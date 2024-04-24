# Association is a relationship between two classes where one class uses the functionality of another class.
# The relationship can be one-to-one, one-to-many, many-to-one, and many-to-many
# In this example, the Driver class has a method drive that takes an instance of Car as an argument.
# This is an example of association.
class Car:
    def __init__(self, model):
        self.model = model


class Driver:
    def __init__(self, name):
        self.name = name

    def drive(self, car):
        print(f"{self.name} is driving a {car.model} car.")


# Direct association is a type of association where one class directly uses the methods or attributes of another class.
# In this example, the Person class has a method command that directly calls the bark method of the Dog class.
# This is an example of direct association.
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"


class Person:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def command(self):
        return self.dog.bark()


# Aggregation is a specialized form of Association where all objects have their own lifecycle, but there is ownership, and child objects cannot belong to another parent object. Let's consider an example where a Library class contains a list of Book instances.
# the Library class has a method add_book that takes an instance of Book as an argument and adds it to the books list. The list_books method lists all the books in the library.
# This is an example of aggregation because the Library class has a list of Book instances, but each Book instance can exist independently of the Library.

class Book:
    def __init__(self, title):
        self.title = title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book.title)


# Composition is a type of association where the child cannot exist independently of the parent.
# If the parent is deleted, all its child objects will also be deleted.
# the Computer class has a CPU instance as an attribute. The CPU instance is created when a Computer instance is created,
# and it cannot exist without the Computer. This is an example of composition.
class CPU:
    def __init__(self, model):
        self.model = model


class Computer:
    def __init__(self, cpu_model):
        self.cpu = CPU(cpu_model)

    def get_cpu_model(self):
        return self.cpu.model

