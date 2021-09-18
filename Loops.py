n=1
while n<5:
    print (n)
    n=n+1

#while loops are used in asking a user or code to repeat a particular code or information until the condition is met
num=float(input("Enter a positive number: "))
while num<=0:
    print("Thats not a positive number!")
    num=float(input("Enter a positive number: "))

for letter in "Python":
    print(letter)


word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index = index + 1

for n in range(3):
    print("Python")


for n in range(10,20):
    print(n*n)

amount=float(input("Enter an amount: "))
for num_people in range (2,6):
    print(f"{num_people} people: ${amount/num_people:,.2f} each")


#Nested loops
for n in range(1,4):
    for j in range(4,7):
        print(f"n={n} and j={j}")

#loops exercises
for n in range (2,11):
    print(n)

#while loops
n=2
while n<11:
    print(n)
    n=n+1

def invest (amount, rate, years):
    for year in range (1, years+1):
        amount=amount * (1+rate)
        print(f"year {year}: ${amount:,.2f}")

amount=float(input("Enter the principal amount: "))
rate=float(input("Enter the rate of return per year: "))
years=int(input("Enter the number of years: "))

invest (amount, rate, years)

x=2
def doubles(x):
    y=x*2
    return y
print(doubles(x))

for i in range(1, 3):
    z=i*2
    print(doubles(x)*z)


Example
def add_underscores(word):
    new_word = "_"
    for i in range (0, len(word)):
        new_word=word[i] + "_"
    return new_word


phrase="hello"
print(add_underscores(phrase))

def add_underscores(word):
    new_word = "_"
    for i in range (0, len(word)):
        new_word=new_word+ word[i] + "_"
    return new_word


phrase="hello"
print(add_underscores(phrase))

sport=input("Enter a sport: ")
p1_score=int(input("Enter player 1 score: "))
p2_score=int(input("Enter player 2 score: "))

if sport.lower()=="basketball":
    if p1_score==p2_score:
        print("The game is a draw")
    elif p1_score>p2_score:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

elif sport.lower()=="golf":
    if p1_score==p2_score:
        print("The game is a draw")
    elif p1_score>p2_score:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

else:
    print("unknown sport")

word=input("Enter a word: ")
if len(word)==5:
    print("Word is equal to 5 characters: ")
elif len(word)<5:
    print("Word is greater than 5 characters: ")
else:
    print("Word is greater than 5 characters: ")


num=int(input("Enter a positive value: "))
for divisor in range (1, num+1):
    if num % divisor==0:
        print(f"{divisor} is a factor of {num}")

sum_of_evens=0
for n in range(1,100):
    if n%2==0:
        sum_of_evens=sum_of_evens+n

print(sum_of_evens)

sum_of_odds=0
for n in range(1,100):
    if n%2==1:
        sum_of_odds=sum_of_odds+n

print(sum_of_odds)

for n in range (0,4):
    if n==2:
        break
    print(n)

print(f"Finished with n = {n}")


for i in range (0,4):
    if i==2:
        continue
    print(i)

print(f"Finished with i = {i}")

for n in range(3):
    password = input("Password: ")
    if password == "I<3Bieber":
        break
    print("Password is incorrect.")
else:
    print("Suspicious activity. The authorities have been alerted.")

for i in range(5):
    key=input("Enter keys: ")
    if key.lower()=="q":
        break
    print("Incorrect key")


for i in range (1,10):
    if i%3==0:
        continue
    print(i)
