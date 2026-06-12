# del key
# used to delete object properties or object itself
class Student:
    def __init__(self, name):
        self.name=name


s1=Student("Aresha")
print (s1.name)
del (s1.name)
# print(s1.name)


# Private methods and attributes are meant to be used only for class
# Not accessible outside the class
class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1=Account("12345", "abcde")
print(acc1.acc_no)

# print(acc1.acc_pass)
print(acc1.reset_pass())


class Person:

    __name="Anonymous"

# isi tarah hm methods ko bhi private bna sktay jesay variables ko bnaya
    def __hello(self):
        print("Hello")
# but this method can be used by another method 
    def welcome(self):
        self.__hello()


p1=Person()
p1.welcome()


# Inheritance
# Example of single inheritance
# 1 single parent class and child class

class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name


car1=ToyotaCar("Fortuner")
car2=ToyotaCar("Civic")


car1.start()
       

# MultiLevel Inheritance

class Truck:
    @staticmethod
    def start():
        print("Truck started...")



    @staticmethod
    def stop():
        print("Truck stopped...")

class ToyotaTruck(Truck):
    def __init__(self,brand):
        self.brand=brand


class Fortuner(ToyotaTruck):
    def __init__(self, type):
        self.type=type

t1=Fortuner("diesel")
t1.start()


# Multiple Inheritance
# multiple classes ki properties ko inherit kar sktii

class A:
    varA="Welcome to class A"

class B:
    varB="Welcome to class B"
class C(A,B):
    varC="Welcome to class C"

c1=C()
c1.varA
c1.varB
c1.varC