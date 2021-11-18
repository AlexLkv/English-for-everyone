import random
import sqlite3
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from cryptocode import encrypt, decrypt

from admin import admin_menu
from admin_check import Ui_adch
from autoriz import Ui_vxo
from front import Ui_MainWindow
from getpass import Ui_getpas
from menu import Ui_menu
from reg import Ui_reg
from reyting import reyting
from rezults import Ui_unrez
from test_form import Ui_formtes
from tests import Ui_tests


# ГЛАВНОЕ МЕНЮ
class Menu1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Menu1, self).__init__()
        self.setupUi(self)
        self.btn_testing.clicked.connect(self.onClicked)
        self.btn_autoriz.clicked.connect(self.onClicked)
        self.btn_reyt.clicked.connect(self.onClicked)
        self.btn_testing.setEnabled(False)
        self.entrpass.triggered.connect(self.onClicked)
        self.user.setText("Войдите в систему")
        self.movie = QMovie(f"{random.randrange(1, 4)}.gif")
        self.movie.setScaledSize(QtCore.QSize(150, 150))
        self.label_2.setMovie(self.movie)
        self.movie.start()

    def aut(self, i):
        self.btn_testing.setEnabled(True)
        self.user.setText(i)

    def onClicked(self):
        if self.sender().text() == "Тестирование":
            self.second_form = tests()
            self.second_form.show()
        if self.sender().text() == "Авторизация":
            self.second_form = autoris()
            self.second_form.show()
        if self.sender().text() == "Общий рейтинг":
            self.second_form = reyting()
            self.second_form.show()
        if self.sender().text() == "Введите пароль":
            self.first_form = admin_check()
            self.first_form.show()


class admin_check(QDialog, Ui_adch):
    def __init__(self):
        super().__init__()
        self.setupUi1(self)
        self.exit.clicked.connect(self.onClicked)
        self.cont.clicked.connect(self.onClicked)
        self.err_pas.hide()

    def onClicked(self):
        if self.sender().text() == "Назад":
            self.close()
        if self.sender().text() == "Войти":
            if self.lineEdit.text() == "IamAdmin":
                if self.test.currentText() == "Редактирование":
                    self.second_form = admin_menu(1)
                    self.second_form.show()
                    self.err_pas.hide()
                else:
                    self.second_form = admin_menu(2)
                    self.second_form.show()
                    self.err_pas.hide()
            else:
                self.err_pas.show()


class tests(QDialog, Ui_tests):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_ex.clicked.connect(self.onClicked)
        self.btn_ts.clicked.connect(self.onClicked)
        self.btn_ts_a.clicked.connect(self.onClicked)
        self.btn_ts_b.clicked.connect(self.onClicked)
        self.btn_ts_c.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.sender().text() == "<-- Назад":
            self.close()
        if self.sender().text() == "Узнать средний уровень ":
            self.first_form = test(1)
            self.first_form.show()
            self.setVisible(False)
        if self.sender().text() == "Placement Test A2/B1":
            self.first_form = test(2)
            self.first_form.show()
            self.setVisible(False)
        if self.sender().text() == "Placement Test B2/C1":
            self.first_form = test(3)
            self.first_form.show()
            self.setVisible(False)
        if self.sender().text() == "Placement Test C1/C2":
            self.first_form = test(4)
            self.first_form.show()
            self.setVisible(False)


