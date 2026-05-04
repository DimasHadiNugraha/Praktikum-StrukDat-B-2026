'''Bagian B — Circular Linked List
Sistem antrian kasir toko "Literasi"
Kasir toko menggunakan Circular Linked List untuk antrian pelanggan. Antrian
awal: Andi → Budi → Citra → Dina → (kembali ke Andi).
1. Buat class Node dengan atribut nama dan next. Buat fungsi insert_tail() dan
tambahkan 4 pelanggan.
2. Buat fungsi print_antrian() untuk menampilkan satu putaran antrian.
3. Tambahkan pelanggan baru Edo di akhir antrian menggunakan insert_tail(), lalu
tampilkan antrian.
4. Buat fungsi delete_head(), hapus Andi (sudah dilayani), lalu tampilkan antrian.'''

class Node:
    def __init__(self,nama):
        self.nama = nama
        self.next = None

class AntrianKasir:
    def __init__(self):
        self.head = None
        
    def insert_tail(self, nama):
        new_node = Node(nama)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
    
    def print_antrian(self):    
        if not self.head:
            print('Antrian kosong')
            return
        temp = self.head
        while True:
            print(temp.nama, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print(' (kembali ke ' + self.head.nama + ')')
    
    def delete_head(self):
        if not self.head:
            print('Antrian kosong')
            return
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

antrian = AntrianKasir()
antrian.insert_tail('Andi')
antrian.insert_tail('Budi')
antrian.insert_tail('Citra')
antrian.insert_tail('Dina')
print('Antrian awal:')
antrian.print_antrian()
print('---------------------------')
antrian.insert_tail('Edo')
print('Antrian setelah menambahkan Edo:')
antrian.print_antrian()
print('---------------------------')
antrian.delete_head()
print('Antrian setelah menghapus Andi:')
antrian.print_antrian()