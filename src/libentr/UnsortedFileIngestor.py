import os, fnmatch
import FileTypeManager
import UnsortedFile

class UnsortedFileIngestor:
    def __init__(self):
        self.type_manager = FileTypeManager.FileTypeManager()
        self.type_manager.register_default_types()

    def ingest_directory(self, path, pattern="[!.]*"):
        paths = []
        for root, dirnames, filenames in os.walk(path):
            for fname in fnmatch.filter(filenames, pattern):
                abs_src = os.path.join(root, fname)
                paths.append(abs_src)
        return self.ingest_paths(paths)

    def ingest_paths(self, paths):
        ufiles = [self.ingest_path(path) for path in paths]
        return ufiles

    def ingest_path(self, absolute_src):
        unsorted_file = UnsortedFile.UnsortedFile(absolute_src)
        return self.ingest_unsorted_file(unsorted_file)

    def ingest_unsorted_file(self, unsorted_file):
        ftype = self.type_manager.type_for_file(unsorted_file.absolute_src)
        metadata = ftype.metadata_for_file(unsorted_file.absolute_src)
        unsorted_file.file_type = ftype
        unsorted_file.metadata = metadata
        return unsorted_file
        
