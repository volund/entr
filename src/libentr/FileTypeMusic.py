import os, collections
from FileTypeSimpleCategorizer import FileTypeSimpleCategorizer


class FileTypeMusic(FileTypeSimpleCategorizer):
    @property 
    def type_id(self):
        return 'Music'

    def __init__(self):
        extensions = [".mp3", ".ogg"]
        metadata = collections.OrderedDict()
        metadata['Artist'] = ''
        metadata['Album'] = ''
        FileTypeSimpleCategorizer.__init__(self, extensions, metadata)
        
    def relative_path_from_metadata(self, metadata):
        categories = [metadata['Artist'], 
                      metadata['Album']]
        path_components = [category for category in categories if category != ""]
        if path_components == []:
            path_components = ['Unknown Artist', 'Unknown Album']
        return os.path.join(*path_components)
        
