# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I learned how Python lists handle insertinos and deletions internally. Because lists are stored
as contiguous arrays, inserting or deleting near the front shifted every element after it, making those operations O(n),
while operations at the end were O(1). I also practiced writing a linear search manually and learned why it has to check elements one at a time in an unsorted list.
2. What challenges did you encounter, and how did you overcome them?
My first version used append() instead of insert, which ignored the index entirely. My first delete function also tried to use an attribute that Python lists don't have.
I fixed these by checking how each list method actually worked and testing my functions with different positions and edge cases, like invalid indices and empty lists.
3. How do list operations impact performance in real-world applications?
With small lists, the differences were barely noticeable, but with large datasets they added up quickly.
Applications that constantly insert at the front of search through unsorted data can slow down significantly, so choosing the right operation or data structure can make a real
difference in performance.
