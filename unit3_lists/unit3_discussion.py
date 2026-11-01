"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.
    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    ## Inserting at the beginning shifts every element
    ## O(n) in the slowest case
    ## Inserting in the middle would shift around half, so still O(n)
    ## Inserting at the end shifts nothing so O(1) in the best case
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if index < 0 or index >= len(lst):
        return None

    removed = lst.pop(index)
    return removed


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for i, item in enumerate(lst):

        if item == value:
            return i

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    ## Starting with a small list of values
    nums = [10, 20, 30, 40, 50]
    print("Original list:", nums)

    ##Insert at index 0, every already existing element shifts one to the right
    insert_at(nums, 0, 5)
    print("After inserting 5 at the beginning:", nums)

    ## Insert in the middle. Only the elements after the middle
    ## index shift right, so still O(n)
    middle = len(nums) // 2
    insert_at(nums, middle, 25)
    print(f"After inserting 25 at index {middle} (middle):", nums)

    ## Insert at the end (index == len). Nothing needs to shift
    ## At the best case: O(1)
    insert_at(nums, len(nums), 60)
    print("After inserting 60 at the end:", nums)
    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    ## Delete from the beginning, all remaining elements shift left
    ## to fill the gap: O(n)
    removed = delete_at(nums, 0)
    print("Removed from beginning:", removed, "-->", nums)

    ## Delete from middle. Elements after index shift left
    middle = len(nums) // 2
    removed = delete_at(nums, middle)
    print(f"Removed from index {middle} (middle):", removed, "-->", nums)

    ## Delete from end, no shifting needed
    removed = delete_at(nums, len(nums) - 1)
    print("Removed from end:", removed, "-->", nums)

    print("\n=== SEARCH TESTS ===")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    ## Search for a value that exists, the linear search
    ## checks each element in order until it finds a match
    target = 25
    result = search_value(nums, target)
    print(f"Searching for {target}: found at index {result}")

    ## Search for a value that doesn't exist, the search must check
    ## every element before concluding that it's missing.
    ## worst case: O(n)
    target = 99
    result = search_value(nums, target)
    print(f"Searching for {target}: result {result} (not found)")


    print("\n=== EDGE CASES ===")


    ## Edge case #1: delete with an invalid index. Validation catches
    ## it and returns None instead of crashing with an IndexError
    result = delete_at(nums, 10)
    print("Delete at invalid index 10:", result, "-->", nums, "(unchanged)")

    ## Edge case 2: delete from an empty list. No index is valid when
    ## the length is 0, so the function safely returns None.
    empty = []
    result = delete_at(empty, 0)
    print("Delete from empty list:", result)


if __name__ == "__main__":
    main()