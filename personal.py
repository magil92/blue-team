
"""name = "Mohammed"
age = 33
city = "misurata"

print("Hi welcome let me intrduce my self")
print("My name is :", name)
print("My age is:", age)
print("My city:", city)
print(name,age,city)
   """
"""class Person:
    def __init__(self):
        pass

        self.name = name
        self.age = age
        self.date = date.today()

    def showinfo(self):
        print("الاسم:", self.name)
        print("العمر:", self.age)
        print("التاريخ:", self.date)
"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" added :{amount}. you have money :: {self.balance}")
        else:
            print(" should > 0")

    def withdraw(self, amount):
        if amount <= 0:
            print(" should> 0")
        elif amount > self.balance:
            print(" Not yet")
        else:
            self.balance -= amount
            print(f" Donhas been withdrawn {amount}. you have money {self.balance}")

    def display(self):
        print(f" account_owner: {self.owner}")
        print(f" اthe money is: {self.balance}")

account = BankAccount("mohammed")
account.deposit(5000)
account.withdraw(2000)
account.display()
