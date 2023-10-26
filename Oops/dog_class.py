#Creating a class

class Dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self , age):
        self.age = age

    def bark(self):
        print('woof')

d = Dog('husk' , 2)
print(d.get_age())

print(d.get_name())
d.bark()
d.set_age(24)
print(d.get_age())
print(type(d))

