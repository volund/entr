import FileTypes

class FileTypeManager:
    def __init__(self):
        self.file_types = []

    def register_default_types(self):
        self.file_types = FileTypes.all_types()

    def type_for_file(self, absolute_fname):
        for ftype in self.file_types:
            if ftype.can_handle_file(absolute_fname):
                return ftype.type_id

        return FileTypeUnknown().type_id