# НАЧАЛО ТЕСТИРОВАНИЯ
class test(QWidget, Ui_formtes):
    def __init__(self, ts):
        super().__init__()
        self.con1 = sqlite3.connect('users')
        self.cur = self.con1.cursor()
        self.i = 1
        self.count = 0
        self.setupUi(self)
        self.con.hide()
        self.prog.setValue(self.i)
        self.min = 0
        self.h = 0
        self.step = 0
        self.step_2 = 0
        self.min_2 = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)
        self.otv_2.hide()
        self.tes = ts
        if ts == 1:
            self.maxi = self.cur.execute("""SELECT id FROM test1 ORDER BY id DESC""").fetchone()
            value = self.cur.execute(f'SELECT * FROM test1 WHERE id="{1}"').fetchall()
            self.lineEdit.hide()
            self.task.setText(value[0][1])
            self.anc_1.setText(value[0][2])
            self.anc_2.setText(value[0][3])
            self.anc_3.setText(value[0][4])
            self.anc_4.setText(value[0][5])
            self.chet.setText(str(self.i))
            self.chet_3.setText(str(self.count))
            self.con.clicked.connect(self.onClicked)
            self.cont.clicked.connect(self.onClicked)
            self.timer.start(1000)
            self.time = ''
        else:
            if self.tes == 2:
                self.maxi = self.cur.execute("""SELECT id FROM test2 ORDER BY id DESC""").fetchone()
                value = self.cur.execute(f'SELECT * FROM test2 WHERE id="{1}"').fetchall()
            elif self.tes == 3:
                self.maxi = self.cur.execute("""SELECT id FROM test3 ORDER BY id DESC""").fetchone()
                value = self.cur.execute(f'SELECT * FROM test3 WHERE id="{1}"').fetchall()
            elif self.tes == 4:
                self.maxi = self.cur.execute("""SELECT id FROM test4 ORDER BY id DESC""").fetchone()
                value = self.cur.execute(f'SELECT * FROM test4 WHERE id="{1}"').fetchall()
            self.con.clicked.connect(self.onClicked)
            self.cont.clicked.connect(self.onClicked)
            self.lineEdit.show()
            self.anc_1.hide()
            self.anc_2.hide()
            self.anc_3.hide()
            self.anc_4.hide()
            self.a.hide()
            self.b.hide()
            self.c.hide()
            self.d.hide()
            self.chet.setText(str(self.i))
            self.chet_3.setText(str(self.count))
            self.task.setText(value[0][1])
            self.timer.start(1000)
            self.time = ''
            self.label_11.hide()
            self.otv.hide()
        self.prog.setMaximum(self.maxi[0])

    def update_func(self):
        self.step += 1
        if self.step == 10:
            self.step_2 += 1
            self.step = 0
        if self.step_2 == 6:
            self.min += 1
            self.step_2 = 0
            self.step = 0
        if self.min == 10:
            self.min_2 += 1
        if self.min_2 == 6:
            self.h += 1
            self.min = 0
            self.min_2 = 0
            self.step_2 = 0
            self.step = 0
        self.time = str(f"0{self.h}:{self.min_2}{self.min}:{self.step_2}{self.step}")
        self.label.setText(self.time)

    def onClicked(self):
        if self.tes == 1:
            if self.otv.currentText() == self.cur.execute(f'SELECT * FROM test1 WHERE id="{self.i}"').fetchall()[0][6]:
                self.count += 1
            self.i += 1
            self.prog.setValue(self.i)
            if self.i > int(self.maxi[0]):
                self.timer.stop()
                f = open('temp.txt', 'r')
                name = f.readline()
                if self.count < 15:
                    self.lvl = 'A1-A2'
                elif 16 <= self.count <= 30:
                    self.lvl = 'B1-B2'
                else:
                    self.lvl = 'C1-C2'
                value = self.cur.execute(f'SELECT * FROM results WHERE name="{name}"').fetchall()
                if value == []:
                    self.cur.execute("INSERT INTO results (name, lvl, vopr, otv, time)" +
                                     f"VALUES ('{name}', '{self.lvl}', '{self.maxi[0]}', '{self.count}', '{self.time}')")
                else:
                    self.cur.execute("""UPDATE results
                                SET lvl = ?,
                                vopr = ?,
                                otv = ?,
                                time = ?
                                WHERE name = ?""", (
                        self.lvl, self.maxi[0], self.count, self.time, name))
                self.con1.commit()
                self.close()
                self.resul = results(1)
                self.resul.show()
        if self.tes == 2:
            if self.i <= 25 and self.lineEdit.text() == \
                    self.cur.execute(f'SELECT * FROM test2 WHERE id="{self.i}"').fetchall()[0][5]:
                self.count += 1
            if self.i > 25 and self.otv_2.currentText() == \
                    self.cur.execute(f'SELECT * FROM test2 WHERE id="{self.i}"').fetchall()[0][5]:
                self.count += 1
            self.i += 1
            self.prog.setValue(self.i)
            if self.i > int(self.maxi[0]):
                self.timer.stop()
                f = open('temp.txt', 'r')
                name = f.readline()
                if self.count < 20:
                    self.lvl = 'A1'
                elif 20 <= self.count <= 35:
                    self.lvl = 'A2'
                else:
                    self.lvl = 'B1'
                value = self.cur.execute(f'SELECT * FROM results2 WHERE name="{name}"').fetchall()
                if value == []:
                    self.cur.execute("INSERT INTO results2 (name, lvl, vopr, otv, time)" +
                                     f"VALUES ('{name}', '{self.lvl}', '{self.maxi[0]}', '{self.count}', '{self.time}')")
                else:
                    self.cur.execute("""UPDATE results2
                                SET lvl = ?,
                                vopr = ?,
                                otv = ?,
                                time = ?
                                WHERE name = ?""", (
                        self.lvl, self.maxi[0], self.count, self.time, name))
                self.con1.commit()
                self.resul = results(2)
                self.resul.show()
                self.close()
        elif self.tes == 3:
            if self.i <= 25 and self.lineEdit.text() == \
                    self.cur.execute(f'SELECT * FROM test3 WHERE id="{self.i}"').fetchall()[0][5]:
                self.count += 1
            if self.i > 25 and self.otv_2.currentText() == \
                    self.cur.execute(f'SELECT * FROM test3 WHERE id="{self.i}"').fetchall()[0][5]:
                self.count += 1
            self.i += 1
            self.prog.setValue(self.i)
            if self.i > int(self.maxi[0]):
                self.timer.stop()
                f = open('temp.txt', 'r')
                name = f.readline()
                if self.count < 22:
                    self.lvl = 'A1-B1'
                elif 22 <= self.count <= 37:
                    self.lvl = 'B2'
                else:
                    self.lvl = 'C1'
                value = self.cur.execute(f'SELECT * FROM results3 WHERE name="{name}"').fetchall()
                if value == []:
                    self.cur.execute("INSERT INTO results3 (name, lvl, vopr, otv, time)" +
                                     f"VALUES ('{name}', '{self.lvl}', '{self.maxi[0]}', '{self.count}', '{self.time}')")
                else:
                    self.cur.execute("""UPDATE results3
                                SET lvl = ?,
                                vopr = ?,
                                otv = ?,
                                time = ?
                                WHERE name = ?""", (
                        self.lvl, self.maxi[0], self.count, self.time, name))
                self.con1.commit()
                self.close()
                self.resul = results(3)
                self.resul.show()
        elif self.tes == 4:
            if (25 >= self.i or 51 < self.i) and self.lineEdit.text() == \
                    self.cur.execute(f'SELECT * FROM test4 WHERE id="{self.i}"').fetchall()[0][6]:
                self.count += 1
            elif 25 < self.i < 51 and self.otv.currentText() == \
                    self.cur.execute(f'SELECT * FROM test4 WHERE id="{self.i}"').fetchall()[0][6]:
                self.count += 1
            self.i += 1
            self.prog.setValue(self.i)
            if self.i > int(self.maxi[0]):
                self.timer.stop()
                f = open('temp.txt', 'r')
                name = f.readline()
                if self.count < 40:
                    self.lvl = 'A1-B2'
                elif 40 <= self.count <= 59:
                    self.lvl = 'C1'
                else:
                    self.lvl = 'C2'
                value = self.cur.execute(f'SELECT * FROM results4 WHERE name="{name}"').fetchall()
                if value == []:
                    self.cur.execute("INSERT INTO results4 (name, lvl, vopr, otv, time)" +
                                     f"VALUES ('{name}', '{self.lvl}', '{self.maxi[0]}', '{self.count}', '{self.time}')")
                else:
                    self.cur.execute("""UPDATE results4
                                SET lvl = ?,
                                vopr = ?,
                                otv = ?,
                                time = ?
                                WHERE name = ?""", (
                        self.lvl, self.maxi[0], self.count, self.time, name))
                self.con1.commit()
                self.close()
                self.resul = results(4)
                self.resul.show()
        if self.i <= int(self.maxi[0]):
            if self.tes == 1:
                value = self.cur.execute(f'SELECT * FROM test1 WHERE id="{self.i}"').fetchall()
            if self.tes == 2:
                value = self.cur.execute(f'SELECT * FROM test2 WHERE id="{self.i}"').fetchall()
            elif self.tes == 3:
                value = self.cur.execute(f'SELECT * FROM test3 WHERE id="{self.i}"').fetchall()
            elif self.tes == 4:
                value = self.cur.execute(f'SELECT * FROM test4 WHERE id="{self.i}"').fetchall()
            if self.i == self.maxi[0]:
                self.cont.hide()
                self.con.show()
            if (25 >= self.i or 50 < self.i) and self.tes != 1:
                self.task.setText(value[0][1])
                self.chet.setText(str(self.i))
                self.chet_3.setText(str(self.count))
                self.anc_1.hide()
                self.anc_2.hide()
                self.anc_3.hide()
                self.anc_4.hide()
                self.a.hide()
                self.b.hide()
                self.c.hide()
                self.d.hide()
                self.otv.hide()
                self.label_11.hide()
                if self.tes != 1:
                    self.lineEdit.show()
                    self.lineEdit.setText("")
            else:
                self.anc_1.show()
                self.anc_2.show()
                self.anc_3.show()
                self.a.show()
                self.b.show()
                self.c.show()
                if self.tes == 4 or self.tes == 1:
                    self.anc_4.show()
                    self.d.show()
                    self.anc_4.setText(value[0][5])
                self.lineEdit.hide()
                self.label_11.show()
                if self.tes != 2 and self.tes != 3:
                    self.otv.show()
                else:
                    self.otv_2.show()
                self.task.setText(value[0][1])
                self.anc_1.setText(value[0][2])
                self.anc_2.setText(value[0][3])
                self.anc_3.setText(value[0][4])
                self.chet.setText(str(self.i))
                self.chet_3.setText(str(self.count))


