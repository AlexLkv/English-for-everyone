import sqlite3


class Data:
    def __init__(self):
        self.con = sqlite3.connect('users')
        self.cur = self.con.cursor()

    def vopros(self, i):
        return self.cur.execute(f'SELECT * FROM all_test WHERE id="{i}"').fetchall()