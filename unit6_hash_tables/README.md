# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview
This assignment uses Python dictionaries to demonstrate hash table behavior.

For this assignment, I used a Python dictionary as a hash table to manage a small grocery store inventory. Each key was an item name, and each value was the quantity in stock. The program showed inserting, looking up, updating, and deleting items, and tested several edge cases. I also added a simple hash function that showed which bucket each item would go to in a small table, so collisions were easy to see in the output.

## Learning Objectives

* Insert key-value pairs
* Retrieve values efficiently
* Update existing values
* Remove entries
* Understand hashing concepts
### Insert key-value pairs
I created an empty dictionary called `inventory` and added six items: apples, bread, milk, eggs, cheese, and rice. I added comments explaining that Python hashed each key to decide where to store its value.

### Retrieve values efficiently
I looked up milk and cheese directly by key, and used the `in` operator to check whether eggs was in the inventory. I explained in the comments that lookups took O(1) time on average because Python went straight to the key's slot instead of searching every item.

### Update existing values
I changed the quantity of bread from 20 to 12 and added 25 to the apples. The program printed the inventory before and after, which showed that updating an existing key replaced its value instead of adding a second entry.

### Remove entries
I deleted rice using `del` and printed the inventory before and after. The other items were not affected.

### Understand hashing concepts
I wrote a `simple_bucket()` function that added up the character codes in a key and took the remainder after dividing by 7. This showed that milk and eggs both landed in bucket 2, and bread and rice both landed in bucket 6, which were collisions. I explained in the comments that a hash table handles collisions with chaining or with open addressing, which is what Python's dict uses, and that more collisions make lookups slower.

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.
### 1. Create and populate a dictionary
I created the `inventory` dictionary and added six items with their quantities. The program displayed the full inventory and the bucket index for each item.

### 2. Lookup operations
The program looked up milk (35 in stock) and cheese (15 in stock) and confirmed that eggs was in the inventory.

### 3. Update operations
The program updated bread to 12 and apples to 75, and displayed the inventory before and after the changes.

### 4. Delete operations
The program deleted rice and displayed the inventory before and after.

### 5. Edge cases
- **Lookup a missing key:** `inventory["bananas"]` raised a KeyError, so I caught it and showed that `get("bananas", 0)` safely returned 0 instead.
- **Delete a missing key safely:** `pop("rice", None)` returned None without crashing, even though rice had already been removed.
- **Update a missing key:** I showed that the program checked whether coffee existed before updating it, and that assigning to a missing key directly added it as a new item instead of causing an error.
- **Empty dictionary:** `len()`, `get()`, `in`, and `pop()` all worked on an empty dictionary without errors.
### 6. Real-world scenario
I used a grocery store inventory as my scenario. A store needs to quickly check, update, and remove items by name, and a hash table lets it do all of these in about the same amount of time no matter how many items it carries.

## Discussion Board Reflection
After completing the programming assignment, add this reflection to your initial discussion post in LEO.
Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
### My Reflection
This assignment helped me connect Python dictionaries, which I already use all the time, to how hash tables actually work. I learned how insert, lookup, update, and delete all use hashing to go straight to a key's location, and I practiced safer methods like get() and pop() for handling missing keys.

One challenge I had was that I could not see where Python actually stores each key, so I could not show collisions using the dictionary itself. I also learned that Python's hash() gives different results for strings each time the program runs. To fix this, I wrote a simple hash function that added up the character codes and took the remainder after dividing by 7, which showed the same collisions every run.

A hash table uses a hash function to turn a key into an index in an array, so it can find data without searching through everything. A collision happens when two keys get the same index. Collisions are handled with chaining or open addressing, but too many of them slow lookups down. When keys are spread out well, hash tables can insert, find, and delete data in O(1) time on average.
 