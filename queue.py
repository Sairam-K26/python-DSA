# Like a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first. A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.
# oper-enqueue,dequeue,front,rear

# implementation

# list method

queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
queue.pop(0)
queue.pop(0)
print(queue)


# collections.deque()

from collections import deque
queue=deque()
queue.append(1)
queue.append(2)
queue.append(3) 
print(queue)
queue.popleft()
queue.popleft()
print(queue)

# using queue.Queue
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())



