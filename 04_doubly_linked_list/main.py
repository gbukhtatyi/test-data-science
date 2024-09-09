class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def pop(self):
        if self.last == None: return
        if self.last.prev == None: return

        self.last = self.last.prev
        self.last.next = None

    def push(self, node):
        if self.last == None:
            self.first = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node

    def unshift(self, node):
        if self.first == None:
            self.first = node
            self.last = node
        else:
            self.first.prev = node
            node.next = self.first
            self.first = node

    def shift(self):
        if self.first == None: return
        if self.first.next == None: return

        self.first = self.first.next
        self.first.prev = None

    def print(self):
        node = self.first
        while node:
            print(node)
            node = node.next
        print('')

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

node_list = LinkedList()

node_list.push(node_1)
node_list.print()

node_list.push(node_2)
node_list.print()

node_list.unshift(node_3)
node_list.print()

node_list.pop()
node_list.print()

node_list.shift()
node_list.print()