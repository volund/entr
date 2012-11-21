from FileTypeMetadataCompleter import *

class MetadataEditorItemDelegate(QtGui.QItemDelegate):
    def __init__(self, metadata_file_type, metadata_retriever, field_retriever):
        QtGui.QItemDelegate.__init__(self)
        self.file_type = metadata_file_type
        self.metadata_retriever = metadata_retriever
        self.field_retriever = field_retriever
        
    def createEditor(self, parent, option, index):
        editor = QtGui.QItemDelegate.createEditor(self, parent, option, index)        
        
        metadata = self.metadata_retriever()
        field = index.row()
        
        completer = FileTypeMetadataCompleter(self.file_type, metadata, field)
        completer.setCaseSensitivity(False)
        #completer.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
        editor.setCompleter(completer)        

        return editor
