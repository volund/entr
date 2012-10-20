import FileType
from SortActionTrash import SortActionTrash

class FileTypeTrash(FileType.FileType):
    @property
    def type_id(self):
        return 'Trash'

    @property
    def sort_action(self):
        return SortActionTrash()
    
    def can_handle_file(self, absolute_fname):
        return False

    def metadata_for_file(self, absolute_fname):
        return {}

    def suggestions_for_meta_field(self, metadata, field):
        return []

    def relative_path_from_metadata(self, metadata):
        return ""
