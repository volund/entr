import FileType
import os, logging

class FileTypeSimpleCategorizer(FileType.FileType):
    @property
    def type_id(self):
        return "SimpleCategorizor (%s)" % self.accepted_extensions

    def __init__(self, accepted_extensions, default_metadata):
        self.accepted_extensions = [ext.lower() for ext in accepted_extensions]
        self.default_metadata = default_metadata
        
    def can_handle_file(self, absolute_fname):
        fname, ext = os.path.splitext(absolute_fname)
        return ext.lower() in self.accepted_extensions

    def metadata_template(self):
        return self.default_metadata.copy()
    
    def suggestions_for_meta_field(self, metadata, field):
        return [].copy()

    def relative_path_from_metadata(self, metadata):
        return ""
