from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from instructions import *

class TestWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connects()
    self.show()
  
  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)

  def initUI(self):
#____________________________________________________________
    self.fio = QLabel(fio_txt)
    self.fio_area = QLineEdit()
#____________________________________________________________
    self.years = QLabel(years_txt) 
    self.years_area = QLineEdit()
#____________________________________________________________
    self.test_1 = QLabel(t1_txt) 
    self.baton_test_1 = QPushButton('Начать первый тест')
    self.test_1_area = QLineEdit()
#____________________________________________________________
    self.test_2 = QLabel(t2_txt)
    self.baton_test_2 = QPushButton('Начать второй тест')
    self.test_2_area = QLineEdit()
#____________________________________________________________
    self.test_3 = QLabel(t3_txt)
    self.baton_test_3 = QPushButton('Начать последний тест')
    self.test_3_area = QLineEdit()
#____________________________________________________________
    self.baton_test_4 = QPushButton('Результат')
    self.timer = QLabel('00:00:15')

#======================================================================@
    self.v_layout1 = QVBoxLayout()
    self.v_layout2 = QVBoxLayout()

#======================================================================@

    # ФАМИЛИЯ
    self.v_layout1.addWidget(self.fio)
    self.v_layout1.addWidget(self.fio_area)
    # ВОЗРАСТ
    self.v_layout1.addWidget(self.years)
    self.v_layout1.addWidget(self.years_area)
    # ТЕСТ НОМЕР 1
    self.v_layout1.addWidget(self.test_1)
    self.v_layout1.addWidget(self.baton_test_1)
    self.v_layout1.addWidget(self.test_1_area)
    # ТЕСТ НОМЕР 2
    self.v_layout1.addWidget(self.test_2)
    self.v_layout1.addWidget(self.baton_test_2)
    self.v_layout1.addWidget(self.test_2_area)
    # ТЕСТ НОМЕР 3
    self.v_layout1.addWidget(self.test_3)
    self.v_layout1.addWidget(self.baton_test_3)
    self.v_layout1.addWidget(self.test_3_area)
    # КНОПКА РЕЗУЛЬТАТА
    self.v_layout1.addWidget(self.baton_test_4)

#======================================================================@
    self.v_layout2.addWidget(self.timer)

#======================================================================@
    self.main_layout = QHBoxLayout()
    self.main_layout.addLayout(self.v_layout1)
    self.main_layout.addLayout(self.v_layout2)

#======================================================================@
    self.setLayout(self.main_layout)

  def connects(self):
    pass
