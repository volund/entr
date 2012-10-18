class SortSettings:
    settings = {'primary_destination_root':''}
    
    def primary_destination_root(self):
        return self.settings['primary_destination_root']

    def set_primary_destination_root(self, root):
        self.settings['primary_destination_root'] = root
