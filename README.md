# Data Structures and Algorithms in Python

## OOPs

Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to design applications and computer programs. It is a powerful tool that can be used to create flexible, reusable, and maintainable code.

### Principles of OOP:

#### 1. Encapsulation:
   - **Definition:** It is the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, known as a class.
   - **Purpose:** Encapsulation helps in hiding the internal details of the object and only exposes what is necessary.

#### 2. Inheritance:
   - **Definition:** It is a mechanism where a new class inherits properties and behaviors of an existing class.
   - **Purpose:** Inheritance promotes code reusability and establishes a relationship between the parent (base) and child (derived) classes.

#### 3. Polymorphism:
   - **Definition:** It allows objects of different classes to be treated as objects of a common base class.
   - **Purpose:** Polymorphism enables a single interface to represent different types of objects, making code more generic and adaptable.

#### 4. Abstraction:
   - **Definition:** It involves hiding the complex reality while exposing only the essential parts.
   - **Purpose:** Abstraction allows programmers to focus on relevant details, ignoring unnecessary complexities.

### Object-oriented programming in Python

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
```
This class defines a `Person` object with two attributes: `name` and `age`. It also defines a method called `greet()`, which prints a greeting to the user.

## Objects

An object is an instance of a class. To create an object, you use the `new` keyword followed by the name of the class and parentheses.

Here is an example of how to create an object:

```python
p = Person("Surya", 20)
```

This code creates a new `Person` object with the name "Alice" and the age 25.

## Methods

A method is a function that is defined inside a class. Methods are used to define the behavior of objects.

To call a method on an object, you use the dot notation. For example, to call the `greet()` method on the `p` object, you would use the following code:


```python
p.greet()
```

# Sorting techniques in Python

Sorting is a fundamental algorithm that is used in many different applications. There are many different sorting techniques available in Python, each with its own strengths and weaknesses.

**Some of the most common sorting techniques in Python include:**

* **Bubble sort:** Bubble sort is a simple sorting algorithm that works by repeatedly comparing adjacent elements in a list and swapping them if they are in the wrong order.
* **Selection sort:** Selection sort is another simple sorting algorithm that works by finding the smallest element in the unsorted list and swapping it with the first element. The algorithm then repeats this process with the remaining elements in the list.
* **Insertion sort:** Insertion sort is a sorting algorithm that works by inserting each element of an unsorted list into the sorted part of the list in its correct position.
* **Merge sort:** Merge sort is a divide-and-conquer sorting algorithm. It works by dividing the unsorted list into two halves, sorting each half recursively, and then merging the sorted halves back together.
* **Quicksort:** Quicksort is another divide-and-conquer sorting algorithm. It works by partitioning the unsorted list around a pivot element and then sorting the two sublists recursively.
