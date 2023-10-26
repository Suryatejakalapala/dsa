class Person:
    number_of_people = 0

    def __init__(self , name , age):
        self.name = name 
        self.age = age
        self.add_people()
    
    @classmethod
    def no_of_people(cls):
        return cls.number_of_people
    
    
    @classmethod
    def add_people(cls):
        cls.number_of_people += 1

p1 = Person('surya' , 20)
print(p1.no_of_people())
p2 = Person('janesh' , 23)
print(p2.no_of_people())