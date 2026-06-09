# OOP (Object-Oriented Programming) in Python
# Mapping real world scenarios to code using objects
# First create a class (blueprint), then create objects from it

# Basic Class Example


class Student:
    name = "Aresha"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)


class Car:
    color = "blue"
    brand = "mercedes"

c1 = Car()
print(c1.color)
print(c1.brand)



# Class with Constructor (__init__)


class St1:
   
    college = "Punjab college"

    # __init__ is the constructor
    # 'self' is a reference to the current instance of the class
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student...")

    def __str__(self):
        return f"Student({self.name}, Marks: {self.marks})"

    def welcome(self):
        print("Hello", self.name)

    def getMarks(self):
        return self.marks


s1 = St1("Ali", 67)
print(s1.name, s1.marks)
print(s1) 

s2 = St1("Arji", 87)
print(s2.name, s2.marks)
s2.welcome()

print(s2.college)
print(s2.getMarks())



# Class with Average Calculation


class S1:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student({self.name}, Marks: {self.marks})"

    def get_avg(self):
        total = 0                        
        for val in self.marks:
            total += val
        avg = total / len(self.marks)   
        print(f"Hi {self.name}, your average score is {avg:.2f}")


s1 = S1("Aresha", [76, 87, 90])
s1.get_avg()
print(s1) 



# Abstraction
# Showing only important features to the user
# Hiding implementation details of a class


class Truck:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def __str__(self):
        return f"Truck(acc={self.acc}, brk={self.brk}, clutch={self.clutch})"

    def start(self):
        self.clutch = True
        self.acc = True
        print("Truck Started")


t1 = Truck()
t1.start()
print(t1) 



# Encapsulation
# Wrapping data and functions into a single unit


class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc

    def __str__(self):
        return f"Account(acc={self.acc}, balance={self.bal})"

    def debit(self, amount):
        self.bal -= amount
        print(f"Rs {amount} was debited")
        print(f"Total balance = {self.getBalance()}")

    def credit(self, amount):
        self.bal += amount
        print(f"Rs {amount} was credited")
        print(f"Total balance = {self.getBalance()}")

    def getBalance(self):
        return self.bal


acc1 = Account(10000, 2345)
print(acc1)
acc1.debit(1000)
acc1.credit(400)
acc1.credit(50000)