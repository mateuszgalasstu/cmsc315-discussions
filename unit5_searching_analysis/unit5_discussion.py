"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

# Application context:
# I based this program on a common textbook example: looking up a student
# ID number in a university's student records. A small class roster is easy
# to check one ID at a time, but a records system with a very large number
# of students is only practical to search quickly if the IDs are kept in
# sorted order. Both search algorithms below work on lists of student IDs
# so the comparison stays tied to that scenario.

import time


def linear_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # The optional stats dictionary lets me count comparisons so the output
    # shows how much work each search does, not only whether it succeeded.
    comparisons = 0

    # I walk through the list one element at a time, starting at index 0.
    # Linear search makes no assumptions about order, so it works on sorted
    # and unsorted data alike.
    for index in range(len(lst)):
        comparisons += 1
        if lst[index] == target:
            if stats is not None:
                stats["comparisons"] = comparisons
            return index

    # If the loop finishes without returning, the target is not in the list.
    # This is the worst case: every one of the n elements was checked once,
    # which is why linear search runs in O(n) time. The work grows in direct
    # proportion to the list size, so doubling the list roughly doubles the
    # number of comparisons in the worst and average cases.
    if stats is not None:
        stats["comparisons"] = comparisons
    return -1


def binary_search(lst, target, stats=None):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    comparisons = 0

    # low and high mark the boundaries of the part of the list that could
    # still contain the target. At the start, that is the entire list.
    low = 0
    high = len(lst) - 1

    # The loop runs as long as the search space has at least one element.
    # For an empty list, high starts at -1, so the loop never runs and the
    # function correctly returns -1.
    while low <= high:
        # I check the middle element of the remaining range. Using
        # low + (high - low) // 2 gives the same result as (low + high) // 2
        # and is the standard form that avoids overflow in languages with
        # fixed-size integers.
        mid = low + (high - low) // 2
        comparisons += 1

        if lst[mid] == target:
            if stats is not None:
                stats["comparisons"] = comparisons
            return mid
        elif lst[mid] < target:
            # The middle value is too small. Because the list is sorted,
            # everything at or before mid is also too small, so I discard
            # the left half by moving low past mid.
            low = mid + 1
        else:
            # The middle value is too large, so everything at or after mid
            # is also too large. I discard the right half by moving high
            # below mid.
            high = mid - 1

        # Each iteration cuts the remaining search space roughly in half.
        # A list of n elements needs at most about log2(n) + 1 iterations
        # before the range is empty, which gives binary search O(log n) time.

    # low passed high, meaning the search space is empty and the target
    # is not in the list.
    if stats is not None:
        stats["comparisons"] = comparisons
    return -1


