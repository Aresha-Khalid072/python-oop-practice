# datatyoe store seq of characters ->strings
str1="this is a string.\nNow do it"
str2='this is a string. \t Now do it'
str3="""This is a string """
print(str3)
print(str1)
print(str2)
#next line is not valid in python
#escape sequence characters are for formating


#concatenation
string1="apna"
string2="college"
print(string1+ " "+string2)
string3=string1+string2
# yahh phir hm iseyy kisi aur mein bhi store karwa sktayy
print(string3)


# length of string->  len(str)
# string ki length mein saces and special chaarcters bhi count hotay
print(len(string1))
# yahh hm yeh bhi kr sktay k isey ksi aur mein store karwa sktay 
len2=len(string2)
print(len2)


# Indexing
# position no
# start from 0
str="Apna College"
print(str[1]) #p
print(str[4])  # space


# Slicing is accessing parts of string
# machine learning mein sue krtay isye
# str[starting index:ending ndex] but ending index output mein include nayi ho ga

print(str[1:4])  #pna
print(str[5:12]) #College
print(str[5:])  # iska mtlb hai k last index tk jana hai
print(str[:4])  # iska mtlb hai k hm 0 sy 4 tk jana chataya



# In python for slicing we also have backward counting whoch starts from 1
stri1="Apple"  #-5 -4  -3 -2 -1
print(stri1[-3:-1])
 # is mein bhi last index includ enayi ho ga

#  
str="i am studying python from apna college" 
print(str.endswith("ege")) # return true

# str.capitalize( ) 1st char
#  but yeh original string mein chnages nayi karay ga is lieyy new meins tore karoo
str=str.capitalize()
print(str)

# replace("old","new")
print(str.replace("python" , "javascript"))
# find()
print(str.find("o"))
# agar ksii aesi cheez ko search katrein jo exist nayi akrti tou -1 return ho ga
# count("am") kitni baar yeh lafz ayay yeh batyey ga

print(str.count("am"))   #am 1 baar aya hai gyz


# Question

name=input("Enter your name:")
print(name)
print(len(name))

# occurence of $ in a strings find it
# yaani cpunt print karwana hai
str="Hi. $I am   $ symbol"
print(str.count("$"))





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
if (marks >= 90):
    print("A")
elif(marks >= 80 and marks<90) :
    print("B")
elif (marks >= 70 and marks<80):
    print("C")
else:
    print("fail")


    # nesting
age=34
if(age >= 18):
    if(age>=80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("Can NoT DRIVE")

  
#Practise Questions
#1
number=int(input("Enter a number"))
if(number%2 == 0):
    print(number, "is Even")
else:
    print(number, "is Odd")

#check  entered number is multiple of 7 or not
number=int(input("Enter a number"))
if(number%7 == 0):
    print(number, "is multiple of 7")
else:
    print(number, "is not multiple of 7")

#find greatest of 3 numbers enetred by user
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if(a >= b and a >= c):
    print("greater number is ",a )
elif (b >= a and b >= c):
    print("greater number is ",b )    
else:
    print("greater number is", c)    
