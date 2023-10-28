# STACK is a data structure which works in the principle of FILO(first in last out principle)

class Stack:

    def __init__(self):
        self._items = [] # we took protected because It helps to prevent outside code from accidentally or maliciously modifying the stack's data.


    def push(self , item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError('Stack is empty')
        return self._items.pop()
    
    def peek(self):
        if not self._items:
            raise IndexError('Stack is empty')
        return self._items[-1]
    
    def isempty(self):
        return not self._items
    
s = Stack()

s.push(5)
s.push(10)
s.push(2)
print(s.peek())
print(s.pop())
print(s.isempty())