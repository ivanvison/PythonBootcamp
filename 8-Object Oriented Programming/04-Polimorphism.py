import os
os.system('cls')

class Dog():

    def __init__(self,name):

        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():

    def __init__(self,name):

        self.name = name

    def speak(self):
        return self.name + " says meow!"

lucy = Dog(name='Lucy')
misha = Cat(name='Misha')
# print(lucy.speak())
# print(misha.speak())

for pet in [lucy,misha]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

#ABSTRACT
class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

fido = Dog("Fido")
sis = Cat("Sis")
fido.speak()
sis.speak()