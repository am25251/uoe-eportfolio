from abc import ABC, abstractmethod
# Car interface
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete cars
class Sedan(Car):
    def drive(self):
        print("Driving a Sedan")

class SUV(Car):
    def drive(self):
        print("Driving an SUV")

class Hatchback(Car):
    def drive(self):
        print("Driving a Hatchback")

# Abstract factory
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

# Concrete factories
class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()

class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()

class HatchbackFactory(CarFactory):
    def create_car(self):
        return Hatchback()

# Client code
factories = [SedanFactory(), SUVFactory(), HatchbackFactory()]

for factory in factories:
    car = factory.create_car()
    car.drive()


