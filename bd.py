import sqlite3


class Data:
    def __init__(self):
        self.con = sqlite3.connect('users')
        self.cur = self.con.cursor()

    def vopros(self, i, c):
        if c == 1:
            return self.cur.execute(f'SELECT * FROM all_test WHERE id="{i}"').fetchall()
        elif c == 2:
            return self.cur.execute(f'SELECT * FROM test2 WHERE id="{i}"').fetchall()