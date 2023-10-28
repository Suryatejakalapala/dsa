# linkedlist 
class Node:

    def __init__(self , data , next = None):
        self.data = data
        self.next = next

    def isempty(self):
        return self.head is None
    
    def append(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node is not None:
                current_node = current_node.Next
            current_node.next = new_node



class Linkedlist:

    def __init__(self):
        self.head = None