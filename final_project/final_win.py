from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
from instructions import *



class FinalWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.show()
  
  def set_appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)

  def initUI(self):
    self.one_text = QLabel(txt_one)
    self.two_text = QLabel(txt_two)


    self.layout = QVBoxLayout()

    self.layout.addWidget(self.one_text, alignment=Qt.AlignCenter)
    self.layout.addWidget(self.two_text, alignment=Qt.AlignCenter)
    
    self.setLayout(self.layout)
