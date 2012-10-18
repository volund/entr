import os.path

class UnsortedFileSorter:
    def sort_files(self, unsorted_files):
        for unsorted_file in unsorted_files:
            self.sort_file(unsorted_file)
            # Note: should have a flag to stop processing here
    
    def sort_file(self, unsorted_file):
        ftype = unsorted_file.file_type
        ftype.validate_metadata(unsorted_file.metadata)
        
        type_folder = ftype.type_id
        relative_path = ftype.relative_path_from_metadata(unsorted_file.metadata)
        dest_name = unsorted_file.final_relative_filename()
        relative_dest = os.path.join(type_folder, relative_path, dest_name)

        ftype.sort_action.sort_unsorted_file(unsorted_file, relative_dest)
        
        
            
