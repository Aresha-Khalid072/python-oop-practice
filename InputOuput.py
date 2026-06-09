# i/o input and output
# file mein dta ko read ,write ,update close waghera akr rahay
# can be used to perfrom operations on a file
# types of files
# text filesdata store in form of characters .txt. docs .log
# binary files data not store in form of characters like .png .jpeg
# agar permanent dtaa store karna chhatay tou hm file mein store kr sktay


# Open files
# we have to open file before read and writing data
# f= open("filename", "mode")
# mod ecan be read or write
# by default read mode
# t by default tetx mode
# r ka mtlb read karna hai but r+ ka mtlb hai rad and write karna hai
# w ka mtlb hai write karna but w+ ka mtlb hai read and write akrna hai


f=open("demo.txt", "r")
data=f.read()
print(data)
# s[ecific characters bhi read kr sktay]   data=f.read(5)


line1= f.readline()   # yeh line read krnay k lieyy
print (line1)
print(type(data))
# jo bhi file open ki usey close zaroor karein


# f.write("i want to learn js123")
f.close()


# writing to a file
# w overwrites the entire line

# file=open("write.txt", 'w')
# file=open("write.txt", 'a') yeh a append ho jayey ga pehlay walay data mein

file=open("write.txt", 'a')
file.write("i will move to react js")
file.write("\n after that nodejs")
file.close()


# for read mode
with open("data.txt", 'r') as f:
    data=f.read()
    print(data)

# for write mode
with open("data.txt", 'w') as f:
    f.write("Hello g")
  

import os
os.remove("write.txt")

with open("practise.txt", 'w') as f:
    f.write("Hi everyone\n We are learning python")
    f.write("Hi everyone\n We are learning python")


with open("practise.txt", 'r') as f:
    data=f.read()

newData=  data.replace("everyone","Java")
print(newData)


with open("practise.txt", 'w') as f:
    f.write(newData)