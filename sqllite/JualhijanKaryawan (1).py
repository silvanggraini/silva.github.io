import sqlite3
conn = sqlite3.connect('Projekk.db')
cursor= conn.cursor()
class karyawan():
    
    def __init__(self,namaKaryawan, umurKaryawan, alamatKaryawan, gaji):
        self.namaKaryawan = namaKaryawan
        self.umurKaryawan = umurKaryawan
        self.alamatKaryawan = alamatKaryawan
        self.gaji = gaji

    def upah (self, diambil):
        self.sisa = self.gaji - diambil
        if self.gaji > diambil:
            print("sisaGaji", self.namaKaryawan,"Rp.",self.sisa)
        elif diambil > self.gaji :
            print("Hutang",self.namaKaryawan,"Rp.",self.sisa)
        else:
            print("sisaGaji",self.namaKaryawan,"Rp.",0)

tampung_nama = input("Masukkan nama karyawan")
tampung_umur = int(input("Masukkan umur"))
tampung_alamat = input("Masukkan alamat")
tampung_gaji = int(input("Masukkan gaji"))
tampung_gajiDiambil = int(input("Masukkan gajiDiambil"))
user1 = karyawan(tampung_nama, tampung_umur, tampung_alamat, tampung_gaji)
print(user1.__dict__)
print(user1.upah(tampung_gajiDiambil))
con = sqlite3.connect('Projekk.db')
cursor= con.cursor()
cursor.execute("INSERT INTO Karyawan (nama, umur, alamat, gaji, gajiDiambil)VALUES ('{}' , '{}', '{}', '{}', '{}') ;".format(tampung_nama, tampung_umur, tampung_alamat, tampung_gaji, tampung_gajiDiambil))
con.commit