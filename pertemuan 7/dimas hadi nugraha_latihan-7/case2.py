'''Case: Sistem Antrean Pasien (Emergency Room)
Skenario: Di sebuah rumah sakit, pasien datang dengan tingkat urgensi yang berbeda. Secara
default, pasien baru akan mengantre di belakang. Namun, jika ada pasien "Darurat", mereka harus
disisipkan di posisi tertentu (misalnya posisi ke-2) agar segera ditangani setelah pasien pertama
yang sedang diperiksa.
Data Awal (Antrean saat ini): ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

Tugas 1: Implementasi pada List Array
Gunakan list bawaan Python antrean_array.
1. Buat list antrean_array dengan data awal di atas.
2. Buat fungsi sisipkan_pasien_darurat_array(nama_pasien, posisi):
o Gunakan metode .insert(posisi - 1, nama_pasien).
o Analisis: Apa yang terjadi pada pasien di belakangnya saat pasien baru masuk di
tengah?
3. Cetak antrean akhir.
Tugas 2: Implementasi pada Singly LinkedList
Gunakan class Node dan AntreanLinkedList.
1. Implementasikan fungsi insert_at_position(head, nama_pasien, posisi) seperti kode yang
kamu punya sebelumnya (menggunakan logika position - 2).
2. Tugas Tambahan: Tambahkan validasi sederhana. Jika posisi yang dimasukkan lebih besar
dari jumlah pasien yang ada, maka pasien tersebut otomatis diletakkan di paling akhir
(Append).'''

'''tugas 1'''
antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)

sisipkan_pasien_darurat_array('Pasien D (Darurat)', 2)
print('Antrian akhir (Array):')
for i, pasien in enumerate(antrean_array, start=1):
    print(f"{i}. {pasien}") 
print(' ')
'''tugas 2'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntreanLinkedList:
    def __init__(self):
        self.head = None

    def append(self, nama_pasien):
        new_node = Node(nama_pasien)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_at_position(self, nama_pasien, posisi):
        new_node = Node(nama_pasien)
        if posisi == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        count = 1
        while current_node and count < posisi - 1:
            current_node = current_node.next
            count += 1  
        if current_node is None:
            self.append(nama_pasien)
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def tampilkan(self):
        current_node = self.head
        index = 1
        while current_node:
            print(f"{index}. {current_node.data}")
            current_node = current_node.next
            index += 1

antrean_linked = AntreanLinkedList()

# Data awal
antrean_linked.append("Pasien A (Stabil)")
antrean_linked.append("Pasien B (Stabil)")
antrean_linked.append("Pasien C (Stabil)")

# Menyisipkan pasien darurat di posisi 2
antrean_linked.insert_at_position("Pasien D (Darurat)", 2)

print("Antrean Pasien (Linked List):")
antrean_linked.tampilkan()
