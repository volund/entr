import os, sys
import libentr
from PyQt4 import QtCore,QtGui
from window_ui import Ui_MainWindow
import editor
from UnsortedFilesModel import *

class ScopeCapturer(object):
    def __init__(self, method, message):
        self.method = method
        self.message = message

    def __call__(self):
        return self.method(self.message)


class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(100, 100, 800, 600)
        self.model = UnsortedFilesModel(self)
        self.ui.unsorted_files_view.setModel(self.model)

        self.ui.actionAdd.triggered.connect(self.actionFileAdd)
        self.ui.actionEdit.triggered.connect(self.actionEdit)
        
        self.ingestor = libentr.UnsortedFileIngestor()
        self.sort_settings = libentr.SortSettings()
        self.ui.unsorted_files_view.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        
        self.file_type_manager = libentr.FileTypeManager()
        self.file_type_manager.register_default_types()
        
        for ftype in self.file_type_manager.list_of_types():
            set_type_action = self.ui.menuSet_Type.addAction(ftype)
            set_type_action.triggered.connect(ScopeCapturer(self.actionSetType, ftype))

        self.ingestFolder(self.sort_settings.default_source())

    def actionFileAdd(self):
        dialog_path = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
        fpath = libentr.utils.qstring_as_unicode(dialog_path)
        self.ingestFolder(fpath)

    def actionEdit(self):
        selected = self.ui.unsorted_files_view.selectedIndexes()
        if (len(selected) == 0):
            return
        
        model = self.ui.unsorted_files_view.model()
        unsorted_files = [model.unsorted_file_at_index(index.row()) for index in selected]
        
        metadata = unsorted_files[0].file_type.metadata_template()
        common_metadata = libentr.MetadataUtils.common_metadata_from_unsorted_files(unsorted_files)
        
        dialog = editor.EditorDialog(metadata, common_metadata)
        dialog.metadataChanged.connect(self.metadataChanged)
        dialog.show()
        dialog.exec_()
        
    def actionSetType(self, new_ftype):
        selected = self.ui.unsorted_files_view.selectedIndexes()
        if len(selected) == 0:
            return
        
        model = self.ui.unsorted_files_view.model()
        for index in selected:
            unsorted_file = model.unsorted_file_at_index(index.row())
            new_type =  self.file_type_manager.type_for_id(new_ftype)
            unsorted_file.set_type(new_type)
            
        model.dataChanged.emit(selected[0], selected[-1])

    def metadataChanged(self, new_meta):
        selected = self.ui.unsorted_files_view.selectedIndexes()
        if len(selected) == 0:
            return
        
        model = self.ui.unsorted_files_view.model()
        unsorted_files = [model.unsorted_file_at_index(index.row()) for index in selected]
        libentr.MetadataUtils.apply_metadata_dictionary(new_meta, unsorted_files)
        model.dataChanged.emit(selected[0], selected[-1])
        
    def ingestFolder(self, fpath):
        unsorted_files = self.ingestor.ingest_directory(fpath)
        self.model.append_unsorted_files(unsorted_files)

def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
