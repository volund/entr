import collections
from PyQt4 import QtCore,QtGui
from meta_editor_ui import Ui_metadata_editor_dlg
from MetadataTableModel import MetadataTableModel

class EditorDialog(QtGui.QDialog):
    metadataChanged = QtCore.pyqtSignal([collections.OrderedDict])
    
    def __init__(self, metadata, common_metadata):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_metadata_editor_dlg()
        self.ui.setupUi(self)
        self.model = MetadataTableModel(metadata, common_metadata
)
        self.ui.metadata_table.setModel(self.model)
        self.ui.metadata_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.ui.done_button.clicked.connect(self.doneButtonClicked)
        self.ui.cancel_button.clicked.connect(self.cancelButtonClicked)

    def doneButtonClicked(self):
        changed_meta = self.model.applicable_metadata()
        self.model.clear_metadata()
        self.metadataChanged.emit(changed_meta)
        QtGui.QDialog.reject(self)

    def cancelButtonClicked(self):
        self.model.clear_metadata()
        QtGui.QDialog.reject(self)
