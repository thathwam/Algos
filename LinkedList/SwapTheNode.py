"""
Swap nodes in a linked list without swapping data

Given a linked list and two keys in it, swap nodes for two given keys. Nodes should be swapped by changing links.
Swapping data of nodes may be expensive in many situations when data contains many fields.
It may be assumed that all keys in linked list are distinct.
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

    def swap_nodes(self, x, y):
        if self.head is None:
            print("Empty List")
            return

        if x == y:
            return

        prev_x = None
        cur_x = self.head
        while cur_x is not None and cur_x.data != x:
            prev_x = cur_x
            cur_x = cur_x.next

        prev_y = None
        cur_y = self.head
        while cur_y is not None and cur_y.data != y:
            prev_y = cur_y
            cur_y = cur_y.next

        if cur_x is None or cur_y is None:
            print('Either of x, y not found')
            return

        if prev_x != None:
            prev_x.next = cur_y
        else: #make y the new head
            self.head = cur_y

        # If y is not head of linked list
        if prev_y != None:
            prev_y.next = cur_x
        else: # make x the new head
            self.head = cur_x

        # Swap next pointers
        temp = cur_x.next
        cur_x.next = cur_y.next
        cur_y.next = temp
