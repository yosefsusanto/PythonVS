"""
Aplikasi Deteksi Gempa Terkini
"""

def ekstrasi_data():
    """
    Tanggal : 05 Juli 2023
    Waktu : 14:31:29 WIB
    Magnitudo : 4.5
    Kedalaman : 3 km
    Lokasi : LS=2.41 - BT=120.88
    Keterangan : Pusat gempa berada di laut 37 km BaratDaya Sumur
    Dirasakan : Dirasakan (Skala MMI): II-III Sumur, II Munjul
    :retrun:
    """
    hasil = dict()
    hasil['tanggal'] = '05 Juli 2023'
    hasil['waktu'] =  '14:31:29 WIB'
    hasil['magnitudo'] = 4.5
    hasil['kedalaman'] = '3 km'
    hasil['lokasi'] = {'LS' = 2.41, 'BT' = 120.88}
    hasil['keterangan'] = 'Pusat gempa berada di laut 37 km BaratDaya Sumur'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Sumur, II Munjul'
    return hasil

def tampilkan_data(result):
    print(f"Gempa terakhir berdasarkan BMKG")
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Keterangan {result['keterangan']}")
    print(f"dirasakan {result['dirasakan']}")

    
    

if __name__ == '__main__':
    print("Aplikasi utama")
    result = ekstrasi_data()
    tampilkan_data(result)



