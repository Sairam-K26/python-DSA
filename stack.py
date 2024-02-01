# A stack is a data structure that stores items in an Last-In/First-Out manner. This is frequently referred to as LIFO. This is in contrast to a queue, which stores items in a First-In/First-Out (FIFO) manner.
# It works almost exactly like a regular queue, except that elements must now join and leave it through only one end called the top of the stack. 
# Stacks are widely used in computing for various purposes. Perhaps the most familiar context for a programmer is the call stack containing the functions in the order they were called. Python will reveal this stack to you through a traceback in case of an unhandled exception. It’s usually a bounded stack with a limited capacity, which you’ll find out about during a stack overflow error caused by too many recursive calls.

# Implementation:
# Stack in Python can be implemented using the following ways: 

# list method
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
stack.pop()
print(stack)

#collections.deque()
from collections import deque
stack=deque()
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
stack.pop()
print(stack)

#using singly linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            popped=self.head.data
            self.head=self.head.next
            return popped

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

    def print_stack(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end="->")
                temp=temp.next
            print("None")

s1 = Stack()
s1.push(5)  
s1.push(10)
s1.push(15)
s1.push(20)
s1.print_stack()
print("Top element is ",s1.peek())
print("Popped element is ",s1.pop())
s1.print_stack()
print("Is stack empty? ",s1.is_empty())
print("Popped element is ",s1.pop())
print("Popped element is ",s1.pop())
print("Popped element is ",s1.pop())
print("Is stack empty? ",s1.is_empty())
print("Popped element is ",s1.pop())
s1.print_stack()
print("Is stack empty? ",s1.is_empty())

