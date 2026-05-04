'''membuat class bisa menggunakan keyword class'''

class MyClass:
  x = 5

'''membuat objek'''

p1 = MyClass()
print(p1.x)

#catatan
'''bisa menghapus objek dengan keyword del '''

'''bisa membuat banyak objek atau Multiple Objects'''
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#catatan
'''class didifinisikan tidak boleh kosong
tetapi jika karena suatu alasan Anda memiliki 
class definisi tanpa konten, tambahkan pass
pernyataan tersebut untuk menghindari kesalahan.'''

class Person:
  pass