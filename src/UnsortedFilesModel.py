import libentr
from PyQt4 import QtCore

class UnsortedFilesModel(QtCore.QAbstractTableModel): 
    def __init__(self, parent=None, *args): 
        self.unsorted_files = []
        QtCore.QAbstractListModel.__init__(self, parent, *args) 

    def unsorted_file_at_index(self, row):
        return self.unsorted_files[row]
    
    def append_unsorted_files(self, ufiles):
        current_length = len(self.unsorted_files)
        ufiles_length = len(ufiles)

        parent = self.index(current_length, 0)
        self.beginInsertRows(parent, current_length, current_length + ufiles_length)
        self.unsorted_files.extend(ufiles)
        self.endInsertRows()
    
    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.unsorted_files) 

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 2
    
    def data(self, index, role): 
        if (not index.isValid()) or (role != QtCore.Qt.DisplayRole):
            return

        unsorted_file = self.unsorted_files[index.row()]
        if index.column() == 0:
            fname = unsorted_file.absolute_src
            root = libentr.SortSettings().default_source()
            fname = fname.replace(root, "")
            return fname
        else:
            return unsorted_file.file_type.type_id
        return QtCore.QVariant()
    
    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return ["Filename", "Type"][col]
        return QtCore.QVariant()
