# Data Structures and Algorithms in Python 

## Oops

\section{Object-oriented programming in Python}

Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to design applications and computer programs. It is a powerful tool that can be used to create flexible, reusable, and maintainable code.

In Python, OOP is implemented through classes and objects. A class is a blueprint for creating objects, and an object is an instance of a class. Objects have their own state and behavior, and they can interact with each other through methods.

**Object-oriented programming in Python**

## Classes

A class is a blueprint for creating objects. It defines the attributes and behaviors of the objects that will be created from it.

To create a class, you use the `class` keyword followed by the name of the class and a colon. The body of the class is indented.

Here is an example of a class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")


This class defines a `Person` object with two attributes: `name` and `age`. It also defines a method called `greet()`, which prints a greeting to the user.

## Objects

An object is an instance of a class. To create an object, you use the `new` keyword followed by the name of the class and parentheses.

Here is an example of how to create an object:

python
p = Person("Surya", 20)


This code creates a new `Person` object with the name "Alice" and the age 25.

## Methods

A method is a function that is defined inside a class. Methods are used to define the behavior of objects.

To call a method on an object, you use the dot notation. For example, to call the `greet()` method on the `p` object, you would use the following code:

python
p.greet()

