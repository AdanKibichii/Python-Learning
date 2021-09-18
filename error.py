#errors
try:
    number=int(input("Enter an integer: "))
except ValueError:
    print("Thats not an integer")

def divide(num1, num2):
    try:
        print(num1/num2)
    except (ValueError, TypeError):
        print("Encountered a problem")



try:
    number=int(input("Enter an integer: "))
except ValueError:
    print("try again")
    number=int(input("Enter an integer: "))

word=input("Enter a word: ")
num=int(input("Enter a number: ")
try:
    print(word[num])
except ValueError:
    print("Enter an integer")