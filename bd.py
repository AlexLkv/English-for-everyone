import sqlite3


class data():
    def __init__(self):
        self.con = sqlite3.connect('users')
        self.cur = self.con.cursor()

    def login_data(self, i):
        return self.cur.execute(f'SELECT * FROM all_test WHERE id="{i}"').fetchall()
