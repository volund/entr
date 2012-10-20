class SortSettings:
    settings = {'primary_destination_root':'',
                'trash_destination':''}
    
    def primary_destination_root(self):
        return self.settings['primary_destination_root']

    def set_primary_destination_root(self, root):
        self.settings['primary_destination_root'] = root

    def trash_destination(self):
        return self.settings['trash_destination']

    def set_trash_destination(self, trash_dest):
        self.settings['trash_destination'] = trash_dest
