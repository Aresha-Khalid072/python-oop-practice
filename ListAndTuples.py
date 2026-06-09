# built in data type taht stores set of  values
# can store differ type of datatypes together

marks=[12.3 ,34.5, 56.7, 98.9]
print(marks)
print(type(marks))


# index
print(marks[0])
print(marks[1])
# can alsp pront length

print(len(marks))

student=["AK", 23,"Karachi"]
print(student)

# in python strings are immutable
# lists are mutable
# list mein value access bhi kr sktay and change bhi but for strings access kr sktay but chnaging is not allowed

print(student[0])
student[0]="Aresha"
print(student)
# range k andar values kko access kr sktayy bs


# list slicing is similar to string slicing
# list_name[starting:ending_index]
# ending index is not included

marks=[1,2,3,4,5]
print(marks[1:4])
# [2, 3, 4]
print(marks[:4])     # 0 sy index start kar k 4 index sy pehlay tk values print
print(marks[1:])
# negtaive indexing is included
print(marks[-3:-1])

# list methods

list=[2,1,3]
list.append(4)
# last mein value ko add kr dy ag
print(list)
# sorting cheezon ko sahi arange karna chotay sy baray
print(list.sort())   # goone return none
print(list)  #sorted one
# for sorting list in descending order
# list.sort(reverse=True)
print(list.sort(reverse=True))
print(list)
# strings par bhi sorting apply kar sktayy

list1=['a', 'd','e','b','c']
print(list1.sort())# none
print(list1) #asce


print(list1.sort(reverse=True))
print(list1) #desce

list1.reverse() # va;ues revrse karay ga
print(list1) 

# list.insert(idx, elem)
list2=[1,2,3,4,5]
list2.insert(2,4)
print(list2)
# remove 1st occurence of elemnt remove karay ga
print(list2.remove(1))
print(list2)
# pop remove at index
list2.pop(4)
print(list2)


# Tuples in python
# built in datatype  and it is immutable just like strings
# we use ()
tup=(2,1,3,1)
print(tup)
# print(type(tup))index accessing
print(tup[0])
print(tup[1])
# assignment is nott allowed kike in strings
tp=(1,)
print(tp)
print(type(tp))
# comma lagaan chhaieyy agar single value hai kiu k yeh agar int hai tou int show akraya ga
# agar value float ahi tou f;lat if it is string tou string
# multiple va;ues  lieyy optional hai k last ;ar , lagana hai tou lagaoo

# slciing same wesay kaam karti jesay strings mein yahh lsit mein
print(tup[1:3])

print(tup.index(1))
print(tup.count(1)) # yeh batayy ga k 1 kitini baar aye ahai

# Q
movies=[]
movie1=input("Enter your 1st fvrt movies")
movie2=input("Enter your 2nd fvrt movies")
movie3=input("Enter your 3rd fvrt movies")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)



# palindrome samnay sy aur peehay sy same hoo 12321
list1=[1,2,1]
list2=[1,2,3]
list1_copy=list1.copy()
list1_copy.reverse()


if(list1_copy == list1):
    print("Palindrome")
else:
    print("Not a plaindorme")
# Tuples
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))

grades=["C","D","A","A","B","B","A"]
grades.sort()
print(grades)