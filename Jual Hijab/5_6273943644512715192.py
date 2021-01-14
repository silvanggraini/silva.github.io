tipe_kerudung = ['Segi Empat', 'Segi Empat', 'Segi Empat', 'Segi Empat', 
                'Pashmina', 'Pashmina', 'Pashmina', 'Pashmina', 'Pashmina', 
                'Syar\'i', 'Syar\'i', 'Syar\'i', 'Syar\'i', 'Syar\'i',]
jenis_kerudung = ['Bella Square', 'Arabia', 'Hijabhijub', 'Rahmahijab',
                    'Ceruty', 'Diamond', 'Jenis Kaos', 'Jenis Arab', 'Sabyan',
                    'Aminah', 'Rahmahijab', 'Aulia', 'Syaida', 'Rafilla',]
harga_kerudung = [20000, 15000, 35000, 50000,
                    45000, 45000, 30000, 40000, 25000,
                    70000, 80000, 60000, 79000, 75000,]
jumlah_kerudung = len(jenis_kerudung)

def buble_sort(jenis_urutan):
    for i in range(1, jumlah_kerudung):
        for j in range(i, 0, -1):
            if jenis_urutan[j] < jenis_urutan[j-1]:
                temp_tipe = tipe_kerudung[j-1]
                tipe_kerudung[j-1] = tipe_kerudung[j]
                tipe_kerudung[j] = temp_tipe
                temp_jenis = jenis_kerudung[j-1]
                jenis_kerudung[j-1] = jenis_kerudung[j]
                jenis_kerudung[j] = temp_jenis
                temp_harga = harga_kerudung[j-1]
                harga_kerudung[j-1] = harga_kerudung[j]
                harga_kerudung[j] = temp_harga

def tampil_data_urut(jawaban):
    print("DATA KERUDUNG SETELAH DIURUTKAN BERDASARKAN", jawaban.upper())
    print(f'{"No"} \t{"Tipe Kerudung"} \t{"Jenis Kerudung"} \t {"Harga"}')
    print('-'*55)
    for i in range(jumlah_kerudung):
        print(f'{i+1} \t{tipe_kerudung[i]}  \t {jenis_kerudung[i]}  \t {harga_kerudung[i]}')
    print('-'*55)
    kembali()
    
def linear_search(jenis_cari, data_yang_cari):
    no = 1
    print(f'{"No"} \t{"Tipe Kerudung"} \t{"Jenis Kerudung"} \t {"Harga"}')
    print('-'*55)
    for i in range(jumlah_kerudung):
        if data_yang_cari == jenis_cari[i]:
            print(f'{no} \t{tipe_kerudung[i]}  \t {jenis_kerudung[i]}  \t {harga_kerudung[i]}')
            no += 1
    kembali()

def kembali():
    input('Klik apa saja untuk kembali. . .')
    tampil_menu()

def tampil_menu():
    print('\nMENU :')
    print('1. Urutkan data')
    print('2. Mencari data')
    print('3. Keluar program')
    pilih_menu = input('Pilih menu : ')
    if pilih_menu == '1':
        jawaban = input('Mengurutkan data berdasarkan apa?\n')
        if jawaban == 'tipe kerudung':
            buble_sort(tipe_kerudung)
            tampil_data_urut(jawaban)
        elif jawaban == 'jenis kerudung':
            buble_sort(jenis_kerudung)
            tampil_data_urut(jawaban)
        elif jawaban == 'harga':
            buble_sort(harga_kerudung)
            tampil_data_urut(jawaban)
        else:
            print('Sepertinya anda salah ketik')

    elif pilih_menu == '2':
        print('[1. Tipe Kerudung] [2. Jenis Kerudung]')
        jawaban = input('Cari berdasarkan :\n')
        if jawaban == '1' or jawaban == 'tipe kerudung':
            buble_sort(tipe_kerudung)
            cari = input('Cari data : ')
            linear_search(tipe_kerudung, cari)
        elif jawaban == '2' or jawaban == 'jenis kerudung':
            buble_sort(tipe_kerudung)
            cari = input('Cari data : ')
            linear_search(jenis_kerudung, cari)
        else:
            print('Pilihan tidak ada')
            kembali()

    elif pilih_menu == '3':
        exit()
    else:
        print('Tekan apa saja untuk kembali')

## Kerudung program
print("DATA KERUDUNG\n")

print(f'{"No"} \t{"Tipe Kerudung"} \t{"Jenis Kerudung"} \t {"Harga"}')
print('-'*55)
for i in range(jumlah_kerudung):
    print(f'{i+1} \t{tipe_kerudung[i]}  \t {jenis_kerudung[i]}  \t {harga_kerudung[i]}')
print('-'*55)

tampil_menu()
