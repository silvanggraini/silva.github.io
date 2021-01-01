import sqlite3
from sqlite3.dbapi2 import Cursor

class Induk:
    def __init__(self):
        self.con = sqlite3.connect("projekk.db")
        self.cursor = self.con.cursor()

    def execute(self,query, retval=False):
        self.cursor.execute(query)
        if retval:
            results = self.cursor.fetchall()
            self.con.commit()
            return results
            
        else:
            results = self.cursor.fetchone()
         