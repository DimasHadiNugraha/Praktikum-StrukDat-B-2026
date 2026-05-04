class StackList:
    def __init__(self):
        self.items = [] 

    def is_empty(self):
        return len(self.items) == 0

    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return 'kosong'
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return 'kosong'
        return self.items[-1]

    def size(self):
        return len(self.items)

d = StackList()
d.push('www.google.com')
d.push('www.github.com')
d.push('www.stackoverflow.com')

print("Stack: ", d.items)
print("Pop: ", d.pop())
print("Stack after Pop: ", d.items)
print("Peek: ", d.peek())
print("isEmpty: ", d.is_empty())
print("Size: ", d.size())
