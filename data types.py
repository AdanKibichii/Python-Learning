if 5>2:
    print("Five is greater than two!")
if 5>2:
        print("Five is greater than two!")
#this is a comment
x=5
y="Hello, John!"
print(x)
print(y)

x=4
x="John"
print(x)
print(type(x))

x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)

x,y,z="Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x=y=z="Oranges"
print(x)
print(y)
print(z)

fruits=["Oranges", "Banana", "Cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

x="Awesome"
print("Python is " + x)

x="Python is "
y="Awesome"
z=x+y
print(z)


x=5
y=7
print(x+y)

#when creating a variable inside a function is is referred to as a local variable meaning can only be used in that function
x="Awesome"
def myfunc():
    x = "Fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)


x="Awesome"
def myfunc():
    print("Python is " + x)


myfunc()


#However by inputting the global keyword you make the local variable converted into a global variable
x="Awesome"
def myfunc():
    global x
    x="Fantastic"


myfunc()
print("Python is " + x)

#getting a data type
x=5
print(type(x))
#data types in python are set once a value is assigned to a variable
#x = "Hello World" #str()
#x = 20 #int()
#x = 20.5 #float()
#x = 1j #complex()
#x = ["apple", "banana", "cherry"] #list()
#x = ("apple", "banana", "cherry") #tuple()
#x = range(6) #range()
#x = {"name" : "John": "age" : 36} #dict()
#x = {"apple", "banana", "cherry"} #set()
#x = frozenset({"apple", "banana", "cherry"}) #frozenset()
#x = True #bool()
#x = b"Hello" #bytes()
#x = bytearray(5) #bytearray()
#x = memoryview(bytes(5)) #memoryview()

x=2
y=1.1
z=1j
print(type(x))
print(type(y))
print(type(z))

#floats can also be scientific numbers containing the 'e' indicating power of
x=35E3
print(type(x))
print(type(y))

#converting data types
x=2 #int
y=2.8 #float
z=2j #complex

a=float(x) #converting int to a float
b=int(y) #converting float to int
c=complex(x) #converting int to complex
print(type(a))
print(type(b))
print(type(c))

#creating and using random numbers
import random
print(random.randrange(1,10))

#python casting is where the type of data in a variable is specified using constructors
str()
float()
int()
#assigning multiple strings to a variable is done by inputting three quotes
a="""hey Ngendo,
hope you doing well today,
i wish you a good day today,
and a good week"""
print(a)

a="Hello World"
print(a[0])
print(a[-1])

#printing the length of a string
x="hello, world"
print(len(x))

#checking a string using in
txt="best things in life are free"
print("free" in txt)

#using if
txt="best things in life are free"
if "free" in txt:
    print("yes, 'free' is present.")


#using nots
txt="best things in life are free"
print('expensive' not in txt)

txt="best things in life are free"
if 'expensive' not in txt:
    print("No, 'expensive' not in txt.")

#slicing strings is done when one wants to return a range of characters in a string or slice syntax
c="Hello, World"
print(c[2:5])
print(c[:5])
print(c[2:])
print(c[-5:-2])

#upper and lower methods
a="hello world"
print(a.upper())
print(a.lower())

#removing white spaces
a=" hello world! "
print(a.strip())

#replacing a character in a string
a="hello world"
print(a.replace("h","J"))

#spliting strings into substrings
a="hello, world!"
print(a.split(","))

#combining strings
a="Hello "
b="World"
c=a+b
print(c)

#adding spaces to a string
a="Hello"
b="World"
print(a+ " " + b)

#format strings
age=35
txt="my name is john, and i am {}"
print(txt.format(age))

weight=60
txt="i am adan, and i am (kgs) {}"
print(txt.format(weight))

quantity=80
item_no=54
price=444
myorder="i want {} number of items {} with a total price of {}"
print(myorder.format(quantity,item_no,price))

#indexing
quantity=80
item_no=54
price=444
myorder="I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity,item_no,price))

#escape characters by use of \\
#for example inserting a string with double quotes in a string already containing double quotes
txt="we are the so-called \"Vikings\" from the north"
print(txt)

#Booleans True or False
print(10>9)
print(10<9)
print(10==9)

a=200
b=33
if b>a:
    print("b is greater than a" )
else:
    print("a is greater than b")

#evaluating a strinbg and a value
print(bool("Hello"))
print(bool(15))
