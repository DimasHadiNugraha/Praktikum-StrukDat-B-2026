# bagian 2
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 

    def is_empty(self):
        return self.count == 0
    

    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return 'kosong'
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.url
    
    def peek(self):
        if self.is_empty():
            return 'kosong'
        return self.top.url
    def size(self):
        return self.count

d = StackLinkedList()
d.push('www.google.com')
d.push('www.github.com')
d.push('www.stackoverflow.com')

print("LinkedList: ", end="")
print("Peek: ", d.peek())
print("Pop: ", d.pop())
print("LinkedList after Pop: ", end="")
print("isEmpty: ", d.is_empty())
print("Size: ", d.size())