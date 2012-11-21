import FileType, SortSettings
import os, logging, glob

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
    
    def suggestions_for_meta_field(self, metadata, field_index):
        meta_template = self.metadata_template()

        fields = meta_template.keys()
        for i in range(field_index):
            if metadata[fields[i]] == '':
                return [][:]

        known_fields = [metadata[field] for field in fields[:field_index]]

        path = ""
        if len(known_fields) > 0:
            path = os.path.join(*known_fields)

        root = SortSettings.SortSettings().primary_destination_root()
        search_path = os.path.join(root, self.type_id, path)

        glob_path = os.path.join(search_path, '*')
        paths = [d for d in glob.glob(glob_path) if os.path.isdir(d)]
        return [os.path.basename(path) for path in paths]

    def relative_path_from_metadata(self, metadata):
        return ""

    
