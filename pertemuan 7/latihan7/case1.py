'''tugas 1'''
Data_Awal = ["google.com", "python.org"]
print(f"Data awal: {Data_Awal}")
print(" ")
history_array = []  

for item in Data_Awal:
    history_array.append(item)

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)

tambah_pencarian_array("w3schools.com")
tambah_pencarian_array("youtube.com")

print("riwayat pencarian(array):")
for item in history_array:
    print(f"-> {item}")
print(" ")

'''tugas 2'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList:
    def __init__(self):
        self.head = None

    def tambah_pencarian_linked(self, keyword):
        new_node = Node(keyword)
        new_node.next = self.head
        self.head = new_node

    def tampilkan_history(self):
        current_node = self.head
        print("Riwayat pencarian:")
        while current_node:
            print(f"-> {current_node.data}")
            current_node = current_node.next

Data_Awal = ["google.com", "python.org"]

history_linked_list = HistoryLinkedList()

for item in Data_Awal:
    history_linked_list.tambah_pencarian_linked(item)       

history_linked_list.tambah_pencarian_linked("w3schools.com")
history_linked_list.tambah_pencarian_linked("youtube.com")


history_linked_list.tampilkan_history()


