import os.path
import SortSettings

class SortActionMove:
    def sort_unsorted_file(self, unsorted_file, relative_dest):
        settings = SortSettings.SortSettings()
        dest_root = settings.primary_destination_root()

        dest = os.path.join(dest_root, relative_dest)

        print("moving {0} to relative dest {1}".format(unsorted_file.absolute_src,
                                                       dest))
