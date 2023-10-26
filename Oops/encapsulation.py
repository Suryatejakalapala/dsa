# Encapsulation is a way to restrict the direct access to some components of an object


class Student:
    def __init__(self , name , age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self , new_age):
        if 0 < new_age <= 150:
            self.__age = new_age

s = Student('Ali' , 20)

print(s.name)
print(s.get_age())
print(s.__age)
s.set_age(22)
print(s.get_age())