import sqlite3
from sqlite3 import Error

class connect():
    def __init__(self):
        self.con = None

    def insertData(self, query):
        try:
            self.con = sqlite3.connect('Projekk.db')
            cursor = self.con.cursor()
            cursor.execute(query)
            self.con.commit()
            print('Data berhasil di inputkan')
        except Error as e:
            print(e)

    def selectData(self, query):
        try:
            self.con = sqlite3.connect('Projekk.db')
            cursor = self.con.cursor()
            cursor.execute(query)
            record = cursor.fetchall()
            self.con.commit()
            for tampil in record:
                print(tampil)
        except Error as e:
            print(e)