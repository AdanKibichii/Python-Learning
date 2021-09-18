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

