import os, sys
import libentr
import editor
from PyQt4 import QtCore,QtGui


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
        dialog_path = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
        fpath = libentr.utils.qstring_as_unicode(dialog_path)
        self.ingestFolder(fpath)

    def actionEdit(self):
        unsorted_files = self.selectedUnsortedFiles()
        if len(unsorted_files) == 0:
            return

        metadata = unsorted_files[0].file_type.metadata_template()
        common_metadata = libentr.MetadataUtils.common_metadata_from_unsorted_files(unsorted_files)
        
        dialog = editor.EditorDialog(metadata, common_metadata)
        dialog.metadataChanged.connect(self.metadataChanged)
        dialog.show()
        dialog.exec_()
        
    def actionSetType(self, new_ftype):
        selected = self.selectedIndicies()
        if len(selected) == 0:
            return
        
        unsorted_files = self.selectedUnsortedFiles()
        new_type =  self.file_type_manager.type_for_id(new_ftype)
        for unsorted_file in unsorted_files:
            unsorted_file.set_type(new_type)
            
        self.model.dataChanged.emit(selected[0], selected[-1])

    def actionSortSelected(self):
        unsorted_files = self.selectedUnsortedFiles()
        for unsorted_file in unsorted_files:
            self.sorter.sort_file(unsorted_file)

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

    def selectedUnsortedFiles(self):
        selected = self.selectedIndicies()
        unsorted_files = [self.model.unsorted_file_at_index(index.row()) for index in selected]
        return unsorted_files

    def selectedIndicies(self):
        selected = self.list_view.selectedIndexes()
        indicies = [index for index in selected if index.column() == 0]
        return indicies
