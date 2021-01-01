class jualHijab():
    def __init__(self):
        pass

    def login (nama, password):
        for j in range (3,1,0):
            for i in range (len(database)):
                if nama == database[i] and password == database[i]:
                    return (nama, password)
                return -1
            print ("maaf nama atau password anda salah", "silahkan coba",j, "kali lagi")
        print("Maaf nama atau password anda salah")

    def karyawan(self,nama, umur, alamat, gaji):
        self.namaKaryawan = namaKaryawan
        self.umurKaryawan = umurKaryawan
        self.alamatKaryawan = alamatKaryawan
        self.gaji = gaji

    def gaji(self, diambil):
        self.ditabung = self.gaji - self.diambil
        return ditabung

class tampilkan(karyawan):
    def __init__(self):
        pass

    def tampil():
        for x in range database:
            print

class transaksi():
    def __init__():
        pass

    def pengirimanBarang(self, tanggalKirim, namaToko, alamatToko, noHpPengirim, jenisBarangDikirim, 
        jumlahBarangDikirim, hargaKirim):
        self.tanggalKirim = tanggalKirim
        self.namaToko = namaToko
        self.alamatToko = alamatToko
        self.noHpPengirim = noHpPengirim
        self.jenisBarangDikirim = jenisBarangDikirim
        self.jumlahBarangDikirim = jumlahBarangDikirim
        self.hargaKirim = hargaKirim

    def totalPengiriman (self, bayar):
        self.totalHargaPengiriman = jumlahBarang * harga
        self.kembalikan = bayar - totalHargaPengiriman
        if bayar > kembalikan:
            print("ini kembalian anda Rp.",self.kembalikan,"Terima kasih sudah belanja")
        elif kembalikan == bayar:
            print("uang anda pas, Terima kasih sudah belanja")
        else:
            print("Maaf uang anda kurang")

    def tampilPengiriman():
        for x in range database:

class transaksiMasuk(transaksi):
    def __init__():
        pass
        
    def barangMasuk(self, tanggal, namaPengirim, alamatPengirim, noHp, jenisBarang, jumlahBarang, harga):
        self.tanggalMasuk = tanggalMasuk
        self.namaPengirim = namaPengirim
        self.alamatPengirim = alamatPengirim
        self.noHp = noHp
        self.jenisBarang = jenisBarang
        self.jumlahBarang = jumlahBarang
        self.harga = harga

    def totalBarangMasuk (self):
        self.totalBarangMasuk = jumlahBarang * harga

class laporan()
    def __init__(self):
        self.keuntungan = self.totalHargaPengiriman - (self.totalBarangMasuk + self.gaji)
        return keuntungan

    def laporan(self):
        print ("Tanggal : {}, \n\tGaji Karyawan : {}, \n\tBarang Masuk : {}, \n\tPengiriman Barang : {}, \n\tKeuntungan"
            .format(self.tanggal, self.gaji, self.totalHarga, self.totalHarga, self.keuntungan
            )
        )