class results(QDialog, Ui_unrez):
    def __init__(self, ts):
        super().__init__()
        self.setupUi(self)
        f = open('temp.txt', 'r')
        name = f.readline()
        con = sqlite3.connect('users')
        cur = con.cursor()
        if ts == 1:
            values = cur.execute(f'SELECT * FROM results WHERE name="{name}"').fetchall()
            val = cur.execute("""SELECT name, time, lvl, otv FROM results ORDER BY otv DESC, time ASC""").fetchmany(5)
        elif ts == 2:
            values = cur.execute(f'SELECT * FROM results2 WHERE name="{name}"').fetchall()
            val = cur.execute("""SELECT name, time, lvl, otv FROM results2 ORDER BY otv DESC, time ASC""").fetchmany(5)
        elif ts == 3:
            values = cur.execute(f'SELECT * FROM results3 WHERE name="{name}"').fetchall()
            val = cur.execute("""SELECT name, time, lvl, otv FROM results3 ORDER BY otv DESC, time ASC""").fetchmany(5)
        elif ts == 4:
            values = cur.execute(f'SELECT * FROM results4 WHERE name="{name}"').fetchall()
            val = cur.execute("""SELECT name, time, lvl, otv FROM results4 ORDER BY otv DESC, time ASC""").fetchmany(5)
        self.lvl.setText(str(values[0][1]))
        self.vop.setText(str(values[0][2]))
        self.otv.setText(str(values[0][3]))
        self.time.setText(str(values[0][4]))
        # ОТРИСОВКА ТАБЛИЦЫ РЕЗУЛЬТАТОВ
        self.name_1.setText(str(val[0][0]))
        self.time_1.setText(str(val[0][1]))
        self.lvl_1.setText(str(val[0][2]))
        self.otv_1.setText(str(val[0][3]))
        if len(val) >= 2:
            self.name_2.setText(str(val[1][0]))
            self.time_2.setText(str(val[1][1]))
            self.lvl_2.setText(str(val[1][2]))
            self.otv_2.setText(str(val[1][3]))

        else:
            self.name_2.setText("-")
            self.time_2.setText("-")
            self.lvl_2.setText("-")
            self.otv_2.setText("-")

        if len(val) >= 3:
            self.name_3.setText(str(val[2][0]))
            self.time_3.setText(str(val[2][1]))
            self.lvl_3.setText(str(val[2][2]))
            self.otv_3.setText(str(val[2][3]))
        else:
            self.name_3.setText("-")
            self.time_3.setText("-")
            self.lvl_3.setText("-")
            self.otv_3.setText("-")
        if len(val) >= 4:
            self.name_4.setText(str(val[3][0]))
            self.time_4.setText(str(val[3][1]))
            self.lvl_4.setText(str(val[3][2]))
            self.otv_4.setText(str(val[3][3]))
        else:
            self.name_4.setText("-")
            self.time_4.setText("-")
            self.lvl_4.setText("-")
            self.otv_4.setText("-")
        if len(val) >= 5:
            self.name_5.setText(str(val[4][0]))
            self.time_5.setText(str(val[4][1]))
            self.lvl_5.setText(str(val[4][2]))
            self.otv_5.setText(str(val[4][3]))
        else:
            self.name_5.setText("-")
            self.time_5.setText("-")
            self.lvl_5.setText("-")
            self.otv_5.setText("-")


