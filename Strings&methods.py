i=1
while i<=1:
    i<=2
    1<=2
    i<=1
    print("*"*19)
    print("*" "                 " *2)
    print("*" "                 " * 2)
    print("*" * 19)
    i=i+1

for i in range(1,2):
    print("*" * 19)
    print("*" "                 " * 2)
    print("*" "                 " * 2)
    print("*" * 19)

i=1
while i<=4:
    print("*"*19)
    i=i+1

for i in range(1,5):
        print("*"*19)

i=1
while i<=4:
    print("*"*i)
    i=i+1

i=1
for i in range(1,5):
    print("*"*i)

i=1
while i<=1:
    i<=2
    1<=2
    i<=1
    print("*"*19)
    print("*" "                 " *2)
    print("*" "                 " * 2)
    print("*" * 19)
    i=i+1

i=1
while i<=4:
    print("*"*19)
    i=i+1

i=1
while i<=4:
    print("*" * i)
    i = i+1

i=1
for i in range(1,5):
    print("*"*i)

letters="abc"
num_letters=len(letters)
print(num_letters)

#writing strings with many lines requires separation of the lines with a backlash
paragraph="This planet has - or rather had - a problem, which was\
this: most of the people living on it were unhappy for pretty much\
of the time. Many solutions were suggested for this problem, but\
most of these were largely concerned with the movements of small\
green pieces of paper, which is odd because on the whole it wasn't\
the small green pieces of paper that were unhappy."

print(paragraph)

#using triple quotes
paragraph="""This planet has - or rather had - a problem, which was\
this: most of the people living on it were unhappy for pretty much\
of the time. Many solutions were suggested for this problem, but\
most of these were largely concerned with the movements of small\
green pieces of paper, which is odd because on the whole it wasn't\
the small green pieces of paper that were unhappy."""
print(paragraph)

#preserving white spaces
print("""An example
     of a string spanning multiple lines
         and preserves white spaces""")


first_name="Adan"
second_name="Kiprotich"
full_name=first_name + " " + second_name
print(full_name)

#indexing
flavor="Apple pie"
print(flavor[1])
print(flavor[0:3])
print(flavor[:14])

word="goal"
word="f" +word[1:]
print(word)

name="Adan Kibichii"
name="E" + word[1:]
print(name)

name="Adan Kibichii"
name_length=len(name)
print(name_length)

name="adan kibichii"
print(name.upper())

# removing whitespaces using string left and right side
name="adan kibichii     "
print(name.rstrip())

name="    adan kibichii"
print(name.lstrip())

#removing whitespaces on both sides of a string
name="     adan kibichii     "
print(name.strip())

#determining if a string contains a particular string
starship="Enterprise"
print(starship.startswith("en"))
print(starship.endswith("se"))

greeting=input("Hey, What's up? ")
print("You said:", greeting)

prompt="Hey Whats'up? "
user_input=input(prompt)
print("You said:", user_input)

response=input("What should i shout? ")
shouted_response=response.upper()
print("Well if you insist...", shouted_response)

response=input("What should i shout? ")
print("Well if you insist...", response.upper())

response=input("What should i shout? ")
print("Well if you insist...", response.__len__())

script=input("Tell me your password: ")
script_firstletter=script.upper()
print("The entered password was:", script_firstletter[0])


#using the sep"" operator
x=int(input("Enter a number: "))
print(x,2*x,3*x,4*x,5*x, sep="---")

password=input("Tell me your password:")
password2= password.upper()
print("The first letter you entered was: ", password2[0])

weight_kgs=int(input("what your weight in Kg: "))
weight_pounds=weight_kgs/0.45
print(weight_pounds)

#a string always generates a string result and must be coonverted to an int() or float() to run
num=int(input("Enter a number to be doubled: "))
doubled_num=num*2
print(doubled_num)

num=input("Enter a number to be doubled: ")
doubled_num=int(num)*2
print(doubled_num)

x= int(input("Enter a number to be squared: "))
x_squared=x*x
print("the squared value is", x_squared)

pancakes_total=10
pancakes_eaten=5
print("only ", pancakes_total-pancakes_eaten, "pancakes left.")

value=int("2")*2
print(value)


num1=2
num2=4
num3=float(num1*num2)
print("The product of 2 and 4 is ", num3)

#various ways of printing strings and additing variables to strings
name="Zaphod"
heads=2
arms=3
print(name, "has ", + heads, "and", + arms, "arms")
print(name + " has " + str(heads) + " and " + str(arms) + " arms ")
print(f"{name} has {heads} heads and {arms} arms")

#adding a python expression in the curly brackets formated strings
n=3
m=4
print(f"{n} times {m} is {n*m}")

Weight=0.2
animal= "newt"
print(str(Weight)+" kg" + " is the weight of the " + str(animal))
print(f"{Weight} kg is the weight of the {animal}")

#using the find() method in strings
phrase="the surprise is in here somehwere"
print(phrase.find("surprise"))
print(phrase.find("hshshshs"))
print("the surprise is in here somewhere".find("surprise"))

print("My number is 555-555-5555".find("5"))

#using the replace method
my_story="i am telling you the truth, nothing but the truth"
print(my_story.replace("the truth", "lies"))
my_story=my_story.replace("the truth", "lies")
print(my_story)

text="some of the stuff"
new_text=text.replace("some of", "all")
new_text=new_text.replace("stuff", "things")
print(new_text)

name=input("What is your name? ")
print(name.find("d"))


text=input("Enter some text: ")
text1=text.replace("I like to eat eggs and spam", "leetspeak")
print(text1)

text=input("Enter some text: ")
text2=text.replace("a", "4")
text2=text2.replace("e", "3")
text2=text2.replace("o", "0")
text2=text2.replace("s", "5")
text2=text2.replace("t", "7")
print(text2)

text=input("Enter some text: ")
new_text=text.replace("I like to eat eggs and spam", "leetspeak")
new_text2=text.replace("a", "4")
new_text2=new_text2.replace("e", "3")
new_text2=new_text2.replace("1", "1")
new_text2=new_text2.replace("o", "0")
new_text2=new_text2.replace("s", "5")
new_text2=new_text2.replace("t", "7")
print(new_text)
print(new_text2)

