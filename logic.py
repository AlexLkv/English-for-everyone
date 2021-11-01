import sqlite3


def check(self, pas1, pas2):
    if pas1 == pas2:
        return 0
    else:
        return 1