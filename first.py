print("Hello World")
print("Aresha Khalid")
# print is a function anme in python  aur inverted commas k andar likh dyein jo bhi prin karwana hai
#python charcater set
# A to Z a to z ,digits 0 to 9, + - * /, white spaces blank spaces, ascii and uni code charcyers

print("Heloo G", "how r u ?")  # same line mein print ho ga sb
print(23)
print(25)
print(23+25)
# variable name given to a memory location in a program
# variable =value
# random jagah par memory mein values store
name="Ak" #string
age=23
price=24.59
# print("name")  yhe oyun hi name print ho jayey ga
print(name)  # ab Ak print ho ga
print ("My name is", name)
print("My age is", age)

# 
age2=age
print("My age is", age2)
#variable names simple,short and meaningful hoon like name,age ,count

# how to print type
print(type(name))
print(type(age))
print(type(str))


#datatypes int,string,floor,boolean, none
#int +,-,0 values
#string name can be written in single,double or triple quote " " 
name2='''SK'''
print(name2)
#float 3.99
#boolean True False capital likhnay hain
#none no type of vale store

old =False  #capital True or False likhnay hain
a=None
print(type(old))
print(type(a))

#Keywords
 #Reserved words  and,as ,break,True,False etc
 #Python is a case sensitive language
 # how to calculate sum
b=10
c=2
sum=b+c
diff=b-c
print(sum)
print(diff)

# relatuonal operators true or false mein value return kartay
a=50
b=20
print(a==b) # false
print(a!=b)# true
print(a>=b)#true
print(a>b)#true
print(a<=b)#false 
print(a<b)#false

#assignment opertaors
num=10
num+=10
print(num) #20
num-=10
print(num)
num*=10
print(num)
num/=10
print(num)
num **=10
print(num)


# logical 
print(not False)
print(not True)

val1=True
val2=False
print("and oper", val1 and val2)
print("or oper", val1 or val2)

# type conversion
a=int("2")
b=23.3
print(a+b)




#Punctuators sentenece structure ko organiz ekarwana
#Typed language
#Implicit languange
#koi type batany kiz aroorat nayi
# string and numeric values can operate together with *
A,B=2,3
text="@"
print(2*text*3)
#stringa nd string can operate with+
C,D='2',3
txt="@"
print((C+txt)*D)
# numeric values can operate with all arithmetic operators
E,F=2,3
C=4
print(A+B*C)
#arithmetci expression with int and float will return value in float
A,B=10,5.0
C=A*B
print(C)
#result of div opertor with two integr will be float
A,B=1,2
C=A/B
print(C)
#int div // with float and int will give int displayed as float
A,B=1.5,3
C=A//B
print(C, A/B)
#result of integer div is same as floor division

A,B=12,5
C=A//B
print(C) 


A,B=-12,5
C=A//B
print(C) 



A,B=12,-5
C=A//B
print(C) 

#rem is neg when demoniator is neagtive





#inputs in python
#for string
name=input("name: ")
print(name)
#for int
age=  int(input("age:"))
print(age)
#float
price=float(input("price: "))
print("My name is ", name, ".My age is ", age , "years old.")


# conditional statments
# if k baad : yeh lagan hai same for eleif and else aur 4 spaces k gap dena hauar
light=(input("light: "))
if(light == "red"):
   print("stop")
elif(light == "yellow"):
   print("look")
elif(light== "green"):
   print("go")
else:
   print("Light is broken")

   #marks


marks = int(input("marks: "))  # Convert to int
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("fail")


    # Practise questions
    first=int(input("enter 1st num:"))
    second=int(input("enter 2nd num:"))
    print("Sum is", first+second)

    #print area
    side=float(input("Enter side:"))
    print("square is ", side*side)
    

    #print average
    a=float(input("enter 1st num:"))
    b=float(input("enter 2nd num:"))
    print("Average is ",( a+b)/2)

    