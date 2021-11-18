import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from add_test import Ui_adte

class admin_menu(QDialog, Ui_adte):
    def __init__(self, ts):
        super().__init__()
        self.con = sqlite3.connect('users')
        self.cur = self.con.cursor()
        self.ts1 = ts
        if ts == 1:
            uic.loadUi('edit_test.ui', self)
        else:
            self.setupUi1(self)
        self.err.hide()
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.vop.text() != '' and self.otv.text() != '' and self.ts1 != 1:
            if self.test.currentText() == "Тест на средний уровень":
                self.cur.execute("INSERT INTO test1 (Question, ans1, ans2, ans3, ans4, right_ans)" +
                                 f"VALUES ('{self.vop.text()}', '{self.otv1.text()}', '{self.otv2.text()}', '{self.otv3.text()}', '{self.otv4.text()}', '{self.otv.text()}')")
                self.con.commit()
                self.close()
            elif self.test.currentText() == "Placement Test A2/B1":
                self.cur.execute("INSERT INTO test2 (Question, ans1, ans2, ans3, right_ans)" +
                                 f"VALUES ('{self.vop.text()}', '{self.otv1.text()}', '{self.otv2.text()}', '{self.otv3.text()}', '{self.otv.text()}')")
                self.con.commit()
                self.close()
            elif self.test.currentText() == "Placement Test B2/C1":
                self.cur.execute("INSERT INTO test3 (Question, ans1, ans2, ans3, right_ans)" +
                                 f"VALUES ('{self.vop.text()}', '{self.otv1.text()}', '{self.otv2.text()}', '{self.otv3.text()}', '{self.otv.text()}')")
                self.con.commit()
                self.close()
            elif self.test.currentText() == "Placement Test C1/C2":
                self.cur.execute("INSERT INTO test4 (Question, ans1, ans2, ans3, right_ans)" +
                                 f"VALUES ('{self.vop.text()}', '{self.otv1.text()}', '{self.otv2.text()}', '{self.otv3.text()}', '{self.otv.text()}')")
                self.con.commit()
                self.close()
        elif self.vop.text() != '' and self.otv.text() != '' and self.num.text() != '' and self.ts1 == 1:
            if self.test.currentText() == "Тест на средний уровень":
                self.cur.execute("""UPDATE test1
                SET Question = ?,
                ans1 = ?,
                ans2 = ?,
                ans3 = ?,
                ans4 = ?,
                right_ans = ?
                WHERE id = ?""", (
                    self.vop.text(), self.otv1.text(), self.otv2.text(), self.otv3.text(), self.otv4.text(),
                    self.otv.text(), self.num.text()))
                self.con.commit()
                self.close()
            elif self.test.currentText() == "Placement Test A2/B1":
                self.cur.execute("""UPDATE test2
                                SET question = ?,
                                ans1 = ?,
                                ans2 = ?,
                                ans3 = ?,
                                right_ans = ?
                                WHERE id = ?""", (
                    self.vop.text(), self.otv1.text(), self.otv2.text(), self.otv3.text(), self.otv.text(),
                    self.num.text()))
                self.con.commit()
                self.close()
            elif self.test.currentText() == "Placement Test B2/C1":
                self.cur.execute("""UPDATE test3
                                SET question = ?,
                                ans1 = ?,
                                ans2 = ?,
                                ans3 = ?,
                                right_ans = ?
                                WHERE id = ?""", (
                    self.vop.text(), self.otv1.text(), self.otv2.text(), self.otv3.text(), self.otv.text(),
                    self.num.text()))
                self.con.commit()
                self.close()
            elif self.test.currentText() == "Placement Test C1/C2":
                self.cur.execute("""UPDATE test4
                                    SET question = ?,
                                    ans1 = ?,
                                    ans2 = ?,
                                    ans3 = ?,
                                    ans4 = ?,
                                    right_ans = ?
                                    WHERE id = ?""", (
                    self.vop.text(), self.otv1.text(), self.otv2.text(), self.otv3.text(), self.otv4.text(), self.otv.text(),
                    self.num.text()))
                self.con.commit()
                self.close()
        else:
            self.err.show()
