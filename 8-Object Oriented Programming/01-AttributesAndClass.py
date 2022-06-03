import os
os.system('cls')

#Creating a Class
class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'

    def __init__(self,breed,name):
        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        #Expect boolean True/False
        # self.spots = spots

    # ACTIONS / OPERATIONS --> Method
    # Dif between function and method is that method is inside of a class
    def bark(self,number):
        print("WOOF! My name is {} and the number is {}".format(self.name,number))


#Instance
my_dog = Dog(breed='Lab', name='Sam')
print(type(my_dog))

my_dog.bark(5)