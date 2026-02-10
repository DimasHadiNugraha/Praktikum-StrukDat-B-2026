'''Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan.
'''
angka = [10, 20, 30, 40, 50]
#1
thislist = [10, 20, 30, 40, 50]

thislist.append("60")

print (thislist)

#2
thislist = [10, 20, 30, 40, 50]
thislist.pop(1)

print (thislist)

#3
angka = [10, 20, 30, 40, 50]
nilaimax = max(angka)
nilaimin = min(angka)

print('angkat tertinggi:',max(angka))
print('angkat terrendah:',min(angka))

#4
angka = [10,30,40,50,60]









