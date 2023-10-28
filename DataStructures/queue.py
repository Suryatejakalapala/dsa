# queue its based on first in first out (FIFO)

class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self , item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError('Queue is empty')
        return self._items.pop(0)
    
    def isempty(self):
        return not self._items
    
q = Queue()

q.enqueue(5)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.isempty())
