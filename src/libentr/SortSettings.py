class SortSettings:
    settings = {'primary_destination_root':'',
                'default_source':'/Users/amos/Downloads/',
                'trash_destination':''}
    
    def primary_destination_root(self):
        return self.settings['primary_destination_root']

    def set_primary_destination_root(self, root):
        self.settings['primary_destination_root'] = root

    def trash_destination(self):
        return self.settings['trash_destination']

    def set_trash_destination(self, trash_dest):
        self.settings['trash_destination'] = trash_dest

    def default_source(self):
        return self.settings['default_source']

    def set_default_source(self, default_source):
        self.settings['default_source'] = default_source
