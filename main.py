import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

import bd


# ГЛАВНОЕ МЕНЮ

class Menu1(QMainWindow):
    def __init__(self):
        super(Menu1, self).__init__()
        uic.loadUi('front.ui', self)
        self.btn_testing.clicked.connect(self.onClicked)
        self.btn_autoriz.clicked.connect(self.onClicked)
        self.btn_reyt.clicked.connect(self.onClicked)
        self.btn_testing.setEnabled(False)
        self.user.setText("Войдите в систему")

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
            pass


# НАЧАЛО ТЕСТИРОВАНИЯ
class tests(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('tests.ui', self)
        self.btn_ex.clicked.connect(self.onClicked)
        self.btn_ts.clicked.connect(self.onClicked)
        self.btn_ts_a.clicked.connect(self.onClicked)
        self.btn_ts_b.clicked.connect(self.onClicked)
        self.btn_ts_c.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.sender().text() == "<-- Назад":
            self.close()
        elif self.sender().text() == "Узнать средний уровень ":
            self.first_form = altest()
            self.first_form.show()
            self.setVisible(False)
        elif self.sender().text() == "Тест level A1-А2":
            pass
        elif self.sender().text() == "Тест level B1-B2":
            pass
        elif self.sender().text() == "Тест level C1-C2":
            pass


class altest(QWidget):
    def __init__(self):
        super().__init__()
        self.con1 = sqlite3.connect('users')
        self.cur = self.con1.cursor()
        self.i = 59
        self.count = 0
        self.maxi = self.cur.execute("""SELECT id FROM all_test ORDER BY id DESC""").fetchone()
        self.ui = uic.loadUi('untitled.ui', self)
        self.cont.clicked.connect(self.onClicked)
        self.con.clicked.connect(self.onClicked)
        self.con.hide()
        self.ui.prog.setMaximum(self.maxi[0])
        self.ui.prog.setValue(self.i)
        self.min = 0
        self.h = 0
        self.step = 0
        self.step_2 = 0
        self.min_2 = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)
        self.timer.start(1000)
        self.time = ''

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
        if self.ui.otv.currentText() == bd.Data.vopros(self, self.i)[0][6]:
            self.count += 1
        self.i += 1
        self.ui.prog.setValue(self.i)
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
            self.cur.execute(
                "INSERT INTO results (name, lvl, vopr, otv, time)" +
                f"VALUES ('{name}', '{self.lvl}', '{self.maxi[0]}', '{self.count}', '{self.time}')")
            self.con1.commit()
            self.resul = results()
            self.resul.show()
        if self.i != 1 and self.i <= int(self.maxi[0]):
            if self.i == self.maxi[0]:
                self.cont.hide()
                self.con.show()
            value = self.cur.execute(f'SELECT * FROM all_test WHERE id="{self.i}"').fetchall()
            self.ui.task.setText(value[0][1])
            self.ui.anc_1.setText(value[0][2])
            self.ui.anc_2.setText(value[0][3])
            self.ui.anc_3.setText(value[0][4])
            self.ui.anc_4.setText(value[0][5])
            self.ui.chet.setText(str(self.i))
            self.ui.chet_3.setText(str(self.count))


class results(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('rezults.ui', self)
        f = open('temp.txt', 'r')
        name = f.readline()
        con = sqlite3.connect('users')
        cur = con.cursor()
        values = cur.execute(f'SELECT * FROM results WHERE name="{name}"').fetchall()
        self.lvl.setText(str(values[0][1]))
        self.vop.setText(str(values[0][2]))
        self.otv.setText(str(values[0][3]))
        self.time.setText(str(values[0][4]))



# МЕНЮ ВЫБОРА АВТОРИЗАЦИИ
class autoris(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
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
class vxod(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('autoriz.ui', self)
        self.err_not_found.hide()
        self.err_not_found_2.hide()
        self.back.clicked.connect(self.onClicked)
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        self.login = self.ui.name_inp.text()
        f = open('temp.txt', 'w')
        f.write(self.login)
        if self.sender().text() == "<-- Назад":
            self.close()

        elif self.sender().text() == "Готово!":
            con = sqlite3.connect('users')
            cur = con.cursor()
            value = cur.execute(f'SELECT name, pass FROM datem WHERE name="{self.login}"').fetchall()
            if value == []:
                self.err_not_found.show()
            elif value[0][1] != self.ui.pas_inp.text():
                self.err_not_found_2.show()
            else:
                ex.aut(self.login)
                self.close()
                cur.close()


# РЕГИСТРАЦИЯ В СИСТЕМЕ
class login1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('login.ui', self)
        self.ui.err_name.hide()
        self.ui.err_name_2.hide()
        self.back.clicked.connect(self.onClicked)
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.sender().text() == "<-- Назад":
            self.close()
        if self.sender().text() == "Готово!":
            self.login = self.ui.lineEdit.text()
            con = sqlite3.connect('users')
            cur = con.cursor()
            value = cur.execute(f'SELECT * FROM datem WHERE name="{self.login}"').fetchall()
            # ПРОВЕРКА НА ИМЕЮЩЕЕСЯ ИМЯ
            if self.sender().text() == "Готово!":
                self.pass1 = self.ui.pas1_inp.text()
                self.pass2 = self.ui.pas2_inp.text()
                dt = str(self.ui.dater.date())[19:-1].split(', ')  # СБОР ИНФОРМАЦИИ О ДАТЕ РОЖДЕНИЯ
                self.dt = (dt[0] + "-" + dt[1] + "-" + dt[2])
                if value != []:
                    self.ui.err_name.show()
                elif self.pass1 != self.pass2:
                    self.ui.err_name_2.show()
                else:
                    cur.execute(f"INSERT INTO datem (name, pass, date)"
                                f"VALUES ('{self.login}', '{self.pass1}', '{self.dt}')")
                    f = open('temp.txt', 'w')
                    f.write(self.login)
                    ex.aut(self.login)
                    self.close()
                    con.commit()
                    cur.close()


# ВОССТАНОВЛЕНИЕ ПАРОЛЯ
class get_pass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('getpass.ui', self)
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
                self.inp_pass.setText(value[0][2])
                self.err_name_3.hide()
                self.err_name_2.hide()


# ВКЛАДКА РЕЙТИНГА
class reyting(QWidget):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu1()
    ex.show()
    sys.exit(app.exec_())
