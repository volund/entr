import os, sys
import libentr
import editor
from PyQt4 import QtCore,QtGui
import LongMessageBox

class UnsortedFilesDelegate:
    def __init__(self, model, list_view):
        self.model = model
        self.list_view = list_view
        
        self.ingestor = libentr.UnsortedFileIngestor()
        self.sorter = libentr.UnsortedFileSorter()
        self.sort_settings = libentr.SortSettings()
        self.file_type_manager = libentr.FileTypeManager()
        self.file_type_manager.register_default_types()

    def mainWindowInitialized(self):
        self.ingestFolder(self.sort_settings.default_source())

# Actions
    def actionFileAdd(self):
        dialog_path = QtGui.QFileDialog.getExistingDirectory(self.list_view, "Select Directory")
        fpath = libentr.utils.qstring_as_unicode(dialog_path)
        self.ingestFolder(fpath)

    def actionEdit(self):
        unsorted_files = self.selectedUnsortedFiles()
        if len(unsorted_files) == 0:
            return

        first_file = unsorted_files[0]
        metadata = first_file.file_type.metadata_template()
        common_metadata = libentr.MetadataUtils.common_metadata_from_unsorted_files(unsorted_files)
        
        dialog = editor.EditorDialog(metadata, common_metadata, first_file.file_type)
        dialog.metadataChanged.connect(self.metadataChanged)
        dialog.show()
        dialog.exec_()
        
    def actionSetType(self, new_ftype):
        selected = self.selectedIndicies(1)
        if len(selected) == 0:
            return
        
        unsorted_files = self.selectedUnsortedFiles()
        new_type =  self.file_type_manager.type_for_id(new_ftype)
        for unsorted_file in unsorted_files:
            unsorted_file.set_type(new_type)
            
        self.model.dataChanged.emit(selected[0], selected[-1])

    def actionSortSelected(self):
        unsorted_files = self.selectedUnsortedFiles()
        indices = [index.row() for index in self.selectedIndicies()]
        indices.sort()
        indices.reverse()
        print(indices)

        failed = []
        for index, unsorted_file in zip(indices, unsorted_files):
            try:
                self.sorter.sort_file(unsorted_file)
                self.model.remove_unsorted_files(index, index + 1)
            except:
                err_type, val = sys.exc_info()[:2]
                failed.append((unsorted_file, err_type, str(val)))

        if (len(failed) > 0):
            self.show_failed_dialog_message(failed)


    def rowDoubleClicked(self, index):
        self.actionEdit()
        
# Events
    def metadataChanged(self, new_meta):
        unsorted_files = self.selectedUnsortedFiles()
        indicies = self.selectedIndicies()
        if (len(unsorted_files) == 0):
            return
        
        libentr.MetadataUtils.apply_metadata_dictionary(new_meta, unsorted_files)
        model = self.list_view.model()
        model.dataChanged.emit(indicies[0], indicies[-1])

# Aux
    def ingestFolder(self, fpath):
        unsorted_files = self.ingestor.ingest_directory(fpath)
        self.model.append_unsorted_files(unsorted_files)
        self.list_view.resizeEvent(None)

    def selectedUnsortedFiles(self):
        selected = self.selectedIndicies()
        unsorted_files = [self.model.unsorted_file_at_index(index.row()) for index in selected]
        return unsorted_files

    def selectedIndicies(self, column = 0):
        selected = self.list_view.selectedIndexes()
        indicies = [index for index in selected if index.column() == column]
        return indicies

    def show_failed_dialog_message(self, failed):
        failures = [(fail[0].absolute_src, str(fail[2])) for fail in failed]
        msgs = u"<br/><br/>".join([u"<b>{0}</b>: {1}".format(fname, err) for (fname, err) in failures])
        msg = u"Could not move the following files: <br/><br/>{0}".format(msgs)
        msgbox = LongMessageBox.LongMessageBox(self.list_view, msg)
        msgbox.show()

