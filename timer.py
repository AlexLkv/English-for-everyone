from PyQt5.QtCore import QTimer


class timer:
    def __init__(self):
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
        return str(f"0{self.h}:{self.min_2}{self.min}:{self.step_2}{self.step}")
    def stop(self):
        self.timer.stop()
        return self.timer
