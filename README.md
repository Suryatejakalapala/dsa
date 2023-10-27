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

This code creates a new `Person` object with the name "Surya" and the age 20.

## Methods

A method is a function that is defined inside a class. Methods are used to define the behavior of objects.

To call a method on an object, you use the dot notation. For example, to call the `greet()` method on the `p` object, you would use the following code:


```python
p.greet()
```

# Sorting techniques in Python

Sorting is a fundamental algorithm that is used in many different applications. There are many different sorting techniques available in Python, each with its own strengths and weaknesses.

**Some of the most common sorting techniques in Python include:**

## Bubble sort:
- **Bubblesort is a simple sorting algorithm that works by repeatedly comparing adjacent elements in a list and swapping them if they are in the wrong order. Bubble sort has a best case time complexity of O(n), which occurs when the list is already sorted. However, bubble sort has an average and worst case time complexity of O(n^2), which makes it inefficient for large lists.**

## Selection sort:
- **Selectionsort is another simple sorting algorithm that works by finding the smallest element in the unsorted list and swapping it with the first element. The algorithm then repeats this process with the remaining elements in the list. Selection sort has a time complexity of O(n^2) in all cases.**

## Insertion sort 
- **Insertionsort is a sorting algorithm that works by inserting each element of an unsorted list into the sorted part of the list in its correct position. Insertion sort has a best case time complexity of O(n), which occurs when the list is already nearly sorted. However, insertion sort has an average and worst case time complexity of O(n^2), which makes it inefficient for large lists**

## Merge sort 
- **Mergesort is a divide-and-conquer sorting algorithm. It works by dividing the unsorted list into two halves, sorting each half recursively, and then merging the sorted halves back together. Merge sort has a time complexity of O(n log n) in all cases, which makes it a more efficient sorting algorithm than bubble sort, selection sort, and insertion sort for large lists.**

## Quicksort 
- **Quickort is another divide-and-conquer sorting algorithm. It works by partitioning the unsorted list around a pivot element and then sorting the two sublists recursively. Quicksort has a time complexity of O(n log n) in the average case, but it can have a worst case time complexity of O(n^2). However, the worst case of quicksort is very rare, and quicksort is generally a very efficient sorting algorithm for large lists.**

## Time Complexity of the Sorting Algorithms 

| Sorting Technique | Best case | Average case | Worst case |
|---|---|---|---|
| Bubble sort | O(n) | O(n^2) | O(n^2) |
| Selection sort | O(n^2) | O(n^2) | O(n^2) |
| Insertion sort | O(n) | O(n^2) | O(n^2) |
| Merge sort | O(n log n) | O(n log n) | O(n log n) |
| Quicksort | O(n log n) | O(n log n) | O(n^2) |





