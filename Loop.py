# loops are used to reapeat instructions
# while and for loops

count=1
while count<=5:
    print("hello")
    count=count+1

    # Another example
i=1
while i<=5:
    print("Bye", i)
    i+=1

    # print numbers from 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

    # print numbers from 5 to1
i=5
while i>=1:
    print(i)
    i-=1

# dont use infinite loops
# Print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

# print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

# Print multipliaction table of a number n
n=int(input("Enter a number"))
i=1
while i<=10:
    print(n*i)
    i+=1
# print numbers
nums=[1,2,4,5,67,89,10,12,13,45]

idx=0
while idx < len(nums):
    print(nums[idx])
    idx+=1

# how to search any elemnt by using tuple
nums=(1,2,4,5,67,89,10,12,13,45)

x=12
i=0
while i<len(nums):
    if nums[i] == x:
        print("found at", i)
        break
    else:
        print("finding")
    i+=1



# continue acts as skip
i=0
while i<=5:
    if(i==3):
        i+=1    
        continue
    print(i)
    i+=1

# how to pritn odd numbers
i=0
while i<=10:
    if(i%2 == 0):
        i+=1
        continue
    print(i)
    i+=1

# now for printing even numbers
i=0
while i<=10:
    if(i%2 != 0):
        i+=1
        continue
    print(i)
    i+=1


# for loops are sused for sequential traversal
# like in list,tuple,string
# here el is variable name and in is a keyword
list=[1,2,3]
for el in list:
    print(el)


veggies=["potatao","pineapple","tomato"]
for el in veggies:
    print(el)


# same goes for tupple
tup=(1,2,3,4,5,6,7,3)
for num in tup:
    print(num)

# here for string
str="apnacollege"
for char in str:
    print(char)
else:
    print("end")



#
list=[1,2,3,4,5,65,43,23,56]
for el in list:
    print(el)


# now for tupple
tuple=(1,2,3,4,5,65,43,23,56)
x=23
idx=0
for el in tuple:
    if(el ==x):
        print("ELemnt found at index", idx)
  
    idx+=1

# Range function returns a seuqnce of number start form 0 by default
print(range(5))
seq=range(5)
for i in seq:
    print(i)

# now we have diffe rmethods to write it
# range (stop) 0 sy 9
for i in range(10):
    print(i)
# 2,10 means start and stop 2sy 9
for i in range(2,10):
    print(i)
# start? stop, step  
# print vene numbers from 2 to 10
for i in range(2,10,2):   #2 sy start 10 sy pehlay tk aur 2 ki valeu sy increase
    print(i)
# for odd numbers
for i in range(1,10,2):   #1 sy start 10 sy pehlay tk aur 2 ki valeu sy increase
    print(i)


# print numbers from 1 to 100 using range
for i in range(1,101):
    print(i)
# print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

# print multiplication table of a number  n
n=int(input("Enter a number"))
for i in range(1,11):
    print(n*i)


# pass is anull statemnet taht dioes nothing
# use as placeholder for futuure code

for el in range(10):
    pass
print("Some useful work")

# pritn sum of n number
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum is ", sum)

# using while loop
n=7
sum=0
i=1
while i<=n:
    sum +=i
    i+=1
print("Sum is ", sum)

# factorial by for
n=7
fact=1
i=1
while i<=n:
    fact *=i
    i+=1
print("Fcat is ",fact)

n=7
fact=1
for i in range(1,n+1):
     fact *=i
print("Fcat is ",fact)
