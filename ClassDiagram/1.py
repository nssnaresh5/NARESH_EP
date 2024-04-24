# Encapsulation
class Car:
    def __init__(self, brand, model, year):
        self._brand = brand  # private attribute
        self._model = model  # private attribute
        self._year = year  # private attribute

    # getter method
    def get_car_details(self):
        return f"Brand: {self._brand}, Model: {self._model}, Year: {self._year}"


# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery):
        super().__init__(brand, model, year)
        self._battery = battery  # private attribute

    # getter method
    def get_battery_status(self):
        return f"Battery: {self._battery}%"


# Polymorphism
class Pet:
    def __init__(self, name):
        self._name = name

    def make_sound(self):
        pass


class Dog(Pet):
    def make_sound(self):
        return f"{self._name} says Woof!"


class Cat(Pet):
    def make_sound(self):
        return f"{self._name} says Meow!"


# Abstraction
from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    @abstractmethod
    def do_something(self):
        pass


class AnotherSubclass(AbstractClassExample):
    def do_something(self):
        super().do_something()
        return "Doing something in the AnotherSubclass!"


# Testing the code
car = Car("Tesla", "Model S", 2020)
print(car.get_car_details())

ecar = ElectricCar("Tesla", "Model 3", 2021, 100)
print(ecar.get_car_details())
print(ecar.get_battery_status())

dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.make_sound())
print(cat.make_sound())

another_subclass = AnotherSubclass()
print(another_subclass.do_something())
