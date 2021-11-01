import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

from front import Ui_MainWindow
from tests import Ui_Dialog


# ГЛАВНОЕ МЕНЮ
# SETENABLE() - БЛОК КНОПКИ
class Menu1(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Menu1, self).__init__()
        uic.loadUi('front.ui', self)
        self.btn_testing.clicked.connect(self.onClicked)
        self.btn_autoriz.clicked.connect(self.onClicked)
        self.btn_reyt.clicked.connect(self.onClicked)

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
class tests(QDialog, Ui_Dialog):
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
        self.i = 1
        self.count = 0
        self.ui = uic.loadUi('untitled.ui', self)
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        con = sqlite3.connect('users')
        cur = con.cursor()
        value = cur.execute(f'SELECT * FROM all_test WHERE id="{self.i}"').fetchall()
        if self.ui.otv.currentText() == value[0][6]:
            self.count += 1
        self.i += 1
        if self.i != 1:
            value = cur.execute(f'SELECT * FROM all_test WHERE id="{self.i}"').fetchall()
            self.ui.task.setText(value[0][1])
            self.ui.anc_1.setText(value[0][2])
            self.ui.anc_2.setText(value[0][3])
            self.ui.anc_3.setText(value[0][4])
            self.ui.anc_4.setText(value[0][5])
            self.ui.chet.setText(str(self.i))
            self.ui.chet_3.setText(str(self.count))
            print(self.i, self.count)


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
        elif self.sender().text() == "Зарегестрироваться":
            self.second_form = login1()
            self.second_form.show()
            self.setVisible(False)
        elif self.sender().text() == "Востановление аккаунта":
            self.third_form = get_pass()
            self.third_form.show()
            self.setVisible(False)

    def fx(self):
        self.setVisible(True)


# ВХОД В СИСТЕМУ
class vxod(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('autoriz.ui', self)
        self.back.clicked.connect(self.onClicked)
        self.cont.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.sender().text() == "<-- Назад":
            self.close()

        elif self.sender().text() == "Готово!":
            self.close()


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
                while True:
                    if value is None:
                        self.ui.err_name.show()
                        continue
                    elif self.pass1 != self.pass2:
                        self.ui.err_name_2.show()
                        continue
                    else:
                        con = sqlite3.connect('users')
                        cur = con.cursor()
                        print(self.dt, self.login, self.pass1)
                        cur.execute(f"INSERT INTO datem (name, pass, date)"
                                    f"VALUES ('{self.login}', '{self.pass1}', '{self.dt}')")
                        self.close()
                        con.commit()
                        cur.close()
                        break


# ВОССТАНОВЛЕНИЕ ПАРОЛЯ
class get_pass(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('getpass.ui', self)
        self.back.clicked.connect(self.onClicked)
        self.cont_2.clicked.connect(self.onClicked)

    def onClicked(self):
        if self.sender().text() == "<-- Назад":
            self.close()


class reyting(QWidget):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu1()
    ex.show()
    sys.exit(app.exec_())
