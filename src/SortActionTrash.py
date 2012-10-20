import os.path
import SortSettings

class SortActionTrash:
    def sort_unsorted_file(self, unsorted_file, relative_dest):
        settings = SortSettings.SortSettings()
        trash_dest = settings.trash_destination()

        print("moving {0} to trash dest {1}".format(unsorted_file.absolute_src,
                                                    trash_dest))
