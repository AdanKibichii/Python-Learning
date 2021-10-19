#initiating class instances in another class
class myClass():
    def method1(self):
        print ("Adan")
        
class childClass(myClass):
    def method2(self):
        print("childClass method2")
        
def main():
    c=childClass()
    c.method1()
    c.method2()
    
if __name__ == "__main__":
    main()
