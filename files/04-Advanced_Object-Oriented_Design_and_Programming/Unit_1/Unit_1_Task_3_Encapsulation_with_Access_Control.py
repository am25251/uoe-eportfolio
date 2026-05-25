class BankAccount:
    def __init__(self, initial_balance=0):
        # Private attribute
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# Test case
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print("Task 3 Output:")
print(acc.get_balance())
print()