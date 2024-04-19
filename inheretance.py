#inheretance is supported by multiple coding languages
#instead of recalling a function way to many times and edit each one individually
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def Bark(self):
        print("Bark")
    pass #instead of leaving this empty we can use "pass"
         #we are telling the terminal pass this line dont worry about it
dog1 = Dog()
dog1.Bark()