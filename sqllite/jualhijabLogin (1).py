import sqlite3
con = sqlite3.connect('Projekk.db')
cursor= con.cursor()
class jualHijab():
    def init(self):
        pass
    
    def login (self, email, password):
       self.query = "select email , pasword from login where email ='{}' and pasword = '{}';".format(email , password)
       cursor.execute(self.query)  
       data_user = cursor.fetchone()
       if data_user != None:
           print('Selamat anda berhasil masuk')
tampung_email = input("Masukkan email")
tampung_pasword = input("Masukkan pasword")
user1 = jualHijab()
user1.login(tampung_email,tampung_pasword)