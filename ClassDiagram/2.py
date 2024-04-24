from diagrams import Diagram, Cluster
from diagrams.programming.language import Python

with Diagram("Class Diagram", show=False):
    car = Python("Car")
    electric_car = Python("ElectricCar")
    pet = Python("Pet")
    dog = Python("Dog")
    cat = Python("Cat")
    abstract_class = Python("AbstractClassExample")
    another_subclass = Python("AnotherSubclass")

    with Cluster("Inheritance"):
        car >> electric_car
        pet >> dog
        pet >> cat
        abstract_class >> another_subclass