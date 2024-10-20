# a='hello world' #this is variable 
# a=str('50')
# print(a,type(a)) #this is print function
# print(a) #this is print function

# a,b,c=10,20,30
# a=b,c=10,20
# print(type(a),b,c)
# c,d,e=[20,30,40]
# f,g,h=[10,20,30]
# print(c,d,e,f,g,h)

# a,b,c='a','b','c'
# print(a+b+c)

x = "awesome"

def myfunc():
  global x 
  x="fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)