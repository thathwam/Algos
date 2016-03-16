"""
Reverse a Linked list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        next = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

llist.print_list()
llist.reverse()
print("\nReversed Linked List")
llist.print_list()

