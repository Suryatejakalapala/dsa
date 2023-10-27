# Method Overloading is a way to implement polymorphism through multiple methods with the same name but different parameters

# PYTHON DOES NOT SUPPORT METHOD OVERLOADING
# THIS IS JUST A WAY TO SHOW 
# IN PYTHON THE SECOUND METHOD WILL TAKEOVER 
class Calculator:
    def add(self , a , b):
        return a + b
    def add(self , a , b , c):
        return a + b + c
    
c = Calculator()

print(c.add(2 , 4))
print(c.add(1 , 2 , 3))

# Polymorphism allows you to write more flexible and extensible code by enabling objects of different types to respond to the same method or function call in a way that is appropriate for thier individual types