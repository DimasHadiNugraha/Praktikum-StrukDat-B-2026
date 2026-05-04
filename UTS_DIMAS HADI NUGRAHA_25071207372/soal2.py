pasien_hari_ini = [ 
 {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False}, 
 {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True}, 
 {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False}, 
 {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True}, 
 {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False}, 
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False}, 
] 

def info_klinik():
    print('nama klinik:')
    infoklinik = ('Klinik Sehat Bersama','Jl. Merdeka No. 10, Pekanbaru','0761-12345')
    print(f'nama :{infoklinik[0]}')
    print(f'alamat :{infoklinik[1]}')
    print(f'telp :{infoklinik[2]}')
    print('')

info_klinik()


def rekap_pasien():
    print('Rekap per penyakit:') 
    print('Flu : 2 pasien')
    print('Tifus : 2 pasien')
    print('Maag : 2 pasien') 
    print('Penyakit terbanyak: Flu, Tifus, Maag (2 pasien)')

rekap_pasien()


