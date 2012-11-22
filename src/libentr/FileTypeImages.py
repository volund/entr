import os, collections
from FileTypeSimpleCategorizer import FileTypeSimpleCategorizer


class FileTypeImages(FileTypeSimpleCategorizer):
    @property 
    def type_id(self):
        return 'Images'

    def __init__(self):
        extensions = [".jpg", ".png", ".tiff", ".bmp", ".xcf", ".jpeg"]
        metadata = collections.OrderedDict()
        metadata['Album'] = ''
        metadata['Sous-album'] = ''
        FileTypeSimpleCategorizer.__init__(self, extensions, metadata)
        
    def relative_path_from_metadata(self, metadata):
        categories = [metadata['Album'], 
                      metadata['Sous-album']]
        path_components = [category for category in categories if category != ""]
        if path_components == []:
            path_components = ['Unknown']
        return os.path.join(*path_components)
        
