# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

## Implementation Documentation
# Unit 1: Python OOP, Namespaces, and Copying

## Implementation

**Parent class.** I created an `Animal` class with a class variable `is_alive` set to `True`, and two instance variables, `name` and `age`, set in the constructor. I also added a `get_info()` method that returned a description of the animal.

**Child class.** I created a `Dog` class that inherited from `Animal`. It added a class variable `species` and two new instance variables, `breed` and `is_trained`. I used `super().__init__()` so the parent class handled `name` and `age`. I added a new `bark()` method and overrode `get_info()` to include the dog's species and breed.

**Namespaces.** In `demonstrate_namespaces()`, I created two dogs, Sparky and Rocky. I accessed `species` through the `Dog` class and through each object to show that objects could read class variables. I then added a `favorite_food` attribute to Sparky only and printed both objects' `__dict__`, which showed the new attribute in Sparky's instance namespace but not Rocky's. Finally, I printed `Dog.__dict__` to display the class namespace.

**Copying.** In `demonstrate_copying()`, I created a dog named Max with a nested `tricks` list, then made a shallow copy with `copy()` and a deep copy with `deepcopy()`. After I appended a new trick to the original's list, the shallow copy showed the change because it shared the same list, while the deep copy stayed the same because it had its own copy of the list.

**Main.** In `main()`, I created an `Animal` object and a `Dog` object, called `get_info()` on both to show method overriding, called `bark()` on the dog, and then ran both demonstration functions.

## How to Run

    unit1_discussion.py