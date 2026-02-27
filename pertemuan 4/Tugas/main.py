# main.py
from kurs import data_kurs
from konverter import konversi
from tabulate import tabulate

def tampilkan_kurs():
    data = []
    for kode, nilai in data_kurs.items():
        data.append([kode, f"{nilai:,.0f}".replace(",", ".")])

    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_kurs()

    daftar_mata_uang = ["IDR"] + list(data_kurs.keys())

    dari = input("Dari (IDR/USD/EUR/SGD/JPY): ").upper()
    ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ").upper()
    jumlah = float(input("Jumlah: "))

    if dari not in daftar_mata_uang or ke not in daftar_mata_uang:
        print("Kode mata uang tidak valid!")
        return

    hasil = konversi(dari, ke, jumlah)

    if dari == "IDR":
        print(f"\nRp {jumlah:,.0f}".replace(",", "."), end="")
    else:
        print(f"\n{jumlah:,.2f} {dari}", end="")

    if ke == "IDR":
        print(f" = Rp {hasil:,.0f}".replace(",", "."))
    else:
        print(f" = {hasil:,.2f} {ke}")

if __name__ == "__main__":
    main()