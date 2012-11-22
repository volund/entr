import os.path
import SortSettings
import send2trash

class SortActionTrash:
    def sort_unsorted_file(self, unsorted_file, relative_dest):
        settings = SortSettings.SortSettings()
        #print("moving {0} to trash ".format(unsorted_file.absolute_src))
        send2trash.send2trash(unsorted_file.absolute_src)
