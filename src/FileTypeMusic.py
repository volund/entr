from FileTypeSimpleCategorizer import FileTypeSimpleCategorizer
import os

class FileTypeMusic(FileTypeSimpleCategorizer):
    @property 
    def type_id(self):
        return 'Music'

    def __init__(self):
        extensions = [".mp3", ".ogg"]
        metadata = {'Artist':'', 'Album':''}
        FileTypeSimpleCategorizer.__init__(self, extensions, metadata)
        
    def relative_path_from_metadata(self, metadata, fname):
        categories = [metadata['Artist'], 
                      metadata['Album']]
        path_components = [category for category in categories if category != ""]
        if path_components == []:
            path_components = ['Unknown Artist', 'Unknown Album']
        path_components.append(fname)
        return os.path.join(*path_components)
        