def run_search(label, search_function, lst, target):
    """
    Helper I added to run one search, time it, and print the result in a
    consistent format. Keeping this in one place avoids repeating the same
    print and timing code for every test below.
    """
    stats = {"comparisons": 0}
    start = time.perf_counter()
    result = search_function(lst, target, stats)
    elapsed_ms = (time.perf_counter() - start) * 1000

    outcome = f"found at index {result}" if result != -1 else "not found (-1)"
    print(f"  {label:<14} target {target:>9}: {outcome:<24} "
          f"| comparisons: {stats['comparisons']:>9,} | time: {elapsed_ms:.4f} ms")
    return result


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # A short, sorted class roster of ten student IDs.
    small_roster = [1012, 1047, 1123, 1189, 1250, 1304, 1377, 1421, 1498, 1563]
    print(f"Class roster ({len(small_roster)} student IDs): {small_roster}")

    # Value that exists: student ID 1421 is at index 7.
    print("\nSearching for a student ID that is on the roster:")
    run_search("Linear search", linear_search, small_roster, 1421)
    run_search("Binary search", binary_search, small_roster, 1421)
    # Both searches returned index 7. Linear search needed 8 comparisons
    # because it checked indexes 0 through 7 in order. Binary search needed
    # only 2 because it started in the middle (index 4), discarded the left
    # half, and landed on index 7 with its next check.

    # Value that does not exist: student ID 1300 falls between 1250 and 1304.
    print("\nSearching for a student ID that is NOT on the roster:")
    run_search("Linear search", linear_search, small_roster, 1300)
    run_search("Binary search", binary_search, small_roster, 1300)
    # Both returned -1. Linear search had to check all 10 entries before it
    # could conclude the student ID was missing. Binary search narrowed the range
    # down to an empty space in 3 comparisons. With only ten items, the time
    # difference is too small to notice, which is why linear search is fine
    # for short lists.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # A large, sorted set of 1,000,000 student IDs. I used every third
    # number starting at 100,000 so the list is sorted and there are known
    # gaps to test missing values.
    large_roster = list(range(100_000, 100_000 + 3 * 1_000_000, 3))
    print(f"University student records: {len(large_roster):,} student IDs "
          f"(from {large_roster[0]:,} to {large_roster[-1]:,})")

    # Value near the end of the list, close to linear search's worst case.
    near_end_id = large_roster[-10]
    print("\nSearching for a student ID near the end of the records:")
    run_search("Linear search", linear_search, large_roster, near_end_id)
    run_search("Binary search", binary_search, large_roster, near_end_id)

    # Value that is missing (not a multiple-of-3 offset, so it falls in a gap).
    missing_id = 2_500_001
    print("\nSearching for a student ID that is NOT in the records:")
    run_search("Linear search", linear_search, large_roster, missing_id)
    run_search("Binary search", binary_search, large_roster, missing_id)

    # Comparison of results:
    # Linear search needed close to 1,000,000 comparisons for both targets,
    # while binary search needed about 20. Going from 10 items to 1,000,000
    # items multiplied linear search's work by about 100,000, but binary
    # search only went from 3-4 comparisons to about 20. That is because
    # log2(1,000,000) is roughly 20: every comparison halves the remaining
    # range, so each time the list doubles in size, binary search only needs
    # one more comparison. The larger the dataset, the wider this gap becomes.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list.
    # Linear search's loop runs zero times, and binary search starts with
    # high = -1, so its while condition is false immediately. Both return -1
    # without raising an IndexError.
    print("\nEdge case 1: Empty roster")
    empty_roster = []
    run_search("Linear search", linear_search, empty_roster, 1012)
    run_search("Binary search", binary_search, empty_roster, 1012)

    # Edge case 2: Single-element list.
    # low and high both start at 0, so binary search checks that one element
    # and either returns 0 or moves a boundary past the other and stops.
    print("\nEdge case 2: Single-student roster")
    single_roster = [1250]
    run_search("Linear search", linear_search, single_roster, 1250)
    run_search("Binary search", binary_search, single_roster, 1250)
    run_search("Linear search", linear_search, single_roster, 9999)
    run_search("Binary search", binary_search, single_roster, 9999)

    # Edge case 3: Value at the first position.
    # This is linear search's best case (1 comparison). Binary search still
    # starts in the middle and has to work its way left, so here it actually
    # takes more comparisons than linear search.
    print("\nEdge case 3: Student ID at the first position")
    run_search("Linear search", linear_search, small_roster, small_roster[0])
    run_search("Binary search", binary_search, small_roster, small_roster[0])

    # Edge case 4: Value at the last position.
    # This is linear search's worst case for a value that exists, since it
    # checks every element. Binary search moves right on each step and
    # reaches the last index in about log2(n) comparisons.
    print("\nEdge case 4: Student ID at the last position")
    run_search("Linear search", linear_search, small_roster, small_roster[-1])
    run_search("Binary search", binary_search, small_roster, small_roster[-1])

    # Edge case 5: Unsorted list.
    # Binary search assumes sorted input. On an unsorted list it can throw
    # away the half that actually contains the target and return -1 even
    # though the value is present. Linear search is unaffected because it
    # never relies on order. This is the main reason the roster has to be
    # kept sorted if binary search is going to be used on it. In this test,
    # student ID 1563 is at index 2, but binary search checks the middle value
    # (1047), sees that it is smaller than 1563, and searches only the right
    # half, so it never reaches index 2.
    print("\nEdge case 5: Unsorted roster (binary search precondition broken)")
    unsorted_roster = [1377, 1012, 1563, 1250, 1047, 1498, 1123, 1421, 1189, 1304]
    print(f"Unsorted roster: {unsorted_roster}")
    run_search("Linear search", linear_search, unsorted_roster, 1563)
    run_search("Binary search", binary_search, unsorted_roster, 1563)
    print("  Binary search missed a student ID that is in the list because the "
          "data was not sorted.")


if __name__ == "__main__":
    main()
