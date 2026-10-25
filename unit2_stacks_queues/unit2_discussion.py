"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Supports LIFO behavior by pushing value to the top of the stack
        self.stack.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # If the stack is empty, an index error will be raised
        if self.is_empty():
            raise IndexError("Pop from empty stack!")

        return self.stack.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek returns the top value without removing it the way pop does
        if self.is_empty():
            raise IndexError("Peek from empty stack!")
        return self.stack[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Supports FIFO behavior by adding value to queue, first come first served
        self.queue.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Added an empty queue error message
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue!")
        return self.queue.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the value at the beginning of the queue
        if self.is_empty():
            raise IndexError("Front of an empty queue!")
        return self.queue[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    # Requirements:
    # 1. Create a Stack object.
    stack = Stack()
    print("Created an empty stack..")
    # 2. Add at least 4 values to the stack.
    stack.push(4)
    print("Pushed 4, stack is now", stack.stack)
    stack.push(3)
    print("Pushed 3, stack is now", stack.stack)
    stack.push(2)
    print("Pushed 2, stack is now", stack.stack)
    stack.push(1)
    print("Pushed 1, stack is now", stack.stack)
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    print("Top of the stack (Peek):", stack.peek())
    print("Popping all values. Last in first out means they come out in reverse order:")
    removed = stack.pop()
    print("Popped", removed, "stack is now", stack.stack)
    removed = stack.pop()
    print("Popped", removed, "stack is now", stack.stack)
    removed = stack.pop()
    print("Popped", removed, "stack is now", stack.stack)
    removed = stack.pop()
    print("Popped", removed, "stack is now", stack.stack)
    # 5. Show what happens when pop() is used on an empty stack.
    print("Trying to pop from empty stack:")
    try:
        stack.pop()
    except IndexError as e:
        print("Error caught:", e)
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    print("Trying to peek at empty stack:")
    try:
        stack.peek()
    except IndexError as e:
        print("Error caught:", e)
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    stack2 = Stack()
    stack2.push(1)
    print("Created stack with one item:", stack2.stack)
    removed = stack2.pop()
    print("Popped", removed)
    print("Is the stack empty now?", stack2.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    # Requirements:
    # 1. Create a Queue object.
    queue = Queue()
    print("Created an empty queue")
    # 2. Add at least 4 values to the queue.
    queue.enqueue(1)
    print("Added 1 to the queue, queue is now", list(queue.queue))
    queue.enqueue(2)
    print("Added 2 to the queue, queue is now", list(queue.queue))
    queue.enqueue(3)
    print("Added 3 to the queue, queue is now", list(queue.queue))
    queue.enqueue(4)
    print("Added 4 to the queue, queue is now", list(queue.queue))
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    print("The queue is now:", list(queue.queue))
    print("Dequeueing..")
    queue.dequeue()
    print("The queue is now:", list(queue.queue))
    print("Dequeueing..")
    queue.dequeue()
    print("The queue is now:", list(queue.queue))
    print("Dequeueing..")
    queue.dequeue()
    print("The queue is now:", list(queue.queue))
    print("Dequeueing..")
    queue.dequeue()
    print("The queue is now:", list(queue.queue))
    # 5. Show what happens when dequeue() is used on an empty queue.
    print("Trying to dequeue from empty queue")
    try:
        queue.dequeue()
    except IndexError as e:
        print("Error caught:", e)
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    print("Trying to use front() from empty queue")
    try:
        queue.front()
    except IndexError as e:
        print("Error caught:", e)
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    queue2 = Queue()
    queue2.enqueue(1)
    print("Created a queue with one item:", list(queue2.queue))
    print("Dequeueing..")
    queue2.dequeue()
    print("Queue is now:", list(queue2.queue))
    print("Is the queue empty?", queue2.is_empty())


if __name__ == "__main__":
    main()