class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, id_buku, judul):
        new_node = Node(id_buku, judul)
        if self.root is None:
            self.root = new_node
            print(f'[insert]berhasil memasukan :id {id_buku} - {judul}')
            return
        
        current = self.root
        while True:
            if id_buku < current.id_buku:
                if current.left is None:
                    current.left = new_node
                    break   
                
                current = current.left

            elif id_buku > current.id_buku:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
            
            else:
                print(f'id buku {id_buku} sudah terdaftar')
                return
            
        print(f'[insert]berhasil memasukan :id {id_buku} - {judul}')
    
    def search(self, id_buku): 
        current = self.root 
        while current is not None: 
            if id_buku == current.id_buku: 
                return current 
            elif id_buku < current.id_buku: 
                current = current.left 
            else: 
                current = current.right
        return None
    
    def traversal_inorder(self, current,posisi=[1]):
        if current is None:
            return
        
        if current.left is not None:
            self.traversal_inorder(current.left, posisi)
        
        print(f"{posisi[0]}. {current.id_buku} - {current.judul}")
        posisi[0] += 1 
            
        if current.right is not None:  
            self.traversal_inorder(current.right, posisi)
    
    def get_min(self,):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.id_buku
    
    def get_max(self,):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.id_buku
    
    def height(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1
        
Binary_Search_Tree = BinarySearchTree()
print(' ')
print('SISTEM KATALOG PERPUSTAKAAN "ILMU TERANG"')
print('===========================================')
buku =[(50, "Dasar Pemrograman"),
       (30, "Struktur Data"),
       (70, "Kecerdasan Buatan"),
       (20, "Matematika Diskrit"),
       (40, "Basis Data"),
       (60, "Jaringan Komputer"),
       (80, "Sistem Operasi")
]

for id_buku, nama in buku:
    Binary_Search_Tree.insert(id_buku, nama)
print(' ')
print('[INFO] Koleksi Buku (In-Order Traversal):')
Binary_Search_Tree.traversal_inorder(Binary_Search_Tree.root)
print()


print('[SEARCH] Mancari ID 60...', end=" ")
cari1 = Binary_Search_Tree.search(60)
if cari1:
    print(f'Ditemukan! Judul: {cari1.judul}.')
else:
    print('Data tidak ditemukan.')

print('[SEARCH] Mencari ID 100...', end=" ")
cari2 = Binary_Search_Tree.search(100)
if cari2:
    print(f'Ditemukan! Judul: {cari2.judul}.')
else:
    print('Data tidak ditemukan.')
print()


print('[STATISTIK] ID Terkecil:', Binary_Search_Tree.get_min())
print('[STATISTIK] ID Terbesar:', Binary_Search_Tree.get_max())
print('[INFO] Tinggi (Height) Tree:', Binary_Search_Tree.height(Binary_Search_Tree.root))
print('===========================================')
print('simulasi selesai !')
print()

  