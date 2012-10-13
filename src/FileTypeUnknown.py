import FileType

class FileTypeUnknown(FileType.FileType):
    @property
    def type_id(self):
        return 'Music'

    def can_handle_file(self, absolute_fname):
        return True

    def metadata_for_file(self, absolute_fname):
        return {}

    def suggestions_for_meta_field(self, metadata, field):
        return []

    def relative_path_from_metadata(self, metadata, fname):
        return fname
