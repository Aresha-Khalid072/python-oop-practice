# block of statements that perform a specific task
# redundant code harab prgrammer ki nashani hai
# redundancy km ho gyi

def calcSum(a,b):  #func def
    sum=a+b
    print(sum)
    return sum

calcSum(2,3)  #function call
calcSum(7,3) 

def calcSum(a,b):
    return a+b
sum=calcSum(7,10)
print(sum)

def print_hello():
    print("hello")
  
print_hello()

# jo function return mein kuch return nayi krta uski ouput none ayye gyi
output=print_hello()
print(output)

# calc average of 3 numbers
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg(1,2,3)

# builtin functions
# print("apna ")
# len() type() range()

print("AK", end=" ")  #sep=" "
print("G oka") #end="\n"

# userdefined function user define krta

# default parameters
# jb koi arg pas na katrein tou yeh sue hoon giy
# pehlay non default value ayeyy gyi aur then default vali jisey hm ny khud value assign ki hai


def calc_product(a,b=2):
    print(a*b)
    return a*b

calc_product(1)


# print length of  a list
cities=["gujrat","bhouch","murree"]
heroes=["Ak","mahir","Mala"]

def len_print(list):
    print(len(list))

len_print(cities)
len_print(heroes)

# print list items in a single line
def print_items(list):
    for items in list:
        print(items, end=" ")

print_items(heroes)
print( " ")

# find factorial

def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

fact(7)


# convert i usd into inr

def converter(usd_r):
    ind_r=usd_r*83
    print(usd_r, "Usd =", ind_r , " indian rupee value")

converter(4)

def evenOddfunc(val):
    if(val %2 == 0):
        print("Even")
    else:
        print("Odd")

evenOddfunc(16)

# Recursion 
# When a functions calls itself repeatedly
# calling statemnt khud hi
# loops ka hatarnak version

def show(n):
    # agar hm base case ko ahat dyein tou yrh infinetly run karay ga aur code carsh akr jayey ga liek in loops

    if(n==0): # base case like idhr value rokni
        return
    print(n)
    show(n-1)

show(6)


# n! =(n-1)!*n
# 5!= (5-1)!*5  =4!*n
# 1! =1 and 0!=1 by default

def factorial(n):
    if( n==1 or n==0):
        return 1
    else:
        return factorial(n-1)*n
    
print(factorial(6))

#write a recusrsive function to calculate sum of first n natural numbers
def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n

calcSum=sum(5)
print(calcSum)

# 
def print_List(list,idx=0):
    if(idx== len(list)):
        return
    print(list[idx])
    print_List(list,idx+1)

fruit=["mango", "banana","oranges","peach"]
print_List(fruit)
