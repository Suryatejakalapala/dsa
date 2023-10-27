# Method Overriding is way a to implement polymorphism through inheritance 

class Animal:
    def speak(self):
        pass # this method will overriden in subclass

class Dog(Animal):

    def speak(self):
        return 'bark!'
    
d = Dog()

print(d.speak())