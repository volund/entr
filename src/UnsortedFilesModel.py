from PyQt4 import QtCore

class UnsortedFilesModel(QtCore.QAbstractListModel): 
    def __init__(self, parent=None, *args): 
        self.unsorted_files = []
        QtCore.QAbstractListModel.__init__(self, parent, *args) 

    def append_unsorted_files(self, ufiles):
        current_length = len(self.unsorted_files)
        ufiles_length = len(ufiles)

        parent = self.index(current_length)
        self.beginInsertRows(parent, current_length, current_length + ufiles_length)
        self.unsorted_files.extend(ufiles)
        self.endInsertRows()
    
    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.unsorted_files) 
 
    def data(self, index, role): 
        if (not index.isValid()) or (role != QtCore.Qt.DisplayRole):
            return

        unsorted_file = self.unsorted_files[index.row()]
        return "{0} | {1}".format(unsorted_file.absolute_src, unsorted_file.file_type.type_id)
    
