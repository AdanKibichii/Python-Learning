#creating a class, methods or objects and calling them out
class myClass():
    def method1(self):
        print ("Adan")
    def method2(self, someString):
        print ("Software Testing: " + someString)

def main():
    c=myClass()
    c.method1()
    c.method2("Testing is fun")

if __name__ == "__main__":
    main()
