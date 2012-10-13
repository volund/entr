import FileType
import os

class FileTypeSimpleCategorizer(FileType.FileType):
    @property
    def type_id(self):
        return "SimpleCategorizor (%s)" % self.accepted_extensions

    def __init__(self, accepted_extensions, default_metadata):
        self.accepted_extensions = [ext.lower for ext in extaccepted_extensions]
        self.default_metadata = default_metadata
        
    def can_handle_file(absolute_fname):
        fname, ext = os.path.splitext(absolute_fname)
        return ext.lower() in self.accepted_extensions

    def metadata_for_file(absolute_fname):
        return self.default_metadata

    def suggestions_for_meta_field(metadata, field):
        return []

    def relative_path_from_metadata(metadata, fname):
        return fname
