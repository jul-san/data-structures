import random
import sys

sys.setrecursionlimit(2000)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def search(self, data):
        if self.data == data:
            return True
        if self.next:
            return self.next.search(data)

class LL:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, data):
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        if self.head.data > data:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            if current.next.data > data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        current.next = new_node

        '''
        Another way to write this

        while current.next and current.next.data < data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        
    def print(self):
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next
        print('->'.join(output))

elements = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(elements)

ll = LL()

for e in elements:
    ll.append(e)

ll.print()
print(ll.search(10))

ll.delete(4)
ll.print()
