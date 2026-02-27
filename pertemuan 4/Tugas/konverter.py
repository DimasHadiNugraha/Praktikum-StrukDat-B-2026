# konverter.py
from kurs import data_kurs

def konversi(dari, ke, jumlah):
    # Jika mata uang sama
    if dari == ke:
        return jumlah

    # Jika dari IDR ke mata uang lain
    if dari == "IDR":
        return jumlah / data_kurs[ke]

    # Jika ke IDR
    if ke == "IDR":
        return jumlah * data_kurs[dari]

    # Jika bukan IDR ke bukan IDR
    # Ubah dulu ke IDR lalu ke mata uang tujuan
    jumlah_idr = jumlah * data_kurs[dari]
    return jumlah_idr / data_kurs[ke]
