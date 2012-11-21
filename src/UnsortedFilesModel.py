import libentr
from PyQt4 import QtCore

class UnsortedFilesModel(QtCore.QAbstractTableModel): 
    def __init__(self, parent=None, *args): 
        self.unsorted_files = []
        QtCore.QAbstractListModel.__init__(self, parent, *args) 

    def unsorted_file_at_index(self, row):
        return self.unsorted_files[row]

    def remove_unsorted_files(self, start_index, end_index):
        print("Removing file at index: ", start_index, " ", end_index)
        current_length = len(self.unsorted_files)
        parent = self.index(current_length, 0)
        
        self.beginRemoveRows(parent, start_index, end_index)
        del self.unsorted_files[start_index:end_index]
        self.endRemoveRows()

    def append_unsorted_files(self, ufiles):
        current_length = len(self.unsorted_files)
        ufiles_length = len(ufiles)

        parent = self.index(current_length, 0)
        self.beginInsertRows(parent, current_length, current_length + ufiles_length)
        self.unsorted_files.extend(ufiles)
        self.endInsertRows()
        self.sort(1, QtCore.Qt.AscendingOrder)
    
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
            return QtCore.QVariant(u"{0}: {1}".format(key, meta[key]))
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

    def sort(self, col, order):
        reverse = (order == QtCore.Qt.DescendingOrder)
        self.layoutAboutToBeChanged.emit()

        sorters = [
            lambda x: x.absolute_src.lower(),
            lambda x: x.file_type.type_id.lower() + str(x.metadata),
            lambda x: x.file_type.type_id.lower() + str(self.meta_preview_data(x, 0)),
            lambda x: x.file_type.type_id.lower() + str(self.meta_preview_data(x, 1))
            ]
        self.unsorted_files.sort(key=sorters[col], reverse=reverse)
        self.layoutChanged.emit()
