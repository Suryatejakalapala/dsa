class Pet:
    def __init__(self , name , age):
        self.name = name 
        self.age = age
    def show(self):
        print(f'i am {self.name} and i am {self.age} years old')

    def speak(self):
        print('i dunno what to say')

class Dog(Pet):
    def speak(self):
        print('bark')

class Cat(Pet):
    def __init__(self , name , age , color):
        super().__init__(name , age)
        self.color = color
        
    def speak(self):
        print('meow')
    def show(self):
        print(f'i am {self.name} and i am {self.age} years old and i am {self.color}')

class Fish(Pet):
    pass
c = Cat('mill' , 23  , 'blue')
c.show()
c.speak()

d = Dog('barg' , 23)
d.show()
d.speak()

f = Fish('bubbles' , 12)
f.speak()