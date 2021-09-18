#packing and unpacking
coordinates=4.21,9.29
print(type(coordinates))
x,y=coordinates
print(x)
print(y)

name, age, occupation= "David", 34, "programmer"
print(name)
print(age)
print(occupation)

def adder_substrator(num1, num2):
    return (num1+num2, num1-num2)

print(adder_substrator(3,2))

cardinal_numbers=("first", "second", "third")
print(cardinal_numbers[1])
position1, position2, position3=cardinal_numbers
print(position1)
print(position2)
print(position3)

my_name="Adan"
my_name=tuple("Adan")
print("x" in my_name)

my_name="Adan"
print(my_name[1:4])