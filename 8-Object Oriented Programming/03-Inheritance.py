import os
os.system('cls')

class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am a dog and eating")

#myanimal = Animal()
#myanimal.who_am_i()
#myanimal.eat()

mydog = Dog()
mydog.who_am_i()
mydog.eat()

