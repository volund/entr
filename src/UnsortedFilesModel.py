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
        return 4

    def src_data(self, unsorted_file):
        fname = unsorted_file.absolute_src
        root = libentr.SortSettings().default_source()
        fname = fname.replace(root, "")
        return fname

    def type_data(self, unsorted_file):
        return unsorted_file.file_type.type_id

    def meta_preview_data(self, unsorted_file, column):
        meta = unsorted_file.metadata
        keys = meta.keys()
        if column >= len(keys):
            return QtCore.QVariant()
        key = keys[column]

        if meta[key] != '':
            return "{0}: {1}".format(key, meta[key])
        return QtCore.QVariant()
        
    def data(self, index, role): 
        if (not index.isValid()) or (role != QtCore.Qt.DisplayRole):
            return

        unsorted_file = self.unsorted_files[index.row()]
        col = index.column()
        if col == 0:
            return self.src_data(unsorted_file)
        elif col == 1:
            return self.type_data(unsorted_file)
        else:
            return self.meta_preview_data(unsorted_file, col - 2)
        
        return QtCore.QVariant()
    
    def headerData(self, col, orientation, role):
        if (orientation != QtCore.Qt.Horizontal) or (role != QtCore.Qt.DisplayRole):
            return QtCore.QVariant()
        
        return ["Filename", "Type", "Meta 1", "Meta 2"][col]
