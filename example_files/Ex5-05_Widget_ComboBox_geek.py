# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # creating a combo box widget
        self.combo_box = QComboBox(self)
  
        # setting geometry of combo box
        self.combo_box.setGeometry(200, 150, 120, 30)
  
        # geek list
        a = ['동', '호', '동호명', '필수사용\n공제', '할인\n구분', '복지할인', '절전할인', '자동이체\n/인터넷']
        a.sort()
        geek_list = a
  
        # adding list of items to combo box
        self.combo_box.addItems(geek_list)
  
        # setting current index
        self.combo_box.setCurrentIndex(2)
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())