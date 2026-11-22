"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""

# Application scenario:
# I used a small grocery store inventory for this program. Each key is an
# item name, and each value is how many of that item are in stock. This is a
# good fit for a hash table because the store needs to look up, update, and
# remove items by name quickly, no matter how many items are in the inventory.

# Size of the simple example table used to show bucket indexes.
TABLE_SIZE = 7


def simple_bucket(key):
    """
    Returns a bucket index for a key using a simple textbook hash function:
    add up the character codes of the string, then take the remainder
    after dividing by the table size.

    Python's real dict uses its own built-in hash() function, which is
    much better at spreading keys out. I used this simpler version only
    so the output shows the same bucket numbers on every run and makes
    collisions easy to see.
    """
    return sum(ord(character) for character in key) % TABLE_SIZE


def show_inventory(inventory):
    """Prints each item and its quantity on its own line."""
    if not inventory:
        print("  (inventory is empty)")
        return
    for item, quantity in inventory.items():
        print(f"  {item}: {quantity}")


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")

    # Create an empty dictionary to act as the hash table.
    inventory = {}

    # Add six key-value pairs (item name -> quantity in stock).
    # When a key is added, Python runs it through a hash function to get a
    # number, and uses that number to pick a slot (bucket) in an internal
    # array. The value is stored in that slot, so later Python can go
    # straight to it instead of searching through every item.
    inventory["apples"] = 50
    inventory["bread"] = 20
    inventory["milk"] = 35
    inventory["eggs"] = 60
    inventory["cheese"] = 15
    inventory["rice"] = 40

    print("Store inventory after adding 6 items:")
    show_inventory(inventory)

    # Show which bucket each key would go to in a simple 7-slot table.
    # When two different keys land in the same bucket, that is a collision.
    print(f"\nBucket index for each key in a simple table of size {TABLE_SIZE}:")
    buckets = {}
    for item in inventory:
        index = simple_bucket(item)
        buckets.setdefault(index, []).append(item)
        print(f"  {item:<7} -> bucket {index}")

    # Print any buckets that ended up holding more than one key.
    print("\nCollisions found:")
    for index, items in sorted(buckets.items()):
        if len(items) > 1:
            print(f"  bucket {index}: {', '.join(items)}")

    # Collisions do not cause errors. The hash table just needs a way to
    # store both keys. With chaining, the bucket holds a small list of
    # every key that landed there. Python's dict uses open addressing
    # instead, which means it probes for another open slot. Either way,
    # more collisions mean more checking, which slows lookups down.

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # To look up a key, Python hashes the key again, goes straight to the
    # matching slot, and confirms the key stored there is the same one.
    # This takes O(1) time on average, so it does not matter whether the
    # inventory has 6 items or 6 million.
    print(f"Lookup 'milk': {inventory['milk']} in stock")
    print(f"Lookup 'cheese': {inventory['cheese']} in stock")

    # The 'in' operator also uses hashing, so checking whether an item
    # exists is just as fast as looking it up.
    print(f"Is 'eggs' in the inventory? {'eggs' in inventory}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    show_inventory(inventory)

    # Assigning a new value to a key that already exists does not create a
    # second entry. Python hashes the key, finds the existing slot, and
    # replaces the old value with the new one. Keys in a dictionary are
    # always unique.
    inventory["bread"] = 12          # some bread was sold
    inventory["apples"] += 25        # a new apple shipment came in

    print("\nAfter update (bread sold down to 12, 25 apples restocked):")
    show_inventory(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    print("Before delete:")
    show_inventory(inventory)

    # Deleting a key hashes it to find its slot, then removes the key and
    # its value. The other items are not affected and do not need to be
    # moved, so deletion is also O(1) on average.
    del inventory["rice"]            # the store stopped carrying rice

    print("\nAfter deleting 'rice':")
    show_inventory(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Looking up a missing key.
    # Using inventory["bananas"] would raise a KeyError and crash the
    # program. The get() method returns a default value instead, so the
    # program can handle the missing item safely.
    print("Edge case 1: Lookup a missing key")
    try:
        print(inventory["bananas"])
    except KeyError:
        print("  inventory['bananas'] raised a KeyError")
    print(f"  inventory.get('bananas', 0) returned {inventory.get('bananas', 0)}")

    # Edge case 2: Deleting a missing key safely.
    # del inventory["rice"] would raise a KeyError because rice was
    # already removed. pop() with a default value removes the key if it
    # exists and returns the default if it does not, so nothing crashes.
    print("\nEdge case 2: Delete a missing key safely")
    removed = inventory.pop("rice", None)
    print(f"  inventory.pop('rice', None) returned {removed} (nothing was removed)")

    # Edge case 3: Updating a missing key.
    # Assigning to a key that does not exist does not cause an error. It
    # just adds the key as a new entry. This can hide mistakes like typos,
    # so the program checks whether the key exists before updating it.
    print("\nEdge case 3: Update a missing key")
    item_to_update = "coffee"
    if item_to_update in inventory:
        inventory[item_to_update] = 30
        print(f"  Updated '{item_to_update}'")
    else:
        print(f"  '{item_to_update}' is not in the inventory, so it was not updated")
    inventory["coffee"] = 30
    print("  Assigning inventory['coffee'] = 30 directly added it as a new item:")
    show_inventory(inventory)

    # Edge case 4: Using an empty dictionary.
    # Lookups, membership checks, and safe deletes all still work on an
    # empty dictionary. They just find nothing.
    print("\nEdge case 4: Empty dictionary")
    empty_inventory = {}
    print(f"  Number of items: {len(empty_inventory)}")
    print(f"  empty_inventory.get('milk') returned {empty_inventory.get('milk')}")
    print(f"  'milk' in empty_inventory: {'milk' in empty_inventory}")
    print(f"  empty_inventory.pop('milk', None) returned {empty_inventory.pop('milk', None)}")
    show_inventory(empty_inventory)



if __name__ == "__main__":
    main()