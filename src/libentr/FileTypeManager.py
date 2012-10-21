import FileTypes

class FileTypeManager:
    def __init__(self):
        self.file_types = []

    def list_of_types(self):
        types = [ftype.type_id for ftype in self.file_types]
        types.sort()
        return types

    def type_for_id(self, type_id):
        for ftype in self.file_types:
            if ftype.type_id == type_id:
                return ftype
        
        return FileTypes.FileTypeUnknown()
        
    def register_default_types(self):
        self.file_types = FileTypes.all_types()

    def type_for_file(self, absolute_fname):
        for ftype in self.file_types:
            if ftype.can_handle_file(absolute_fname):
                return ftype

        return FileTypes.FileTypeUnknown()
