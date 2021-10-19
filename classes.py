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


#no2
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


#ex3
class User:
    name=""
    
    def __init__(self,name):
        self.name=name
    
    def sayHello(self):
        print("Welcome to Guru99, " + self.name)

User1=User("Alex")
User1.sayHello()


#super function
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2*self.width

class Square:
    def __init__(self, length):
        self.length=length
    def area(self):
        return self.length * self.length
    def perimeter(self):
        return 4*self.length

square=Square(4)
print(square.area())
print(square.perimeter())

rectangle=Rectangle(2,4)
print(rectangle.area())
print(rectangle.perimeter())



class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2*self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)

square=Square(4)
rectangle=Rectangle(2,4)
print(square.area())
print(rectangle.area())
print(square.perimeter())
print(rectangle.perimeter())