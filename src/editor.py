import collections
from PyQt4 import QtCore, QtGui
from meta_editor_ui import Ui_metadata_editor_dlg
from MetadataTableModel import MetadataTableModel
from MetadataEditorItemDelegate import MetadataEditorItemDelegate


class EditorDialog(QtGui.QDialog):
    metadataChanged = QtCore.pyqtSignal([collections.OrderedDict])
    
    def __init__(self, metadata, common_metadata, metadata_file_type):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_metadata_editor_dlg()
        self.ui.setupUi(self)
        self.model = MetadataTableModel(metadata, common_metadata)
        self.metadata_file_type = metadata_file_type
        self.ui.metadata_table.setModel(self.model)
        self.ui.metadata_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.done_button.clicked.connect(self.doneButtonClicked)
        self.ui.cancel_button.clicked.connect(self.cancelButtonClicked)

        item_dlg = MetadataEditorItemDelegate(self.metadata_file_type,
                                              self.metadataRetriever(),
                                              self.currentFieldRetriever())
        self.ui.metadata_table.setItemDelegate(item_dlg)

    def doneButtonClicked(self):
        changed_meta = self.model.applicable_metadata()
        self.model.clear_metadata()
        self.metadataChanged.emit(changed_meta)
        QtGui.QDialog.reject(self)

    def cancelButtonClicked(self):
        self.model.clear_metadata()
        QtGui.QDialog.reject(self)

    def metadataRetriever(self):
        return lambda: self.model.metadata

    def currentFieldRetriever(self):
        return lambda field_index: "Random Field #{0}".format(field_index)
