'''Diberikan sebuah list angka:
angka = [10, 20, 30, 40, 50]
1. Tambahkan angka 60 ke dalam list.
2. Hapus angka 20 dari list.
3. Tampilkan angka tertinggi dan terendah
4. Hitung rata-rata angka setelah perubahan data
5. Tampilkan seluruh isi list setelah perubahan.
'''

#1
angka = [10, 20, 30, 40, 50]

angka.append(60)

print (angka)

#2
angka.remove(20)
print(angka)

#3

nilaimax = max(angka)
nilaimin = min(angka)

print('angkat tertinggi:',max(angka))
print('angkat terrendah:',min(angka))

#4
rata_rata = sum(angka) / len(angka)
print(rata_rata)

print(angka)









