from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Test case
animals = [Dog(), Cat()]
print("Task 4 Output:")
for animal in animals:
    print(animal.make_sound())
print()