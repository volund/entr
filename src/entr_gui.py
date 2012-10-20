import os, sys
import libentr
from PyQt4 import QtCore,QtGui
from window_ui import Ui_MainWindow
from UnsortedFilesModel import *

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.model = UnsortedFilesModel(self)
        self.ui.unsorted_files_view.setModel(self.model)

        self.ui.actionAdd.triggered.connect(self.actionFileAdd)

        self.ingestor = libentr.UnsortedFileIngestor()
        

    def actionFileAdd(self):
        fpath = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        unsorted_files = self.ingestor.ingest_directory(fpath)
        self.model.append_unsorted_files(unsorted_files)

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
