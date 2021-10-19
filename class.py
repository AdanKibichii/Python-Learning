#working with classes
class myClass():
    def method1(self):
        print ("Adan")
    def method2(self,someString):
        print ("Software Testing:" + someString)

def main():
    c=myClass()
    c.method1()
    c.method2("Testing is fun")

if __name__ == "__main__":
    main()

#exercise 2
class myClass():
    def method1(self):
        print ("Adan")

class childClass(myClass):
    def method2(self):
        print ("child class method2")

def main ():
    c2=childClass()
    c2.method1()
    c2.method2()

if __name__ == "__main__":
    main()

#exe3
class User:
    name=""

    def __init__(self,name):
        self.name=name

    def sayHello(self):
        print("Welcome to Guru99, " +self.name)
user1=User("Alex")
user1.sayHello()
