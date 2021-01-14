 def jenisBarangJual1(self, jenisBarang, ukuran):
        if jenisBarangJual == "Madam":
            if ukuran == "XL":
                hargaBarangJual = jumlahBarangJual * 50000
            elif ukuran == "L":
                hargaBarangJual = jumlahBarangJual * 45000
            else:
                hargaBarangJual = jumlahBarangJual * 40000
        elif jenisBarangJual == "Wolfis":
            if ukuran == "XL":
                hargaBarangJual = jumlahBarangJual * 50000
            else:
                hargaBarangJual = jumlahBarangJual * 45000

    def jenisBarangJual2(self, jenisBarang, namaBarang):
        if jenisBarang == Pashmina:
            if namaBarang == "Ceruty":
                hargaBarangJual= jumlahBarangJual * 25000
            else:
                hargaBarangJual= jumlahBarangJual * 35000
        elif jenisBarangJual == "Segiempat":
            if namaBarang == "Bella Squere":
                hargaBarangJual = jumlahBarangJual * 25000
            elif namaBarang == "Motif":
                hargaBarangJual = jumlahBarangJual * 30000
        elif jenisBarangJual == "Ceruty":
            if namaBarang == "Ceruty mini tali":
                hargaBarangJual = jumlahBarangJual * 30000
            elif namaBarang == "Ceruti Jumbo Bis":
                hargaBarangJual = jumlahBarangJual * 60000
            elif namaBarang == "Ceruti Pinguin":
                hargaBarangJual = jumlahBarangJual * 55000
            elif namaBarang == "Ceruti Pinguin Bordir":
                hargaBarangJual = jumlahBarangJual * 75000
            elif namaBarang == "Ceruti Pinguin Permata":
                hargaBarangJual = jumlahBarangJual * 65000
        elif jenisBarangJual == "Jersi":
            if namaBarang == "KCB Tali":
                hargaBarangJual = jumlahBarangJual * 50000
            elif namaBarang == "Renda":
                hargaBarangJual = jumlahBarangJual * 45000
            elif namaBarang == "AntiVirus":
                hargaBarangJual = jumlahBarangJual * 45000
            elif namaBarang == "Serut Jokowi":
                hargaBarangJual = jumlahBarangJual * 25000
