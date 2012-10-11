import DocumentTypeSimpleCategorizer
import os

class DocumentTypeDocument(DocumentTypeSimpleCategorizer.DocumentTypeSimpleCategorizer):
    def __init__(self):
        extensions = [".txt", ".rtf", ".doc", ".xdoc", ".xls"]
        metadata = {'Category':'', 'Subcategory':'', 'Sub-subcategory':''}
        DocumentTypeSimpleCategorizer.__init__(extensions, metadata)
        
    def relative_path_from_metadata(metadata, fname):
        categories = [metadata['Category'], 
                      metadata['Subcategory'],
                      metadata['Sub-subcategory']]
        path_components = [category for category in categories if category != ""]
        if path_components == []:
            path_components = ['Unknown']
        path_components.append(fname)
        return os.join(path_components)
