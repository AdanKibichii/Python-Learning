class Dog:
    #class attribute
    species="Canis familiaris"

    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def speak(self,sound):
        return f"{self.name} says {sound}"
