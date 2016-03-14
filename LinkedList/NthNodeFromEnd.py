"""
Find n’th node from the end of a Linked List
Given a Linked List and a number n, write a function that returns the value at the n’th
node from end of the Linked List.
"""
class LinkedList:
    def __init__(self):
        self.head = None

    class Node:

        def __init__(self, data):
            self.data = data
            self.Next = None

    def push(self, data):
        node = self.Node(data)
        node.Next = self.head
        self.head = node

    def print_list(self):
        if self.head is None:
            print("List is Empty")
        else:
            tmp = self.head
            while tmp is not None:
                print(tmp.data)
                tmp = tmp.Next

    def find_nth_node(self, n):
        main_ptr = self.head
        ref_ptr = self.head
        count = 0

        if self.head is not None:
            while count < n:
                if ref_ptr is None:
                    print(str(n) + " is greater than the length of List.")
                ++count
                ref_ptr = ref_ptr.Next

            while ref_ptr is not None:
                main_ptr = main_ptr.Next
                ref_ptr = ref_ptr.Next

            print("Node number " + str(n) + "From end is " + str(main_ptr.data))

lList = LinkedList()

lList.print_list()
lList.push(1)
lList.push(2)
lList.push(3)
lList.push(4)
lList.push(5)
lList.push(6)
lList.print_list()
lList.find_nth_node(2)