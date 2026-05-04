class Node:
    def __init__(self, nama,keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class Queue:
    def __init__ (self):
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, nama, keluhan):
        new_node = Node(nama, keluhan)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"[daftar] {nama} terdaftar dengan keluhan: {keluhan} no antrian: {self._size}")

    def dequeue(self):
        if self.is_empty():
            print('[panggilan] Antrian kosong')
            return None
        removed = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f'[panggilan] {removed.nama} dengan keluhan: {removed.keluhan} dipanggil')

    def peek(self):
        if self.is_empty():
            print('[peek] Antrian kosong')
        else:
            print(f'[peek] Antrian berikutnya: {self.head.nama} dengan keluhan: {self.head.keluhan}')

    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self._size    
    
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print('[clear] Antrian telah dikosongkan')

    def utama(self):
        if self.is_empty():
            print('[antrian kosong]:')
            return
        print('[daftar antrian]:')
        current = self.head
        i = 1
        while current:
            print(f'{i}. {current.nama} -> {current.keluhan}')
            current = current.next
            i += 1

q = Queue()
print('===========================================================================')
print('SISTEM ANTRIAN POLI UMUM')
print('RS sehat bersama')
print('===========================================================================')

print(f'[cek nama]apakah antrian kosong?->{'ya'if q.is_empty() else 'tidak'}')
q.enqueue('budi', 'Demam tinggi')
q.enqueue('ani', 'batuk pilek')
q.enqueue('citra', 'sakit kepala')
print(' ')
print(f'[info]jumlah pasien menunggu: {q.size()} orang')
q.peek()
print(' ')
q.dequeue()
q.enqueue('dodi', 'nyeri perut')
print(' ')
q.utama()
print(' ')
q.dequeue()
print(f'[info]jumlah pasien menunggu: {q.size()} orang')
q.clear()

print(f'[cek]apakah antrian kosong?-> {'ya'if q.is_empty() else 'tidak'} antrian sudah kosong')
print('===========================================================================')
print('Simulasi selesai!')
print('===========================================================================')
