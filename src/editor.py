import collections
from PyQt4 import QtCore, QtGui
from meta_editor_ui import Ui_metadata_editor_dlg
from MetadataTableModel import MetadataTableModel




class MyCompletionModel(QtCore.QAbstractTableModel):
    #dummy instead of database data
    def __init__(self, parent=None):
        #super(MyCompletionModel, self).__init__(parent)
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.rows = [(1,"Abraham","Alfred"), (2,"Bull","Bill"), (3,"Cesar", "Charles")]
    
    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.rows)
    
    def columnCount(self, parent = QtCore.QModelIndex()):
        return len(self.rows[0])
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        return self.rows[index.row()][1]

    def completionCount(self):
        return len(self.rows)
    
class MyCompleter(QtGui.QCompleter):
    def __init__(self, parent=None):
        #super(MyCompleter, self).__init__(parent)
        #model = MyCompletionModel()
        model = QtGui.QStringListModel(["Artist 1", "Artist 2", "Artist 3", "Artist 4", "Artist 5"])
        QtGui.QCompleter.__init__(self, parent)
        self.setModel(model)
        #self.setCompletionColumn(1)


#class CustomItemDelegate(QtGui.QAbstractItemDelegate):
class CustomItemDelegate(QtGui.QItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtGui.QItemDelegate.createEditor(self, parent, option, index)
        
        completer = MyCompleter()
        completer.setCaseSensitivity(False)
        editor.setCompleter(completer)
        
        return editor
        
class EditorDialog(QtGui.QDialog):
    metadataChanged = QtCore.pyqtSignal([collections.OrderedDict])
    
    def __init__(self, metadata, common_metadata):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_metadata_editor_dlg()
        self.ui.setupUi(self)
        self.model = MetadataTableModel(metadata, common_metadata)
        self.ui.metadata_table.setModel(self.model)
        self.ui.metadata_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.done_button.clicked.connect(self.doneButtonClicked)
        self.ui.cancel_button.clicked.connect(self.cancelButtonClicked)

        custom_item_dlg = CustomItemDelegate()
        self.ui.metadata_table.setItemDelegate(custom_item_dlg)

    def doneButtonClicked(self):
        changed_meta = self.model.applicable_metadata()
        self.model.clear_metadata()
        self.metadataChanged.emit(changed_meta)
        QtGui.QDialog.reject(self)

    def cancelButtonClicked(self):
        self.model.clear_metadata()
        QtGui.QDialog.reject(self)
