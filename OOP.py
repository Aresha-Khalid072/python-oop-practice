# To map with real worl d scenarios we use objects in code ->OOP
# pehlay class bnaoo then object
# class is a blueprint for creating objects
# creating class
class Student:
    name="Aresha"

s1=Student()
print(s1.name)

s2=Student()
print(s2.name)


class Car:
    color="blue"
    brand="mercedes"

c1=Car()
print(c1.color)
print(c1.brand)


class St1:
    # class attribute 1 dafa hi store hota aur sb k lieyy use kr sktay isey
    # class mein data aur methods store ho sktay

    college="Punjab college"
    # name="Aresha G"
    # yeh __init__ aik constructor hai aur self naam ki 1parameter yeh must leta hai
    # se;f is refernce to the current instance of the class



#  default constructors
    # def __init__(self):
    #     pass

#   paramtereized constrctors 
# object attribute > class attrubute
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
        print("Adding new student...")

    def welcome(self):
        print("hello", self.name)

    def getMarks(self):
        return self.marks

s1=St1("Ali",67)
print(s1.name, s1.marks)

s2=St1("Arji", 87)
print(s2.name, s2.marks)
s2.welcome()


print(s2.college)
print(s2.getMarks())

class S1:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi", self.name , "you avg score is", sum/3)



s1=S1("aresha", [76,87,90])
s1.get_avg()


# Static methods dont allow self paramerter
# work for class level
#  @staticmethod use krna hai


# Abstraction
# showing only imp features to user
# hiding implementation details of  a class

class Truck:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
       
        self.clutch=True
        self.acc=True
        print("Truck Started")


t1=Truck()
t1.start()


# Encapsulation
# Wrapping data and functions into a single unit


class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc

        # debit method balance sy amount cancel ho gyi

    def debit(self, amount):
        self.bal -=amount
        print("Rs", amount, "was debited")
        print("Total balance =",self.getBalance())

        # credit

    def credit(self, amount):
        self.bal +=amount
        print("Rs", amount, "was credited")
        print("Total balance =",self.getBalance())

    def getBalance(self):
        return self.bal
    



acc1=Account(10000, 2345)
# print(acc1.bal)
# print(acc1.acc)
acc1.debit(1000)
acc1.credit(400)
acc1.credit(50000)
