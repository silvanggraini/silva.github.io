import sqlite3
from Connect import connect

class pelanggan():
    def insertDataPelanggan(self):
        nama = input("Nama pelanggan :")
        noHp = input("No hp pelanggan :")
        alamat = input("Alamat :")
        self.query = 'INSERT INTO pelanggan (namaPelanggan, noHpPelanggan, alamat)'
        'VALUES ( \'%s\', \'%s\', \'%s\');'
        self.query = self.query % (nama, noHp, alamat)
        self.executeQuery(self.query)

        