# МЕНЮ ВЫБОРА АВТОРИЗАЦИИ
class autoris(QWidget, Ui_menu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.onClicked)
        self.autr.clicked.connect(self.onClicked)
        self.reg.clicked.connect(self.onClicked)
        self.getpas.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.sender().text() == "<-- Назад":
            self.close()
        elif self.sender().text() == "Войти":
            self.first_form = vxod()
            self.first_form.show()
            self.setVisible(False)
        elif self.sender().text() == "Зарегистрироваться":
            self.second_form = login1()
            self.second_form.show()
            self.setVisible(False)
        elif self.sender().text() == "Восстановление аккаунта":
            self.third_form = get_pass()
            self.third_form.show()
            self.setVisible(False)


# ВХОД В СИСТЕМУ
class vxod(QWidget, Ui_vxo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.err_not_found.hide()
        self.err_not_found_2.hide()
        self.back.clicked.connect(self.onClicked)
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        self.login = self.name_inp.text()
        fl = open('temp.txt', 'w')
        fl.write(self.login)
        if self.sender().text() == "<-- Назад":
            self.close()

        elif self.sender().text() == "Готово!":
            con = sqlite3.connect('users')
            cur = con.cursor()
            value = cur.execute(f'SELECT name, pass FROM datem WHERE name="{self.login}"').fetchall()
            if value == []:
                self.err_not_found.show()
                self.err_not_found_2.hide()
            elif decrypt(value[0][1], "wow") != self.pas_inp.text():
                self.err_not_found_2.show()
                self.err_not_found.hide()
            else:
                ex.aut(self.login)
                self.close()
                cur.close()


# РЕГИСТРАЦИЯ В СИСТЕМЕ
class login1(QWidget, Ui_reg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.err_name.hide()
        self.err_name_2.hide()
        self.back.clicked.connect(self.onClicked)
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.sender().text() == "<-- Назад":
            self.close()
        if self.sender().text() == "Готово!":
            self.login = self.lineEdit.text()
            con = sqlite3.connect('users')
            cur = con.cursor()
            value = cur.execute(f'SELECT * FROM datem WHERE name="{self.login}"').fetchall()
            # ПРОВЕРКА НА ИМЕЮЩЕЕСЯ ИМЯ
            if self.sender().text() == "Готово!":
                self.pass1 = self.pas1_inp.text()
                self.pass2 = self.pas2_inp.text()
                dt = str(self.dater.date())[19:-1].split(', ')  # СБОР ИНФОРМАЦИИ О ДАТЕ РОЖДЕНИЯ
                self.dt = (dt[0] + "-" + dt[1] + "-" + dt[2])
                if value != []:
                    self.err_name.show()
                elif self.pass1 != self.pass2:
                    self.err_name_2.show()
                    self.err_name.hide()
                else:
                    str_encoded = encrypt(self.pass1, "wow")
                    cur.execute(f"INSERT INTO datem (name, pass, date)"
                                f"VALUES ('{self.login}', '{str_encoded}', '{self.dt}')")
                    fl = open('temp.txt', 'w')
                    fl.write(self.login)
                    ex.aut(self.login)
                    self.close()
                    con.commit()
                    cur.close()


# ВОССТАНОВЛЕНИЕ ПАРОЛЯ
class get_pass(QWidget, Ui_getpas):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.onClicked)
        self.cont_2.clicked.connect(self.onClicked)
        self.err_name_3.hide()
        self.err_name_2.hide()

    def onClicked(self):
        self.login = self.lineEdit.text()

        if self.sender().text() == "<-- Назад":
            self.close()
        elif self.sender().text() == "Узнать!":
            dt = str(self.dater.date())[19:-1].split(', ')  # СБОР ИНФОРМАЦИИ О ДАТЕ РОЖДЕНИЯ
            self.dt = (dt[0] + "-" + dt[1] + "-" + dt[2])
            con = sqlite3.connect('users')
            cur = con.cursor()
            value = cur.execute(f'SELECT * FROM datem WHERE name="{self.login}"').fetchall()
            if value == []:
                self.err_name_3.show()
            elif value[0][3] != self.dt:
                self.err_name_2.show()
                self.err_name_3.hide()
            else:
                self.inp_pass.setText(decrypt(value[0][2], "wow"))
                self.err_name_3.hide()
                self.err_name_2.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu1()
    ex.show()
    sys.exit(app.exec_())
