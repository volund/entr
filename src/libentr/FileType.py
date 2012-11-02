import collections
from SortActionMove import SortActionMove

class FileType:
    @property
    def type_id(self):
        return 'AbstractBase'
    
    @property
    def sort_action(self):
        return SortActionMove()
    
    def can_handle_file(self, absolute_fname):
        return False

    def metadata_template(self):
        return collections.OrderedDict()
    
    def metadata_for_file(self, absolute_fname):
        return self.metadata_template()
    
    def suggestions_for_meta_field(self, metadata, field):
        return [].copy()
    
    def relative_path_from_metadata(self, metadata):
        return ""
    
    def validate_metadata(self, metadata):
        # Should raise an exception of type InvalidMetadataError
        # if the metadata is invalid
        pass
    
