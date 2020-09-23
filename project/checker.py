"""This program lets you give input to convert to hash"""
from project.hashermd5 import Hasher
print("What is the datatype 1. string 2. dictionary 3. list 4. tuple")
choice=int(input())
if choice==1:
    ob1=Hasher(input("Enter the string"))
elif choice==2:
    d={}
    num=int(input("Enter the number of elements"))
    for i in range(num):
        s=input("enter the key")
        v=input("Enter the element")
        d[s]=v
    ob1=Hasher(d)
elif choice==3:
    newlist=[]
    num = int(input("Enter the number of elements"))
    for i in range(num):
        newlist.append(input("Enter the element"))
    ob1=Hasher(newlist)
else:
    newlist=[]
    num = int(input("Enter the number of elements"))
    for i in range(num):
        newlist.append(input("Enter the element"))
    ob1=Hasher(tuple(newlist))
result=ob1.hashermd5()
print(result)




