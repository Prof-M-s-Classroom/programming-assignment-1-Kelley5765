from distance import Distance

class Node:
    """
    Node class to be used in the linked list implementation of the stack.
    """
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None # Pointer to next node in linked list

class CircularStack:
    """
    Circular stack class using a linked list with a maximum size of 5 elements.
    """
    MAX_SIZE = 5 # Maximum number of elements the stack can hold

    def __init__(self):
        """Initialize the stack with an empty state."""
        self.top = None   # Most recent entry
        self.rear = None   # Oldest entry
        self.size = 0

    def push(self, distance):
        """Add a new Distance object to the stack, replacing the oldest entry if full."""
        new_node = Node(distance)
        if self.size == 0:
            # If stack is empty, both top and rear point to the new node
            self.top = new_node
            self.rear = new_node
            new_node.next = new_node # Circular reference (node points to itself)
        else:
            self.top.next = new_node # Current top node points to new node
            self.top = new_node      # Update top pointer to new node
            self.top.next = self.rear

        if self.size < self.MAX_SIZE:
            self.size += 1
        else:
            self.rear = self.rear.next   # Move rear to the next oldest entry
            self.top.next = self.rear    # Re-establish circular link from top to new rear


    def pop(self):
        """Remove the oldest entry from the stack."""
        if self.size == 0:
            print("Stack is empty")
            return None
        elif self.size == 1:
            removed = self.rear.data
            self.top = None
            self.rear = None
            self.size = 0
        else:
            removed = self.rear.data
            self.rear = self.rear.next   # Move rear forward
            self.top.next = self.rear    # Maintain circular link
            self.size -= 1
        return removed

    def peek(self):
        """Return the most recent distance entry without removing it."""
        if self.size == 0:
            print("Stack is empty")
            return None
        return self.top.data

    def print_stack(self):
        """Print all stored readings in order from oldest to newest."""
        if self.size == 0:
            print("Stack is empty")
            return

        temp = self.rear
        count = 0
        while count < self.size:  # Iterate only over the number of elements stored
            print(temp.data)
            temp = temp.next
            count += 1

    def is_empty(self):
        """Return True if the stack is empty, otherwise False."""
        return self.size == 0
