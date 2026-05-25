class Vehicle:
    def __init__(self, brand, fuel_type):
        # Initialize attributes
        self.brand = brand
        self.fuel_type = fuel_type


class Car(Vehicle):
    def __init__(self, brand, fuel_type, num_doors):
        # Call parent constructor
        super().__init__(brand, fuel_type)
        # Initialize additional attribute
        self.num_doors = num_doors


# Test case
car1 = Car("Toyota", "Petrol", 4)
print("Task 1 Output:")
print(car1.brand, car1.fuel_type, car1.num_doors)
print()