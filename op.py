# if (5 and 4):
#     print("True")

# if (not(2&1)):
#     print("False")

# print(5//4)

#list
# arr=list((1,2,3,4))
# print(arr)

# arr=[]
# arr.append(1)
# arr.append(2)
# arr.append(3)
# print(arr)
# arr.pop()
# print(arr)

# arr=[1,2,3,4,5]
# arr[0:2]=[0,0]
# # arr1=arr[0:2]
# # print(arr[0:2] is arr1)
# print(arr)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry","girl"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# arr=[1,3,4]
# arr.insert(1,2)
# print(arr)
# arr=[1,2]
# dic={4:5}
# arr.extend(dic)
# print(type(arr[1]))
# print(arr)

#tuple
# tup=("apple","banana")
# print(type(tup))
# print(type(tuple((1,2,3,4))))
# tup=(1,2,3,4)
# lis=list(tup)
# print(type(lis))

# list=(1,2,3,4)

# for x in list:
#     print(x)
# for i in range(len(list)):
#     print(i)
#     print(list[i])

# tup=[1,2,3,4]
# tuple1=[5,6,7,8]
# print("12"*2)
# tup=(1,2,3,4)

# xor operator
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 ^ set2
# print(set3)

#map
#differece between dict and json : key in json is always string
# map={"hello":1,2:"word"}
# print(map)

# dic={"hello":1,"world":2}
# for x,y in dic.items():
#     print(x,y)

# arr=[1,2,3,4]
# for i in range(1,len(arr),2):
#     print(i)

# def helper(*arg):
#     arg[0]["hello"]=5

# map={"hello":1,"world":2}
# print(map)
# helper(map)
# print(map)
# # helper(map)

#in **kwargs, key value argument is passed and in *args, #positional argument is passed
# def fun(**kwargs):
#     print(kwargs)

# fun(a=1,b=2)
#class and objects 
#every this is class in python
# class Person:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return f"{self.a},{self.b}"

# temp=Person(1,2)
# del temp

#inheritance in python

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return f"{self.a},{self.b}"
#     def hello(self):
#         return "hello"
    
# class B(A):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c=c
#     def __str__(self):
#         return f"{self.a},{self.b},{self.c}"
#     def hello(self):
#         return super().hello()+"world"
    
# temp=B(1,2,3)
# print(temp.hello())

#iterators

# arr=[1,2,3,4]
# iter1=iter(arr)
# print(next(iter1))
# print(next(iter1))


# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.a>self.b:
#             raise StopIteration
#         else:
#             self.a+=1
#             return self.a-1
        
# temp=A(1,5)

# for i in temp:
#     print(i)

#scope in python 

#you cannot access variable of other scope with out using global : for global and nonlocal for local key word
# x=5

# def fun():
#     x=5
#     def child():
#         nonlocal x
#         x+=1
#         return x
#     return child 

# # print(x)
# temp=fun()
# print(temp())

# import json
# data={"name":1,1:2,"surName":[1,2,3,4]}
# x=json.dumps(data)
# print(json.loads(x))

#files in python 
#CRUD
import os 
if not os.path.exists("hello"):
    os.mkdir("hello")
filePath="hello/hello.py"
try:
    file=open(filePath,"a+")
    try:
        file.write("print('hello world')")
    except:
        print("error writing to file")
    else:
        print(file.read())
    finally:
        file.close()
except IOError:
    print("error opening file")
finally:
    if os.path.exists(filePath):
        os.remove(filePath)
