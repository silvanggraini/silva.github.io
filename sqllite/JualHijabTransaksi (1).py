class transaksiPenjualan():
    
    def __init__(self, tanggalPenjualan, namaPelanggan, noHpPelanggan):
        self.tanggalPenjualan = tanggalPenjualan
        self.namaPelanggan = namaPelanggan
        self.noHpPelanggan = noHpPelanggan
        self.totalBelanja = []
 
    def Penjualan(self):
        print("1. Pashmina")
        print("2. Segiempat")
        print("3. Ceruty")
        print("4. Jersi")
        print("5. Madam")
        print("6. Wolfis")
        jenisBarangJual = input("Mau belanja apa saja?")
        if jenisBarangJual == "Pashmina":
            print("1. Ceruty")
            print("2. Diamond")
            namaBarang = input("Apa nama barang yang dicari? ")
            jumlahBarangJual = int(input("Berapa banyak yang dibeli?(dalam satuan helai)"))
            if namaBarang == "Ceruty":
                self.totalTP = jumlahBarangJual * 25000 * jumlahBarangJual
            else:
                self.totalTP = jumlahBarangJual * 35000 * jumlahBarangJual
        elif jenisBarangJual == "Segiempat":
            namaBarang = input("Apa nama barang yang dicari?")
            print("1. Bella Squere")
            print("2. Motif")
            jumlahBarangJual = int(input("Berapa banyak yang dibeli?(dalam satuan helai)"))
            if namaBarang == "Bella Squere":
                self.totalTP = jumlahBarangJual * 25000 * jumlahBarangJual
            elif namaBarang == "Motif":
                self.totalTP = jumlahBarangJual * 30000 * jumlahBarangJual
        elif jenisBarangJual == "Ceruty":
            namaBarang = input("Apa nama barang yang dicari?")
            print("1. Ceruty Mini Tali")
            print("2. Ceruty Jumbo Bis")
            print("2. Ceruty Penguin Bordir")
            print("2. Ceruty Penguin Permata")
            jumlahBarangJual = int(input("Berapa banyak yang dibeli?(dalam satuan helai)"))
            if namaBarang == "Ceruty mini tali":
                self.totalTP = jumlahBarangJual * 30000 * jumlahBarangJual
            elif namaBarang == "Ceruti Jumbo Bis":
                self.totalTP = jumlahBarangJual * 60000 * jumlahBarangJual
            elif namaBarang == "Ceruti Pinguin":
                self.totalTP = jumlahBarangJual * 55000 * jumlahBarangJual
            elif namaBarang == "Ceruti Pinguin Bordir":
                self.totalTP = jumlahBarangJual * 75000 * jumlahBarangJual
            elif namaBarang == "Ceruti Pinguin Permata":
                self.totalTP = jumlahBarangJual * 65000 * jumlahBarangJual
        elif jenisBarangJual == "Jersi":
            namaBarang = input("Apa nama barang yang dicari?")
            print("1. KCB tali")
            print("2. Renda ")
            print("2. AntiVirus")
            print("2. Serut Jokowi")
            jumlahBarangJual = int(input("Berapa banyak yang dibeli?(dalam satuan helai)"))
            if namaBarang == "KCB Tali":
                self.totalTP = jumlahBarangJual * 50000 * jumlahBarangJual
            elif namaBarang == "Renda":
                self.totalTP = jumlahBarangJual * 45000 * jumlahBarangJual
            elif namaBarang == "AntiVirus":
                self.totalTP = jumlahBarangJual * 45000 * jumlahBarangJual
            elif namaBarang == "Serut Jokowi":
                self.totalTP = jumlahBarangJual * 25000 * jumlahBarangJual
        self.totalBelanja.append(self.totalTP)
        
    def totalPenjualan(self):
        for i in range (len(self.totalBelanja)):
            self.totalHargaPenjualan = self.totalHargaPenjualan + self.totalTP[i]
            return self.totalHargaPenjualan

    def pembayaran(self, bayar):
        self.kembalikan = bayar - self.totalHargaPenjualan
        if bayar > self.kembalikan:
            print("ini kembalian anda Rp.",self.kembalikan,"Terima kasih sudah belanja")
        elif self.kembalikan == bayar:
            print("uang anda pas, Terima kasih sudah belanja")
        else:
            print("Maaf uang anda kurang")

class transaksiPembelian():

    def __init__(self, tanggalPembelian, namaDistributor, noHpDistributor):
        self.tanggalPembelian = tanggalPembelian
        self.namaDistributor = namaDistributor
        self.noHpDistributor = noHpDistributor
        self.totalBeli = []
        
    def pembelian(self):
        print("1. Yarsi")
        print("2. Ceruty")
        print("3. Madam")
        self.inputanPembelian = int(input("Nama barang yang dibeli:"))
        if self.inputanPembelian == 1:
            self.jumlahBarang = int(input("Banyak barang yang dibeli (dalam hitungan kg) :"))
            self.hargaBeli = self.jumlahBarang * 78000
        elif self.inputanPembelian == 2 :
            self.jumlahBarang = int(input("Banyak barang yang dibeli (dalam hitungan kg) :"))
            self.hargaBeli = self.jumlahBarang * 50000
        else:
            self.jumlahBarang = int(input("Banyak barang yang dibeli (dalam hitungan kg) :"))
            self.hargaBeli = self.jumlahBarang * 70000
        self.totalBeli.append(self.hargaBeli)
            
    def totalPembelian (self):
        for x in range (len(self.totalBeli)):
            self.totalHargaPembelian = self.totalHargaPembelian + self.hargaBeli[x]
            return self.totalHargaPembelian

while 1 > 0:
    print("1. Transakasi Penjualan")
    print("2. Transakasi Pembelian")
    print("3. Exit")
    pilihan = int(input("Masukan pilihan :"))
    if pilihan == 1:
        # con = sqlite.connect 
        tanggalPembelian = input("Masukkan tanggal : ")
        namaDistributor = input("masukan nama Distributor : ")
        noHpDistributor = input("Masukkan no hp Distributor : ")
        user1 = transaksiPenjualan(tanggalPembelian, namaDistributor, noHpDistributor)
        while 1 > 0 :
            user1.Penjualan()
            lagi = print("Apakah anda mau belanja lagi? ")
            if lagi == True:
                user1.Penjualan()
            else:
                user1.totalPenjualan()
                print(user1.totalHargaPenjualan)
                bayar = print("Masukan uang anda : ")
                user1.pembayaran(bayar)
    if pilihan == 2:
        tanggalPenjualan = input("Masukkan tanggal : ")
        namaPelanggan = input("masukan nama pelanggan : ")
        noHpPelanggan = input("Masukkan no hp pelanggan : ")
        user1 = transaksiPembelian(tanggalPembelian, namaDistributor, noHpDistributor)
        while 1 > 0 :
            user1.pembelian()
            lagi = print("Apalagi yang mau dibeli? ")
            if lagi == True:
                user1.pembelian()
            else:
                user1.totalPembelian()
                print(user1.totalHargaPembelian)
                bayar = print("Masukan uang anda : ")
    else:
        exit()

