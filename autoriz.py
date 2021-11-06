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
            self.first_form = test(1)
            self.first_form.show()
            self.setVisible(False)
        elif self.sender().text() == "Тест level A1-А2":
            self.first_form = test(2)
            self.first_form.show()
            self.setVisible(False)
        elif self.sender().text() == "Тест level B1-B2":
            pass
        elif self.sender().text() == "Тест level C1-C2":
            pass


class test(QWidget):
    def __init__(self, ts):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.con1 = sqlite3.connect('users')
        self.cur = self.con1.cursor()
        self.i = 1
        self.count = 0
        self.maxi = self.cur.execute("""SELECT id FROM all_test ORDER BY id DESC""").fetchone()
        self.cont.clicked.connect(self.onClicked)
        self.con.clicked.connect(self.onClicked)
        self.con.hide()
        self.prog.setMaximum(self.maxi[0])
        self.prog.setValue(self.i)
        self.min = 0
        self.h = 0
        self.step = 0
        self.step_2 = 0
        self.min_2 = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_func)
        self.timer.start(1000)
        self.time = ''
        if ts == 1:
            value = self.cur.execute(f'SELECT * FROM all_test WHERE id="{self.i}"').fetchall()
            self.lineEdit.hide()
            self.task.setText(value[0][1])
            self.anc_1.setText(value[0][2])
            self.anc_2.setText(value[0][3])
            self.anc_3.setText(value[0][4])
            self.anc_4.setText(value[0][5])
            self.chet.setText(str(self.i))
            self.chet_3.setText(str(self.count))
            self.cont.clicked.connect(self.onClicked)
        elif ts == 2:
            value = self.cur.execute(f'SELECT * FROM test2 WHERE id="{self.i}"').fetchall()
            self.a.hide()
            self.b.hide()
            self.c.hide()
            self.d.hide()
            self.anc_1.hide()
            self.anc_2.hide()
            self.anc_3.hide()
            self.anc_4.hide()
            self.label_11.hide()
            self.otv.hide()
            self.task.setText(value[0][1])
            self.chet.setText(str(self.i))
            self.chet_3.setText(str(self.count))
            self.cont.clicked.connect(self.onClicked1)

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
        if self.otv.currentText() == bd.Data.vopros(self, self.i, 1)[0][6]:
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
            self.task.setText(value[0][1])
            self.anc_1.setText(value[0][2])
            self.anc_2.setText(value[0][3])
            self.anc_3.setText(value[0][4])
            self.anc_4.setText(value[0][5])
            self.chet.setText(str(self.i))
            self.chet_3.setText(str(self.count))

    def onClicked1(self):
        print(self.lineEdit.text(), bd.Data.vopros(self, self.i, 2)[0][5])
        if self.lineEdit.text() == bd.Data.vopros(self, self.i, 2)[0][5]:
            self.count += 1
        self.i += 1
        self.prog.setValue(self.i)
        if self.i <= int(self.maxi[0]):
            value = self.cur.execute(f'SELECT * FROM test2 WHERE id="{self.i}"').fetchall()
            self.task.setText(value[0][1])
            self.chet.setText(str(self.i))
            self.chet_3.setText(str(self.count))