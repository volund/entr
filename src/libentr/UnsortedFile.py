import os.path

class UnsortedFile:
    def __init__(self, absolute_src):
        self.absolute_src = absolute_src
        self.file_type = None
        self.relative_dst = ''
        self.metadata = {}

    def final_relative_filename(self):
        if (self.relative_dst) != '' and (self.relative_dst != None):
            return self.relative_dst
        return os.path.basename(self.absolute_src)
