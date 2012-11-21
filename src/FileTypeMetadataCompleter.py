from PyQt4 import QtCore, QtGui

class FileTypeMetadataCompleterModel(QtCore.QAbstractTableModel):
    def __init__(self, file_type, metadata, field, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.metadata = metadata
        self.field = field
        self.file_type = file_type
        
        self.rows = self.file_type.suggestions_for_meta_field(metadata, field)
    
    def rowCount(self, parent = QtCore.QModelIndex()):
        return len(self.rows)
    
    def columnCount(self, parent = QtCore.QModelIndex()):
        return 1
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not role in (QtCore.Qt.EditRole, QtCore.Qt.DisplayRole):
            return QtCore.QVariant()
        return self.rows[index.row()]

    def completionCount(self):
        return len(self.rows)

class FileTypeMetadataCompleter(QtGui.QCompleter):
    def __init__(self, file_type, metadata, field, parent=None):
        QtGui.QCompleter.__init__(self, parent)
        model = FileTypeMetadataCompleterModel(file_type, metadata, field)
        self.setModel(model)
