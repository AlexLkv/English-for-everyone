import sqlite3
from PyQt5.QtWidgets import QApplication,  QWidget
from all_reyting import Ui_Reyt

class reyting(QWidget, Ui_Reyt):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect('users')
        cur = con.cursor()
        ts1 = cur.execute("""SELECT name, time, lvl, otv FROM results ORDER BY otv DESC, time ASC""").fetchmany(5)
        ts2 = cur.execute("""SELECT name, time, lvl, otv FROM results2 ORDER BY otv DESC, time ASC""").fetchmany(5)
        ts3 = cur.execute("""SELECT name, time, lvl, otv FROM results3 ORDER BY otv DESC, time ASC""").fetchmany(5)
        ts4 = cur.execute("""SELECT name, time, lvl, otv FROM results4 ORDER BY otv DESC, time ASC""").fetchmany(5)

        # ОТРИСОВКА ТАБЛИЦЫ РЕЗУЛЬТАТОВ
        if len(ts1) >= 1:
            self.name_11.setText(str(ts1[0][0]))
            self.time_11.setText(str(ts1[0][1]))
            self.lvl_11.setText(str(ts1[0][2]))
            self.otv_11.setText(str(ts1[0][3]))
        else:
            self.name_12.setText("-")
            self.time_12.setText("-")
            self.lvl_12.setText("-")
            self.otv_12.setText("-")
        if len(ts1) >= 2:
            self.name_12.setText(str(ts1[1][0]))
            self.time_12.setText(str(ts1[1][1]))
            self.lvl_12.setText(str(ts1[1][2]))
            self.otv_12.setText(str(ts1[1][3]))

        else:
            self.name_12.setText("-")
            self.time_12.setText("-")
            self.lvl_12.setText("-")
            self.otv_12.setText("-")

        if len(ts1) >= 3:
            self.name_13.setText(str(ts1[2][0]))
            self.time_13.setText(str(ts1[2][1]))
            self.lvl_13.setText(str(ts1[2][2]))
            self.otv_13.setText(str(ts1[2][3]))
        else:
            self.name_13.setText("-")
            self.time_13.setText("-")
            self.lvl_13.setText("-")
            self.otv_13.setText("-")
        if len(ts1) >= 4:
            self.name_14.setText(str(ts1[3][0]))
            self.time_14.setText(str(ts1[3][1]))
            self.lvl_14.setText(str(ts1[3][2]))
            self.otv_14.setText(str(ts1[3][3]))
        else:
            self.name_14.setText("-")
            self.time_14.setText("-")
            self.lvl_14.setText("-")
            self.otv_14.setText("-")
        if len(ts1) >= 5:
            self.name_15.setText(str(ts1[4][0]))
            self.time_15.setText(str(ts1[4][1]))
            self.lvl_15.setText(str(ts1[4][2]))
            self.otv_15.setText(str(ts1[4][3]))
        else:
            self.name_15.setText("-")
            self.time_15.setText("-")
            self.lvl_15.setText("-")
            self.otv_15.setText("-")

        # ОТРИСОВКА ТАБЛИЦЫ РЕЗУЛЬТАТОВ 2
        if len(ts2) >= 1:
            self.name_21.setText(str(ts2[0][0]))
            self.time_21.setText(str(ts2[0][1]))
            self.lvl_21.setText(str(ts2[0][2]))
            self.otv_21.setText(str(ts2[0][3]))
        else:
            self.name_21.setText("-")
            self.time_21.setText("-")
            self.lvl_21.setText("-")
            self.otv_21.setText("-")
        if len(ts2) >= 2:
            self.name_22.setText(str(ts2[1][0]))
            self.time_22.setText(str(ts2[1][1]))
            self.lvl_22.setText(str(ts2[1][2]))
            self.otv_22.setText(str(ts2[1][3]))
        else:
            self.name_22.setText("-")
            self.time_22.setText("-")
            self.lvl_22.setText("-")
            self.otv_22.setText("-")
        if len(ts2) >= 3:
            self.name_23.setText(str(ts2[2][0]))
            self.time_23.setText(str(ts2[2][1]))
            self.lvl_23.setText(str(ts2[2][2]))
            self.otv_23.setText(str(ts2[2][3]))
        else:
            self.name_23.setText("-")
            self.time_23.setText("-")
            self.lvl_23.setText("-")
            self.otv_23.setText("-")
        if len(ts2) >= 4:
            self.name_24.setText(str(ts2[3][0]))
            self.time_24.setText(str(ts2[3][1]))
            self.lvl_24.setText(str(ts2[3][2]))
            self.otv_24.setText(str(ts2[3][3]))
        else:
            self.name_24.setText("-")
            self.time_24.setText("-")
            self.lvl_24.setText("-")
            self.otv_24.setText("-")
        if len(ts2) >= 5:
            self.name_25.setText(str(ts2[4][0]))
            self.time_25.setText(str(ts2[4][1]))
            self.lvl_25.setText(str(ts2[4][2]))
            self.otv_25.setText(str(ts2[4][3]))
        else:
            self.name_25.setText("-")
            self.time_25.setText("-")
            self.lvl_25.setText("-")
            self.otv_25.setText("-")
        # ОТРИСОВКА ТАБЛИЦЫ РЕЗУЛЬТАТОВ 3
        if len(ts3) >= 1:
            self.name_31.setText(str(ts3[0][0]))
            self.time_31.setText(str(ts3[0][1]))
            self.lvl_31.setText(str(ts3[0][2]))
            self.otv_31.setText(str(ts3[0][3]))
        else:
            self.name_31.setText("-")
            self.time_31.setText("-")
            self.lvl_31.setText("-")
            self.otv_31.setText("-")
        if len(ts3) >= 2:
            self.name_32.setText(str(ts3[1][0]))
            self.time_32.setText(str(ts3[1][1]))
            self.lvl_32.setText(str(ts3[1][2]))
            self.otv_32.setText(str(ts3[1][3]))
        else:
            self.name_32.setText("-")
            self.time_32.setText("-")
            self.lvl_32.setText("-")
            self.otv_32.setText("-")
        if len(ts3) >= 3:
            self.name_33.setText(str(ts3[2][0]))
            self.time_33.setText(str(ts3[2][1]))
            self.lvl_33.setText(str(ts3[2][2]))
            self.otv_33.setText(str(ts3[2][3]))
        else:
            self.name_33.setText("-")
            self.time_33.setText("-")
            self.lvl_33.setText("-")
            self.otv_33.setText("-")
        if len(ts3) >= 4:
            self.name_34.setText(str(ts3[3][0]))
            self.time_34.setText(str(ts3[3][1]))
            self.lvl_34.setText(str(ts3[3][2]))
            self.otv_34.setText(str(ts3[3][3]))
        else:
            self.name_34.setText("-")
            self.time_34.setText("-")
            self.lvl_34.setText("-")
            self.otv_34.setText("-")
        if len(ts3) >= 5:
            self.name_35.setText(str(ts3[4][0]))
            self.time_35.setText(str(ts3[4][1]))
            self.lvl_35.setText(str(ts3[4][2]))
            self.otv_35.setText(str(ts3[4][3]))
        else:
            self.name_35.setText("-")
            self.time_35.setText("-")
            self.lvl_35.setText("-")
            self.otv_35.setText("-")
