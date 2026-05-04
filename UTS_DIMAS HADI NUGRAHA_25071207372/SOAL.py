
pasien_hari_ini = [ 
 {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False}, 
 {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True}, 
 {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False}, 
 {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True}, 
 {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False}, 
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False}, 
] 

for data in pasien_hari_ini:
     if data['bayar'] == True:
        data['bayar'] = 'lunas' 
     else:
        data['bayar'] = 'belum lunas'

def tampilkan_pasien():
    print('===daftar pasien klinik===')
    if data in pasien_hari_ini:
        print(f'ID:{data['id']} | Nama:{data['nama']} | Usia{data['usia']} | Penyakit{data['penyakit']} | Status Bayar{data['status bayar']} ')
    print()



def pasie_belum_bayar():
    print('===pasien belum bayar===')
    for data in pasien_hari_ini:
        if data['bayar'] == 'belum bayra':
            print(f'{data['nama']}')
    print()
    

tampilkan_pasien()
pasie_belum_bayar()










    


    
