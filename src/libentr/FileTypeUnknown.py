import FileType

class FileTypeUnknown(FileType.FileType):
    @property
    def type_id(self):
        return 'Unknown'

    def can_handle_file(self, absolute_fname):
        return True

    def suggestions_for_meta_field(self, metadata, field):
        return [].copy()

    def relative_path_from_metadata(self, metadata):
        return fname
