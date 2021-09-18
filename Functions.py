#typing the name does not execute the function
#IDLE inspects the variable as usual
print(len)
#use parentheses to call the function
#(len())
#an error is raised when a function is called without an argument
#arguments are values assigned to a function as an input

num_letters=len("four")
print(num_letters)

#when you call the print function print() the displayed text is not a return value but a side effect of print()
return_value=print("What do i return?")

def multiply(x,y): #function signature
    product=x*y #function body
    return product

def greet(name):
    print(f"Hello, {name}!")

greet("Dave")
return_value=greet("Dave")

#adding docstrings to a function to note what the function is used for and the inputs or parameters expected
def multiply (x,y):
    """Returns the product of two numbers x and y."""
    product=x*y
    return product

help(multiply)

def cube(x):
    third_power=x**3
    return third_power


print(cube(3))

def greet(name):
    print(f"Hello, <{name}>!")


greet("name")


