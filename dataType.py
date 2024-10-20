#implement basic data structures in python

#list
# a=['a',1,2]
# b=list(('a',3,4))

# print(a,type(b))

# #set
# a={1,2,3}
# b=set((1,2,3))
# print(a,type(b))


# #map
# a={'a':1,'b':2}
# a=dict(a=1,b=2)

# print(a,type(a))

#numbers


# a=1
# b=1.2
# c=1+2j
# c=a+b
# print(a,type(a))
# print(b,type(b))
# print(c,type(c))
# a=1e2

# print(a,type(a))
# import random 

# print(random.randint(1,2))#[1,2]
# print(random.randrange(1,2))#[1,2)

# print(float("12.3"))

#string 

# a="hello world"
# print(a,len(a),"hello" in a)
# if len(a)>5:
#     print("hello")
# # a[0]='p'#invalid string is immutable in python
# print(a)

#string slicing

# a="hello world"

# print(a[1:2])#a[1,2)

# print(a[::-1])

#string methods

# a='abcd fdh'
# print(len(a),a[0:1].upper(),a.split(' '))
# b="hello"
# print(a+" "+b,a+b)

#string format 
# print(f"hello world {5*2}")

#escape sequence

# print("hello \n world","hello\tworld","hello \\ world","hello\"\" world")
print("hello world".count("hello"))
print("hello world".find("world"))
