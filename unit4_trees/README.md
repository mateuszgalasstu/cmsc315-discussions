# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
   I learned how to write recursive tree methods, especially the pattern where the insert helper returns the node reference so each parent keeps its link. I also learned why in-order traversal produces sorted output: the left-node-right order matches the BST rule at every level.
2. What challenges did you encounter, and how did you overcome them?
   My main challenge was the 1,000-node sequential test. It crashed with a RecursionError because the tree was 1,000 levels deep, past Python’s default recursion limit. I raised the limit for the demo, but the crash itself showed how badly an unbalanced tree performs. I also had to decide how to handle duplicates. Since employee IDs are unique, I chose to ignore them.
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
   A BST works like binary search on a sorted array, since each comparison removes half of the remaining data, but it allows inserts without shifting elements. A linked list or unsorted list needs O(n) searches, while a balanced BST needs O(log n). However, efficiency depends on insertion order. Sequential IDs turned my tree into a linked list needing 1,000 comparisons, while a balanced order needed only 9. Self-balancing trees like AVL or red-black trees fix this.