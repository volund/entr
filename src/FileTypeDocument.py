from FileTypeSimpleCategorizer import FileTypeSimpleCategorizer
import os

class FileTypeDocument(FileTypeSimpleCategorizer):
    @property 
    def type_id(self):
        return 'Document'

    def __init__(self):
        extensions = [".txt", ".rtf", ".doc", ".xdoc", ".xls"]
        metadata = {'Category':'', 'Subcategory':'', 'Sub-subcategory':''}
        FileTypeSimpleCategorizer.__init__(self, extensions, metadata)
        
    def relative_path_from_metadata(self, metadata, fname):
        categories = [metadata['Category'], 
                      metadata['Subcategory'],
                      metadata['Sub-subcategory']]
        path_components = [category for category in categories if category != ""]
        if path_components == []:
            path_components = ['Unknown']
        path_components.append(fname)
        return os.join(path_components)
