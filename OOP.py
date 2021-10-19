class Dog:
    #class attribute
    species = "Canis familiaris"
    #initializing a class
    def __init__(self, name, age):
        self.name=name
        self.age=age

buddy=Dog('Buddy',9)
miles=Dog('Miles',4)

print(buddy.name)
print(buddy.age)
print(miles.name)
print(miles.age)

print(buddy.species)
print(miles.species)

buddy.age=10
print(buddy.age)

class Dog:
    #class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name=name
        self.age=age
    #instance methods
    def description(self):
        return (f"{self.name} is {self.age} years old")
    def speak (self,sound):
        return (f"{self.name} says {sound}")
miles=Dog("Miles",4)
print(miles.description())
print(miles.speak("Woof Woof"))
print(miles.speak("Bow Bow"))

names=["Fletcher", "David", "Dan"]
print(names)

class Dog:
    species="Canis familiaris"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
miles=Dog('Miles',4)
print(miles)

#Exercises
class Dog:
    species="Canis familiaris"
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def __str__(self):
        return f"{self.name}'s coat is {self.coat_color}"
philo=Dog('Philo',5,"Brown")
print(philo)


class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return f"The {self.color} has {self.mileage:,} miles."
blue_car=Car("blue", 20000)
red_car=Car("red", 30000)
print(blue_car)
print(red_car)


class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def drive(self,miles):
        self.mileage=self.mileage+miles
blue_car=Car("blue",0)
blue_car.drive(100)
print(blue_car.mileage)

class Dog():
    species= "Canis familiaris"

    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def speak(self,sound):
        return (f"{self.name} says {sound}")
    
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("Yap"))
print(jim.speak("Woof"))
print(jack.speak("Woof"))


class Dog():
    species= "Canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,sound):
        return (f"{self.name} says {sound}")

class JackRussellTerrier(Dog):
    pass
class Dachshund(Dog):
    pass
class Bulldog(Dog):
    pass

miles=JackRussellTerrier("Miles",4)
buddy=Dachshund("Buddy",9)
jack=Bulldog("Jack",3)
jim=Bulldog("Jim",5)

print(miles.species)
print(buddy.name)
print(jack)
print(jim.speak("Woof"))

print(type(miles))
print(isinstance(miles,Dog))


class JackRussellTerrier(Dog):
    def speak(self,sound="Arf"):
        return f"{self.name} says {sound}"
miles=JackRussellTerrier("Miles",4)
print(miles.speak())


class Dog:
    species= "Canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self,sound):
        return (f"{self.name} barks: {sound}")

class Bulldog(Dog):
    pass
jim=Bulldog("Jim",5)
print(jim.speak("Woof"))

miles=JackRussellTerrier("Miles",4)
print(miles.speak())


class JackRussellTerrier(Dog):
    def speak(self,sound="Arf"):
        return super().speak(sound)
miles=JackRussellTerrier("Miles",4)
print(miles.speak())