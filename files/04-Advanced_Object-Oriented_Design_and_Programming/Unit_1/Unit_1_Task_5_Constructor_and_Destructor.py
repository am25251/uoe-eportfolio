class Person:
    def __init__(self, name):
        # Initialize name
        self.name = name
        print(f"{self.name} has been created.")

    def __del__(self):
        # Destructor message
        print(f"{self.name} has been deleted. Goodbye!")


# Test case
print("Task 5 Output:")
p = Person("Alice")
del p