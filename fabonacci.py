numbers=int(input("How may fibonacci numbers to print? "))
n1=0
n2=1
count=0
if numbers <=0:
    print("Please enter a positive integer")
elif numbers==1:
    print("print fibonacci sequence upto numbers", numbers, ":" )
else:
    print("fibonacci sequence:")
    while count< numbers:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1




