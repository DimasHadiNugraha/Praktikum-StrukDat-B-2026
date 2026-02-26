'''4. Sebuah data mahasiswa disimpan dalam bentuk dictionary:'''
mahasiswa = {
"A001": {"nama": "Budi", "prodi": "Informatika",
"ipk": 3.45},
"A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
"A003": {"nama": "Andi", "prodi": "Informatika",
"ipk": 3.75}
}
'''1. Tampilkan nama mahasiswa yang memiliki IPK di atas 3.5.
2. Hitung rata-rata IPK seluruh mahasiswa.
3. Tambahkan satu data mahasiswa baru ke dalam dictionary tersebut.'''

#1
for x in mahasiswa:
    if (mahasiswa[x]["ipk"]) > 3.5:
        print(mahasiswa[x]["nama"]) 

#2
hitung = 0
jumlah = 0
for x in mahasiswa:
    jumlah = jumlah + (mahasiswa[x]["ipk"])
    hitung = hitung + 1
avgIPK = jumlah/hitung
print(f"{avgIPK:.2f}")

#4
mahasiswa["A004"] = {"nama": "dimas", "prodi":"Informatika", "ipk":3.4 }

for x, obj in mahasiswa.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])



