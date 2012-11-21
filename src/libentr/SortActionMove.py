import os.path
import SortSettings
import shutil

class SortActionMove:
    def sort_unsorted_file(self, unsorted_file, relative_dest):
        settings = SortSettings.SortSettings()
        dest_root = settings.primary_destination_root()
        dest = os.path.join(dest_root, relative_dest)
        
        print(u"moving", unsorted_file.absolute_src," to relative dest", dest)
        dirname = os.path.dirname(dest)
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        shutil.move(unsorted_file.absolute_src, dest)
