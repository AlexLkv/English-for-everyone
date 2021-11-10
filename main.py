import sqlite3
import sys

import cryptocode
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
        self.entrpass.triggered.connect(self.onClicked)
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
        if self.sender().text() == "Введите пароль":
            self.first_form = admin_check()
            self.first_form.show()


class admin_check(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('admin_check.ui', self)
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
                else:
                    self.second_form = admin_menu(2)
                    self.second_form.show()
            else:
                self.err_pas.show()


class admin_menu(QDialog):
    def __init__(self, ts):
        super().__init__()
        self.con = sqlite3.connect('users')
        self.cur = self.con.cursor()
        self.ts1 = False
        if ts == 1:
            uic.loadUi('edit_test.ui', self)
            self.ts1 = True
        else:
            uic.loadUi('add_test.ui', self)
        self.err.hide()
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.vop.text() != '' and self.otv.text() != '' and self.ts1 is not True:
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
        elif self.vop.text() != '' and self.otv.text() != '' and self.num.text() != '' and self.ts1 is True:
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
        else:
            self.err.show()


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
        if self.sender().text() == "Узнать средний уровень ":
            self.first_form = test(1)
            self.first_form.show()
            self.setVisible(False)
        if self.sender().text() == "Placement Test A2/B1":
            self.first_form = test(2)
            self.first_form.show()
            self.setVisible(False)
        if self.sender().text() == "Тест level B1-B2":
            pass
        if self.sender().text() == "Тест level C1-C2":
            pass


# НАЧАЛО ТЕСТИРОВАНИЯ
class test(QWidget):
    def __init__(self, ts):
        super().__init__()
        self.con1 = sqlite3.connect('users')
        self.cur = self.con1.cursor()
        self.i = 1
        self.count = 0
        self.ui = uic.loadUi('untitled.ui', self)
        self.con.hide()
        self.ui.prog.setValue(self.i)
        self.min = 0
        self.h = 0
        self.step = 0
        self.step_2 = 0
        self.min_2 = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)
        self.ui.otv_2.hide()
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
        if ts == 2:
            self.maxi = self.cur.execute("""SELECT id FROM test2 ORDER BY id DESC""").fetchone()
            value = self.cur.execute(f'SELECT * FROM test2 WHERE id="{1}"').fetchall()
            self.con.clicked.connect(self.onClicked2)
            self.cont.clicked.connect(self.onClicked2)
            self.lineEdit.show()
            self.ui.anc_1.hide()
            self.ui.anc_2.hide()
            self.ui.anc_3.hide()
            self.ui.anc_4.hide()
            self.ui.a.hide()
            self.ui.b.hide()
            self.ui.c.hide()
            self.ui.d.hide()
            self.chet.setText(str(self.i))
            self.chet_3.setText(str(self.count))
            self.task.setText(value[0][1])
            self.timer.start(1000)
            self.time = ''
            self.ui.label_11.hide()
            self.ui.otv.hide()
        self.ui.prog.setMaximum(self.maxi[0])

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
        if self.ui.otv.currentText() == bd.Data.vopros(self, self.i, 1)[0][6]:
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
            self.resul = results(1)
            self.resul.show()
        if self.i <= int(self.maxi[0]):
            if self.i == self.maxi[0]:
                self.cont.hide()
                self.con.show()
            value = self.cur.execute(f'SELECT * FROM test1 WHERE id="{self.i}"').fetchall()
            self.ui.task.setText(value[0][1])
            self.ui.anc_1.setText(value[0][2])
            self.ui.anc_2.setText(value[0][3])
            self.ui.anc_3.setText(value[0][4])
            self.ui.anc_4.setText(value[0][5])
            self.ui.chet.setText(str(self.i))
            self.ui.chet_3.setText(str(self.count))

    def onClicked2(self):
        if self.i <= 25 and self.ui.lineEdit.text() == bd.Data.vopros(self, self.i, 2)[0][5]:
            self.count += 1
        if self.i > 25 and self.ui.otv.currentText() == bd.Data.vopros(self, self.i, 2)[0][5]:
            self.count += 1
        self.i += 1
        self.ui.prog.setValue(self.i)
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
            self.cur.execute(
                "INSERT INTO results2 (name, lvl, vopr, otv, time)" +
                f"VALUES ('{name}', '{self.lvl}', '{self.maxi[0]}', '{self.count}', '{self.time}')")
            self.con1.commit()
            self.resul = results(2)
            self.resul.show()
        if self.i <= int(self.maxi[0]):
            value = self.cur.execute(f'SELECT * FROM test2 WHERE id="{self.i}"').fetchall()
            if self.i == self.maxi[0]:
                self.cont.hide()
                self.con.show()
            if self.i <= 25:
                self.ui.task.setText(value[0][1])
                self.ui.chet.setText(str(self.i))
                self.ui.chet_3.setText(str(self.count))
                self.ui.lineEdit.setText("")
            else:
                self.ui.anc_1.show()
                self.ui.anc_2.show()
                self.ui.anc_3.show()
                self.ui.a.show()
                self.ui.b.show()
                self.ui.c.show()
                self.lineEdit.hide()
                self.ui.label_11.show()
                self.ui.otv_2.show()
                self.ui.task.setText(value[0][1])
                self.ui.anc_1.setText(value[0][2])
                self.ui.anc_2.setText(value[0][3])
                self.ui.anc_3.setText(value[0][4])
                self.ui.chet.setText(str(self.i))
                self.ui.chet_3.setText(str(self.count))


class results(QDialog):
    def __init__(self, ts):
        super().__init__()
        uic.loadUi('rezults.ui', self)
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
            elif cryptocode.decrypt(value[0][1], "wow") != self.ui.pas_inp.text():
                self.err_not_found_2.show()
                self.err_not_found.hide()
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
                    str_encoded = cryptocode.encrypt(self.pass1, "wow")
                    print(type(str_encoded), str_encoded)
                    cur.execute(f"INSERT INTO datem (name, pass, date)"
                                f"VALUES ('{self.login}', '{str_encoded}', '{self.dt}')")
                    fl = open('temp.txt', 'w')
                    fl.write(self.login)
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
                self.inp_pass.setText(cryptocode.decrypt(value[0][2], "wow"))
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
