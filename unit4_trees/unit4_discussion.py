"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================
 
INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).
 
You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Each node holds one value (here, an employee ID) and two links.
        # A new node always starts as a leaf, so both children are None.
        self.value = value
        self.left = None   # subtree of values SMALLER than self.value
        self.right = None  # subtree of values LARGER than self.value


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # An empty tree is represented by a root of None. Every method
        # starts from the root, so None tells them there is nothing to visit.
        self.root = None
        # Track how many nodes were checked during the most recent search.
        # This makes the "reduced search space" visible in the output.
        self.last_comparisons = 0

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.
 
        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion has to respect the BST rule: everything in a node's
        # left subtree is smaller than the node, and everything in its right
        # subtree is larger. If a new value were placed anywhere else, search
        # would go the wrong direction and never find it. That is why every
        # step of insertion compares the value with the current node and
        # moves left (smaller) or right (larger) until it finds an empty spot.
        #
        # The helper returns the (possibly new) root, so assigning it back
        # covers the case where the tree was empty before this insert.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.
 
        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: an empty position was reached, so the new value goes here.
        if node is None:
            return Node(value)

        if value < node.value:
            # Smaller values belong in the left subtree.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values belong in the right subtree.
            node.right = self._insert_recursive(node.right, value)
        # else: value == node.value
        # Duplicates are ignored. Employee IDs are unique, so storing the
        # same ID twice would create a duplicate record. Ignoring it keeps
        # the tree's ordering rule strict (left < node < right).

        # Return the unchanged node reference so the parent keeps its link.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.
 
        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A linear search through a list has to check items one by one, so
        # in the worst case it looks at all n items (O(n)).
        # A BST search only follows ONE path from the root downward. Each
        # comparison tells us whether the target is to the left or right,
        # so the entire other subtree is skipped. In a balanced tree this
        # cuts the remaining search space roughly in half at every step,
        # giving O(log n). For 1,000,000 records that is about 20 checks
        # instead of up to 1,000,000.
        self.last_comparisons = 0
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case 1: fell off the tree, so the value is not stored.
        if node is None:
            return False

        self.last_comparisons += 1

        # Base case 2: found the value.
        if value == node.value:
            return True

        # Recursive cases: only go down the side that could contain it.
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Start with an empty list and let the helper fill it.
        # An empty tree simply returns [] because the helper stops at None.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.
 
        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Why this is sorted: for any node, every value in its left subtree
        # is smaller and every value in its right subtree is larger.
        # Visiting left -> node -> right therefore outputs all the smaller
        # values first, then the node, then all the larger values. Because
        # the same rule applies recursively at every level, the full result
        # comes out in ascending order without any extra sorting step.
        if node is None:
            return
        self._inorder_recursive(node.left, values)   # 1. left subtree
        values.append(node.value)                    # 2. current node
        self._inorder_recursive(node.right, values)  # 3. right subtree

    # ----------------------------------------------------------
    # Additional helpers (added to support the real-world example)
    # ----------------------------------------------------------
    def height(self):
        """Return the number of levels in the tree (empty tree = 0)."""
        # Height is the length of the longest root-to-leaf path. It is the
        # worst-case number of comparisons a search can take, so it is the
        # best single number for judging how efficient the tree is.
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left),
                       self._height_recursive(node.right))

    def size(self):
        """Return the number of nodes stored in the tree."""
        return len(self.inorder())


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")
    print("Real-world example: organizing employee records by employee ID")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    employees = BST()

    # The IDs are inserted in a "balanced" order: the middle value first,
    # then the middles of each half. This produces a full tree of height 3.
    #
    #                 1050
    #               /      \
    #           1025        1075
    #          /    \      /    \
    #       1010   1040  1060   1090
    #
    # Step-by-step explanation of how each insert narrows the search space:
    # - 1050: becomes the root. Every later ID is split into "below 1050"
    #         (left) or "above 1050" (right), so one comparison removes
    #         half of the tree from consideration.
    # - 1025: 1025 < 1050, so it goes left. It now splits the lower half
    #         into 1000-1024 and 1026-1049.
    # - 1075: 1075 > 1050, so it goes right and splits the upper half.
    # - 1010: < 1050 (left), < 1025 (left). Two comparisons placed it;
    #         the right side of the tree was never touched.
    # - 1040: < 1050 (left), > 1025 (right).
    # - 1060: > 1050 (right), < 1075 (left).
    # - 1090: > 1050 (right), > 1075 (right).
    # Every insert followed a single path of at most 3 nodes, out of 7.
    balanced_order = [1050, 1025, 1075, 1010, 1040, 1060, 1090]
    for emp_id in balanced_order:
        employees.insert(emp_id)

    print(f"Inserted employee IDs (in this order): {balanced_order}")
    print(f"Root ID: {employees.root.value}")
    print(f"Left subtree root: {employees.root.left.value}  "
          f"(IDs smaller than {employees.root.value})")
    print(f"Right subtree root: {employees.root.right.value}  "
          f"(IDs larger than {employees.root.value})")
    print(f"Nodes: {employees.size()}, Height: {employees.height()}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # In-order visits left subtree, then the node, then the right subtree.
    # Since every left subtree only holds smaller IDs and every right
    # subtree only holds larger IDs, the IDs come out from lowest to
    # highest, even though they were inserted out of order.
    # This is useful for something like printing an employee roster
    # sorted by ID without running a separate sort.
    sorted_ids = employees.inorder()
    print(f"In-order result: {sorted_ids}")
    print(f"Matches sorted(): {sorted_ids == sorted(balanced_order)}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Existing IDs:
    # - 1050 is the root, so it is found on the first comparison.
    # - 1060 is found in 3 comparisons: 1050 -> go right -> 1075 -> go left
    #   -> 1060. The entire left half (1010, 1025, 1040) is never checked.
    # Missing IDs:
    # - 1030: 1050 -> left -> 1025 -> right -> 1040 -> left -> None.
    #   Reaching an empty spot proves it is not in the tree after only
    #   3 checks; a linear search would need to check all 7 records.
    # - 2000: larger than every ID, so the search keeps going right
    #   (1050 -> 1075 -> 1090) and ends at None.
    for emp_id in [1050, 1060, 1030, 2000]:
        found = employees.search(emp_id)
        status = "FOUND" if found else "NOT FOUND"
        print(f"Search {emp_id}: {status:<9} "
              f"({employees.last_comparisons} of {employees.size()} "
              f"nodes checked)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Edge case 1: empty tree.
    # The root is None, so the traversal helper stops immediately and
    # returns [], and search hits the "node is None" base case and returns
    # False. No special if-statements are needed in main() because the
    # base cases already handle it.
    empty = BST()
    print(f"Empty tree traversal: {empty.inorder()}")
    print(f"Empty tree search for 1050: {empty.search(1050)}")
    print(f"Empty tree height: {empty.height()}")

    # Edge case 2: single-node tree.
    # The only node is both the root and a leaf. Search succeeds in one
    # comparison or fails after one comparison.
    single = BST()
    single.insert(1001)
    print(f"Single-node traversal: {single.inorder()}, "
          f"height: {single.height()}")

    # Edge case 3: duplicate IDs.
    # Inserting 1025 again reaches the node that already holds 1025.
    # The value is neither smaller nor larger, so it is ignored and the
    # node count stays at 7. This prevents duplicate employee records.
    before = employees.size()
    employees.insert(1025)
    print(f"Duplicate insert of 1025: size before={before}, "
          f"size after={employees.size()}")

    # Edge case 4: sequential insertion order (the inefficient case).
    # Inserting IDs in ascending order means every new ID is larger than
    # all existing IDs, so it always goes to the right. The tree turns
    # into a chain (basically a linked list) with height equal to the
    # number of nodes, and searching becomes O(n) again.
    #
    #   1001 -> 1002 -> 1003 -> ... -> 1007   (all right children)
    sequential = BST()
    sequential_order = list(range(1001, 1008))
    for emp_id in sequential_order:
        sequential.insert(emp_id)
    sequential.search(1007)
    print(f"\nSequential insert {sequential_order}")
    print(f"Sequential tree height: {sequential.height()} "
          f"(balanced tree with 7 nodes: {employees.height()})")
    print(f"Search 1007 in sequential tree: "
          f"{sequential.last_comparisons} comparisons")

    # Scaling the same comparison to 1,000 employees shows how big the
    # difference gets. A balanced order is built by always inserting the
    # middle ID of each range first.
    def balanced_insert(tree, ids):
        if not ids:
            return
        mid = len(ids) // 2
        tree.insert(ids[mid])
        balanced_insert(tree, ids[:mid])
        balanced_insert(tree, ids[mid + 1:])

    big_ids = list(range(1, 1001))
    big_sequential = BST()
    for emp_id in big_ids:
        big_sequential.insert(emp_id)
    big_balanced = BST()
    balanced_insert(big_balanced, big_ids)

    big_sequential.search(1000)
    seq_checks = big_sequential.last_comparisons
    big_balanced.search(1000)
    bal_checks = big_balanced.last_comparisons
    print(f"\n1,000 employees, searching for ID 1000:")
    print(f"  Sequential order -> height {big_sequential.height()}, "
          f"{seq_checks} comparisons")
    print(f"  Balanced order   -> height {big_balanced.height()}, "
          f"{bal_checks} comparisons")


if __name__ == "__main__":
    import sys
    # The 1,000-node sequential tree is 1,000 levels deep, which goes past
    # Python's default recursion limit, so raise it for this demo.
    # (This itself shows a real cost of an unbalanced tree.)
    sys.setrecursionlimit(5000)
    main()
