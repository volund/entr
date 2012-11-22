import os, collections
from FileTypeSimpleCategorizer import FileTypeSimpleCategorizer


class FileTypeEbook(FileTypeSimpleCategorizer):
    @property 
    def type_id(self):
        return 'Ebooks'

    def __init__(self):
        extensions = [".mobi", ".epub"]
        metadata = collections.OrderedDict()
        metadata['Author'] = ''
        metadata['Series'] = ''
        FileTypeSimpleCategorizer.__init__(self, extensions, metadata)
        
    def relative_path_from_metadata(self, metadata):
        categories = [metadata['Author'], 
                      metadata['Series']]
        path_components = [category for category in categories if category != ""]
        if path_components == []:
            path_components = ['Unknown']
        return os.path.join(*path_components)
        
