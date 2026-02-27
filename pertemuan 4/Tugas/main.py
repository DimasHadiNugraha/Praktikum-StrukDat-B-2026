from kurs import data_kurs #mengimport dari kurs.py
from konverter import konversi #mengimport dari konverter.py
from tabulate import tabulate #untuk menampikan tabel dengan rapi

def tampilkan_kurs():
    data = []
    for kode, nilai in data_kurs.items():
        data.append([kode, f"{nilai:,.0f}".replace(",", ".")])

    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid")) #menampikan tabel 

def main():
    tampilkan_kurs()

    daftar_mata_uang = ["IDR"] + list(data_kurs.keys())

    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper() #meminta inputan dari penguna
    ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    if dari not in daftar_mata_uang or ke not in daftar_mata_uang: #memriksa jika pengguna memasukan kode yang salah
        print("Kode mata uang tidak valid!")
        return

    hasil = konversi(dari, ke, jumlah) #menghitung hasil dengan memanggil fungi yang ada di konverter.py
# format untuk meanpikan . , di jumlah dan hasil dengan rapi
    if dari == "IDR":
        print(f"\nRp {jumlah:,.0f}".replace(",", "."), end="")
    else:
        print(f"\n{jumlah:,.2f} {dari}", end="")

    if ke == "IDR":
        print(f" = Rp {hasil:,.0f}".replace(",", "."))
    else:
        print(f" = {hasil:,.2f} {ke}")
#menjalankan program utama
if __name__ == "__main__":
    main()