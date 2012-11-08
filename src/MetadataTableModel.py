from PyQt4 import QtCore
import collections, libentr

class MetadataTableModel(QtCore.QAbstractTableModel): 
    def __init__(self, metadata={}, common_metadata={}, parent=None, *args): 
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.keys = metadata.keys()
        self.metadata = metadata.copy()
        self.enabled_fields = {key:False for key in metadata}
        for key in common_metadata:
            self.enabled_fields[key] = True
            self.metadata[key] = common_metadata[key]

        QtCore.QAbstractListModel.__init__(self, parent, *args) 

    def clear_metadata(self):
        for key in self.metadata:
            self.metadata[key] = ''
        for key in self.enabled_fields:
            self.enabled_fields[key] = False
        
    def metadata_field_at_index(self, row):
        return self.keys[row]

    def metadata_value_at_index(self, row):
        return self.metadata[self.keys[row]]
    
    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self.metadata)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 2
    
    def data(self, index, role): 
        if (not index.isValid()):
            return QtCore.QVariant()

        key = self.keys[index.row()]
        if (role == QtCore.Qt.CheckStateRole) and (index.column() == 0):
            return self.enabled_fields[key]

        if (role != QtCore.Qt.DisplayRole):
            return QtCore.QVariant()

        if index.column() == 0:
            return key
        else:
            return self.metadata[key]

        return QtCore.QVariant()

    def setCheckStateData(self, index, data):
        key = self.keys[index.row()]
        self.enabled_fields[key] = not self.enabled_fields[key]
        
        self.dataChanged.emit(index, index)
        return True

    def setEditData(self, index, data):
        key = self.keys[index.row()]
        udata = libentr.utils.qstring_as_unicode(data.toString())
        self.metadata[key] = udata
        self.enabled_fields[key] = True
        self.dataChanged.emit(index, index)
        return True


    def setData(self, index, data, role):
        if role == QtCore.Qt.CheckStateRole:
            return self.setCheckStateData(index, data)
        if role == QtCore.Qt.EditRole:
            return self.setEditData(index, data)
        return False
    
    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return ["Key", "Value"][col]
        return QtCore.QVariant()

    def flags(self, index):
        if (index.column() == 0):
            return QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled 
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable

    def applicable_metadata(self):
        meta = collections.OrderedDict()
        for key in self.enabled_fields:
            if self.enabled_fields[key]:
                meta[key] = self.metadata[key]
        return meta