# ОТРИСОВКА ТАБЛИЦЫ РЕЗУЛЬТАТОВ
        if len(ts4) >= 1:
            self.name_41.setText(str(ts4[0][0]))
            self.time_41.setText(str(ts4[0][1]))
            self.lvl_41.setText(str(ts4[0][2]))
            self.otv_41.setText(str(ts4[0][3]))
        else:
            self.name_41.setText("-")
            self.time_41.setText("-")
            self.lvl_41.setText("-")
            self.otv_41.setText("-")
        if len(ts4) >= 2:
            self.name_42.setText(str(ts4[1][0]))
            self.time_42.setText(str(ts4[1][1]))
            self.lvl_42.setText(str(ts4[1][2]))
            self.otv_42.setText(str(ts4[1][3]))

        else:
            self.name_42.setText("-")
            self.time_42.setText("-")
            self.lvl_42.setText("-")
            self.otv_42.setText("-")

        if len(ts4) >= 3:
            self.name_43.setText(str(ts4[2][0]))
            self.time_43.setText(str(ts4[2][1]))
            self.lvl_43.setText(str(ts4[2][2]))
            self.otv_43.setText(str(ts4[2][3]))
        else:
            self.name_43.setText("-")
            self.time_43.setText("-")
            self.lvl_43.setText("-")
            self.otv_43.setText("-")
        if len(ts4) >= 4:
            self.name_44.setText(str(ts4[3][0]))
            self.time_44.setText(str(ts4[3][1]))
            self.lvl_44.setText(str(ts4[3][2]))
            self.otv_44.setText(str(ts4[3][3]))
        else:
            self.name_44.setText("-")
            self.time_44.setText("-")
            self.lvl_44.setText("-")
            self.otv_44.setText("-")
        if len(ts4) >= 5:
            self.name_45.setText(str(ts4[4][0]))
            self.time_45.setText(str(ts4[4][1]))
            self.lvl_45.setText(str(ts4[4][2]))
            self.otv_45.setText(str(ts4[4][3]))
        else:
            self.name_45.setText("-")
            self.time_45.setText("-")
            self.lvl_45.setText("-")
            self.otv_45.setText("-")
