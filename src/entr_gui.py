import os, sys
import libentr
from PyQt4 import QtCore,QtGui
from window_ui import Ui_MainWindow
from UnsortedFilesModel import *
from UnsortedFilesDelegate import UnsortedFilesDelegate

class ScopeCapturer(object):
    def __init__(self, method, message):
        self.method = method
        self.message = message

    def __call__(self):
        return self.method(self.message)


class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.createUI()
        self.createAndConnectModel()
        self.createAndConnectDelegate()
        self.populateSetTypeMenu()
        
        self.delegate.mainWindowInitialized()
        self.raise_()

    def createUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.unsorted_files_view.horizontalHeader().setResizeMode(QtGui.QHeaderView.Custom)
        self.ui.unsorted_files_view.setSortingEnabled(True)
        self.ui.unsorted_files_view.sortByColumn(1, QtCore.Qt.AscendingOrder)

    def createAndConnectModel(self):
        self.model = UnsortedFilesModel(self)
        self.ui.unsorted_files_view.setModel(self.model)

    def createAndConnectDelegate(self):
        self.delegate = UnsortedFilesDelegate(self.model, self.ui.unsorted_files_view)
        self.ui.actionAdd.triggered.connect(self.delegate.actionFileAdd)
        self.ui.actionEdit.triggered.connect(self.delegate.actionEdit)
        self.ui.actionSortSelected.triggered.connect(self.delegate.actionSortSelected)
        self.ui.unsorted_files_view.doubleClicked.connect(self.delegate.rowDoubleClicked)
        
    def populateSetTypeMenu(self):
        file_type_manager = libentr.FileTypeManager()
        file_type_manager.register_default_types()
        for ftype in file_type_manager.list_of_types():
            set_type_action = self.ui.menuSet_Type.addAction(ftype)
            set_type_action.triggered.connect(ScopeCapturer(self.delegate.actionSetType, ftype))

    def resizeEvent(self, resizeEvent):
        self.ui.unsorted_files_view.setColumnWidth(0,500)
        self.ui.unsorted_files_view.setColumnWidth(1,400)
        self.ui.unsorted_files_view.setColumnWidth(2,250)
        self.ui.unsorted_files_view.setColumnWidth(3,250)
        self.ui.unsorted_files_view.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Interactive)
        self.ui.unsorted_files_view.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Interactive)
        self.ui.unsorted_files_view.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Interactive)
        self.ui.unsorted_files_view.horizontalHeader().setResizeMode(3, QtGui.QHeaderView.Interactive)


def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
