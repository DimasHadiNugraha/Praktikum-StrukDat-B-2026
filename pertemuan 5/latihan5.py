'''. Diberikan list nilai mahasiswa: nilai_tugas = [70,85, 90, 65, 80] 
a. Ganti nilai 65 menjadi 75 menggunakan pencarian indeks.
b. Tambahkan nilai 95 ke dalam list, lalu urutkan list tersebut dari yang terbesar ke
terkecil.
c. Tampilkan jumlah total seluruh nilai dalam list tersebut.
d. Tampilkan pesan "Ada nilai sempurna" jika angka 100 ada di dalam list, jika tidak
tampilkan "Tidak ada”.'''

nilai_tugas = [70,85, 90, 65, 80]
#a
nilai_tugas[3] = 75
print(nilai_tugas)


#b
nilai_tugas.append(95)
print(nilai_tugas)
nilai_tugas.sort()
print(nilai_tugas)

#c
total = sum(nilai_tugas)
print(total)

#d
for x in nilai_tugas:
    if x == 100:
        print('ada nilai sempurna')
    else:
        print('tidak ada')


'''Diberikan sebuah list yang berisi beberapa tuple. Setiap tuple berisi (Nama, Nilai):
kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]
a. Gunakan perulangan untuk memproses setiap tuple tersebut. Jika nilai >= 75,
tampilkan: "Selamat [Nama], Anda Lulus!". Jika di bawah 75, tampilkan: "Maaf
[Nama], Anda harus remidi."'''

kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]
for nama,nilai in kumpulan_nilai:
    print(f"selamat {nama}, anda lulus") if nilai >=75 else print(f"maaf {nama}anda harus remedi")




'''
Diberikan dua daftar hadir mahasiswa di dua sesi yang berbeda:
sesi_pagi = {"Andi", "Budi", "Cici"} sesi_siang = {"Budi", "Deni", "Eka"}
a. Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang)
b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua
sesi tanpa duplikat).
c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.
'''


sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}

#a
hadir = sesi_pagi.intersection (sesi_siang)
print(hadir)


#b
set3 = sesi_pagi.union(sesi_siang)
print(set3)

#c
sesi_hari_ini = sesi_pagi.union(sesi_siang)
print(sesi_hari_ini)

4. 
transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]
'''
a. Ubah jumlah buku menjadi 8.
b. Tambahkan 2 produk baru.
c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan
perulangan.
Tampilkan ringkasan seperti ini:
Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.'''

#a
for i in transaksi:
    if i ["produk"] == "Buku":
        i.update({"jumlah" : 8})
    print(i)

#b
transaksi += [{"produk": "polio", "harga": 1000, "jumlah": 10},
{"produk": "krayon", "harga": 15000, "jumlah": 5}]
print(transaksi)

for i in range(len(transaksi)):
    print(f"{transaksi[i]["produk"]} | total {transaksi[i]['harga'] * transaksi[i]["jumlah"]}" )
