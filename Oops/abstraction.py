# Abstraction is a programming concept that allows us to hide the implementation details of a piece of code and expose only its essential functionality

#python doesnt have abstraction by default but we can achieve it by the module abc (abstract base class)

from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self): # the decorator @abstractmethod makes this method explicitly as abstractmethod which means the subclass must consists this method
        pass

class Circle(Shape):
    def __init__(self , radius ):
        self.radius = radius
    def area(self , radius):
        return 3.14 * radius * radius
    
    def perimeter(self , radius):
        return 2 * 3.14 * radius 
    
class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self , length , width):
        return length * width
    
    def perimeter(self , length , width):
        return 2*(length + width)
    

c = Circle(5)
print(c.area(5))
print(c.perimeter(5))

