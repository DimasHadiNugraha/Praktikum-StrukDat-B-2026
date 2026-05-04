
#operasi dasar queue
from xml.dom import Node


class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.isEmpty():
            return "queue is empty"
        removed_item = self.items.pop(0)
        print(f"Dequeued: {removed_item}")
        return removed_item
    
    def peek(self):
        if not self.isEmpty():
            return "queue is empty"
        return self.items[0]

    def size(self):
        return len(self.items)
    
q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(f"Next item: {q.peek()}")




    
# implementasi menggunakan linked list

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class queuelinkedlist:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0
    def is_Empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node (item)
        if self.rear is Node:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.count += 1
        print(f'enqueued:{item}')
    
    def dequeue(self):
        if self.is_Empty():
            return "Quenue kosong"
        
        temp_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        
        self.count -= 1
        return temp_data
    
    def peek(self):
        if self.is_Empty():
            return "Queue kosong"
        return self.front.data
    
    def size(self):
        return self.count
              
        
