# we use constructors so we add the values within our code
class Person:
    def __init__(self,name): #init is short for initialise, this is a method that gets called when we creaye a new point  object
        self.name = name
    def talk(self):
        print(f"Hello,I am {self.name}")


point = Person("Tala Alqam")
point2 = Person("mosh ana")
point.talk()
point2.talk()
#each object is a different instance of a person class