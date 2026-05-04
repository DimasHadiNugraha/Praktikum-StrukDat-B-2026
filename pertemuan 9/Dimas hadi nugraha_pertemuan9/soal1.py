'''Bagian A — Double Linked List'''

class Node:
    def __init__(self,judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None

class daftar_buku:
    def __init__(self):
        self.head = None
        
    def insert_tail(self, judul, pengarang):
        new_node = Node(judul, pengarang)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def print_forward(self):    
        temp = self.head
        while temp:
            print(f'{temp.judul} - {temp.pengarang}')
            temp = temp.next

    def print_backward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next

        while temp:
            print(f'{temp.judul} - {temp.pengarang}')
            temp = temp.prev
    
    def delete_by_judul(self, judul):
        temp = self.head
        while temp:
            if temp.judul == judul:
                if temp.prev is None:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prew = temp.prev
                return
            temp = temp.next

dll = daftar_buku()
dll.insert_tail('Laskar Pelangi', 'Andrea Hirata')
dll.insert_tail('Bumi Manusia', 'Pramoedya Ananta Toer')
dll.insert_tail('Sang Pemimpi', 'Andrea Hirata')

print('forward:')
dll.print_forward()
print('---------------------------')
print('backward:')
dll.print_backward()
dll.delete_by_judul('Bumi Manusia')
print('---------------------------')
print('setelah dihapus:')
dll.print_forward() 