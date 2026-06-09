# Dictionary
# pairs ki form mein kaam krti
# used to stores datat va;ue in key:value pairs
# elements ko add,remove change kr sktay



info={
    "key":"value",
    "subjects":["python", "java"],
    "topics":("dictionary","sets"),
    "learning": "coding",
    "name":"AK",
    "age":21,
    "marks":94.4,
   " is_adult":True
}
print(info)
print(type(info))
# dictionaries are unordered,mutable, and dont allow duplictae keys

# individual values ko print karnay k liyeyy
print(info["name"])
print(info["learning"])
print(info["subjects"])

# we can alsoo change values
info["name"]="Aresha Khalid"
info["surname"]="Khalid Mehmood"
print(info)

# can also print null dictionary
null_dict={

}
null_dict["name"]='Apna Pakistan'
print(null_dict)

# Nested dictionaries

student={
    "name":"Aresha Khalid",
    "subjects":{
        "phy":67,
        "math":45,
        "English":90
    }
}

print(student)
print(student["subjects"])
# agar math k amrks print karwnay tou
print(student["subjects"]["math"])


# dictionary methods
# .keys() return all key values
print(student.keys())
# list mein change karnay k lieyy typecast karein
print(list(student.keys()))
# length print
print(len(student))


# .values() return all values
print(student.values())
# .items( ) return all(key:value ) paisr as tuples
print(student.items())
# .get("key") return no error
print(student.get("name"))
# print(student["name3"])  return error bcz of name3

# .update(newDict) insert new dictoanry items
student.update({"city":"Bhouch", "age":16})
print(student)

# sets
# collection of unordered items
# must be unique and immutable
# ignore duplicate valeus
collection={1,2,2,3,4,5,"hello","world"}
print(collection)
print(type(collection))
print(len(collection))

# emptyb set
null_set=set()


print(type(null_set))

# Set Methods
# set mutable hai but elements immuatble hain
# .add(elemnt)
null_set.add(1)
null_set.add(2)
null_set.add(2)

null_set.add("AK CH")

null_set.add((1,2,3))
# list add nayi kr sktayyy 
# tuple add kr sktay
# .remove9()

# .clear() 
# null_set.clear()


# .pop() removes random values


print(null_set.pop())

set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))

# Q
dict1={
    "cat":"A small animal",
    "table":["a piece of furniture","list of facts and figures"]
}
print(dict1)
# Q
subjects={
   " python","java","c++"," python","javascript","java",
   " python","java","c++","c"
}
print(len(subjects))

# Q
marks={}
x=int(input("enter marks of phys"))
marks.update({"phy":x})

x=int(input("enter marks of maths"))
marks.update({"math":x})

x=int(input("enter marks of eng"))
marks.update({"eng":x})
print(marks)

# Q store 9 and 9.0 separte in set
values={9,"9.0"}
print(values)

val={
    ("float",9.0),
    ("int",9)
}
print(val)