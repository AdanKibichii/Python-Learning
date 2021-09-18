#Numbers and Math
num1=float(input("Enter the first number(base): "))
num2=int(input("Enter the second number(exponent): "))
num3=num1**num2
print("1.2 to the power of 3 =", num3)
print(f"1.2 to the power of 3 = {num3}")
#round and power or exponent **
print(round(2.3))
print(pow(2,3))
print(pow(2,-2))
#adding the third argument to return a modulus %
print(pow(2,3,2))

#number method
num=2.5
print(num.is_integer())

num=2.0
print(num.is_integer())

number=float(input("Enter a number: "))
number=round(number, 2)
print(number)


number=float(input("Enter a number: "))
number=round(number, 2)
print(f"5.432 rounded off to 2 is {number}")

number=int(input("Enter a number: "))
number=abs(number)
print(f"The absolute value of -10 is {number}")

num1=float(input("Enter a number: "))
num2=float(input("Enter another number: "))
num3=num1-num2
print(f"The difference between 1.5 and 1.0 is an integer? {num3.is_integer()}")


#formating numbers to 2 decimal places or 1 decimal place
n=7.125
print(f"The value of n is {n:.2f}")

n=7.126
print(f"The value of n is {n:.1f}")

n=1
print(f"The value of n is {n:.2f}")

n=1
print(f"The value of n is {n:.3f}")

n=1234567890
print(f"The value of n is {n:,}")

#rounding of decimal places and putting round commas to a thousand
n=1234.56
print(f"The value of n is {n:,.2f}") # the specifier ,.2f is very useful in displaying currencies

n=1234.56
print(f"The value of n is {n:,.3f}")

#example
balance=2000.0
spent=256.35
remaining=balance-spent
print(f"After spending ${spent:.2f}, I was left with ${remaining:,.2f}")

num1=int(input("Enter a number: "))
num2=float(input("Enter another number: "))
print(f"The difference between {num1} and {num2} is {num1-num2}")

#printing a percentage amount using the :.% percentage calculation
n=0.08
print(f"The percentage of {n:.1%}")


ratio=0.8
print(f"Over {ratio:.1%} Pythonistas say 'Real Python Sucks!")
print(f"Over {ratio:.2%} Pythonistas say 'Real Python Sucks!")

n=3**.125
print(f"{n:.3f}")

number=150000
print(f"{number:,.2f}")

#complex numbers
n=1+2j
print(n)
print(n.real)
print(n.imag)

a=1+2j
b=3-4j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

#integers and floats also have their real and imaginary value
x=42
print(x.imag)
print(x.real)
print(x.conjugate())

y=3.14
print(y.imag)
print(y.real)
print(y.conjugate())







