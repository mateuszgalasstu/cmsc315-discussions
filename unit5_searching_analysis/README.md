# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

For this assignment, I implemented both search algorithms in Python and tested them using a student ID lookup scenario. I ran each search on a small class roster, a large set of student records, and several edge cases, and the program printed the result, the number of comparisons, and the time for every search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency
### Implement linear search
I wrote `linear_search` with a loop that checked each item from the start of the list to the end. It returned the index when it found the target and returned -1 if it reached the end without finding it. I added comments explaining that it was O(n) because, in the worst case, it had to check every item once.

### Implement binary search
I wrote `binary_search` using `low` and `high` variables to track the part of the list that was still being searched. Each time through the loop, it checked the middle item. If the middle value was too small, it moved `low` past the middle, and if it was too large, it moved `high` below the middle. This cut the search space in half every time. I added comments explaining that this made it O(log n).

### Compare performance
I added an optional `stats` parameter to both functions so they could count how many comparisons they made, without changing what they returned. I also added a `run_search` helper function that timed each search and printed the results in the same format.

### Analyze algorithm efficiency
The results showed that binary search was much more efficient on large data. On 1,000,000 IDs, linear search needed about 1,000,000 comparisons, while binary search needed about 20. Since log2(1,000,000) is about 20, this matched the O(log n) expectation.

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.
### 1. Small dataset
I created a sorted class roster of 10 student IDs. When searching for ID 1421, linear search found it at index 7 in 8 comparisons, and binary search found it in 2. When searching for ID 1300, which was not in the list, both returned -1. Linear search took 10 comparisons and binary search took 3.

### 2. Large dataset
I created a sorted list of 1,000,000 student IDs. For an ID near the end of the list, linear search took 999,991 comparisons and binary search took 19. For an ID that was not in the list, linear search took 1,000,000 comparisons and binary search took 20.

### 3. Edge cases
- **Empty list:** Both searches returned -1 without any errors.
- **Single-element list:** Both searches found the item in one comparison and returned -1 in one comparison when it was missing.
- **First position:** Linear search found it in 1 comparison, while binary search took 3. This showed that binary search is not faster in every single case.
- **Last position:** Linear search took 10 comparisons and binary search took 4.
- **Unsorted list:** Binary search returned -1 for ID 1563 even though it was in the list, while linear search still found it. This showed that binary search only works on sorted data.
### 4. Performance analysis
On the small list, both searches finished in a few microseconds, so the difference did not really matter. On the large list, linear search took tens of milliseconds, while binary search took about 0.01 ms. The comparison counts showed the reason. Linear search's work grew at the same rate as the list, but binary search only needed one extra comparison each time the list doubled in size.

### 5. Real-world search scenario
I used a university student records system as my scenario. A small class roster is easy to check one ID at a time, but a large records system needs to be kept sorted by ID so that binary search can find a student quickly.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
### My Reflection

This assignment helped me understand the difference between O(n) and O(log n) much better than just reading about it. Counting the comparisons made it clear, since linear search went from 10 comparisons to about 1,000,000, while binary search only went from 3 to 20. I also got more practice with tracking the low, high, and middle positions in a loop.

One challenge I had was with my unsorted list test. The first ID I picked happened to be right in the middle of the list, so binary search found it on the first try, and the test did not show anything. I fixed this by choosing an ID that binary search would skip past, which showed it returning -1 for a value that was actually in the list.

Linear search is the better choice for small or unsorted lists, or lists that change often, like a class sign-in sheet, because sorting first would take more time than just searching. Binary search is better for large lists that stay sorted, like a student records system, but the tradeoff is that the data has to be sorted and kept that way.
 