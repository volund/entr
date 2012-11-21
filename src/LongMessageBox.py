from PyQt4.QtCore import *
from PyQt4.QtGui import *


class LongMessageBox(QDialog):
    def __init__(self, parent=None, text=""):
        QMainWindow.__init__(self, parent)
        self.create_main_frame(text)       

    def create_main_frame(self, text):        
        page = QWidget()        

        self.button = QPushButton('Ok', self)
        self.edit1 = QTextEdit()
        self.edit1.setHtml(text)
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.edit1)
        vbox1.addWidget(self.button)
        self.setLayout(vbox1)
        self.setGeometry(200, 200, 640, 240)
        self.connect(self.button, SIGNAL("clicked()"), self.clicked)

    def clicked(self):
        QDialog.reject(self)
