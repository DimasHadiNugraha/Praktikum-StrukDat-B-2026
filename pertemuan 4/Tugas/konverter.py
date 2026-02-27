from kurs import data_kurs

def konversi(dari, ke, hasil):
    #jika dari dan ke nya sama maka hasilnya tetap
    if dari == ke:
        return hasil
    #jika dari idr maka akan dibagi
    if dari == "IDR":
        return hasil / data_kurs[ke]
    #jika ke sama sengan idr maka akan dikali
    if ke == "IDR":
        return hasil * data_kurs[dari]
    #jika keduanya bukan dari idr makan akan dikonversi ke idr
    jumlah_idr = hasil * data_kurs[dari]
    return jumlah_idr / data_kurs[ke]
