import os, collections
from FileTypeSimpleCategorizer import FileTypeSimpleCategorizer

class FileTypeDocument(FileTypeSimpleCategorizer):
    @property 
    def type_id(self):
        return 'Documents'

    def __init__(self):
        extensions = [".txt", ".rtf", ".doc", ".xdoc", ".xls", ".pdf"]
        metadata = collections.OrderedDict()
        metadata['Category'] = ''
        metadata['Subcategory'] = ''
        metadata['Sub-subcategory'] = ''
        FileTypeSimpleCategorizer.__init__(self, extensions, metadata)
        
    def relative_path_from_metadata(self, metadata):
        categories = [metadata[key] for key in ['Category', 
                                                'Subcategory',
                                                'Sub-subcategory']
                      if metadata.has_key(key)]
        path_components = [category for category in categories if category != ""]
        if path_components == []:
            path_components = ['Unknown']
        return os.path.join(*path_components)
