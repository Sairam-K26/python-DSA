#using deque
from collections import deque
deque()
deque(['a','b','c'])
deque('abc')
deque([{'data': 'a'}, {'data': 'b'}])
#insert delete
llist = deque("abcde")
llist.append("f")
print(llist)
llist.pop()
print(llist)
# in left
llist.appendleft("z")
print(llist)
llist.popleft()
print(llist)



#own linkedlist

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

#traversing
def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next

#insert in beggining
def add_first(self, node):
    node.next = self.head
    self.head = node

#insert in end
def add_last(self, node):
    if self.head is None:
        self.head = node
        return
    for current_node in self:
        pass
    current_node.next = node

#insert in between
def add_after(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")

    for node in self:
        if node.data == target_node_data:
            new_node.next = node.next
            node.next = new_node
            return

    raise Exception("Node with data '%s' not found" % target_node_data)

#remove
def remove_node(self, target_node_data):
    if self.head is None:
        raise Exception("List is empty")

    if self.head.data == target_node_data:
        self.head = self.head.next
        return

    previous_node = self.head
    for node in self:
        if node.data == target_node_data:
            previous_node.next = node.next
            return
        previous_node = node

    raise Exception("Node with data '%s' not found" % target_node_data)

