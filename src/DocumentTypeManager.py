import DocumentTypes

class DocumentTypeManager:
    def __init__(self):
        self.document_types = {}

    def add_document_type(self, label, document_type):
        self.document_types[label] = document_type

    def register_default_types(self):
        types_by_label = DocumentTypes.all_document_labels_and_types()
        for label in types_by_label:
            doc_type = types_by_label[label]
            self.add_document_type(label, doc_type)

    def type_label_for_file(self, absolute_fname):
        for label in self.document_types:
            doc_type = self.document_types[label]
            if doc_type.can_handle_file(absolute_fname):
                return label
        return 'Unknown' # Note: doctype labels should be attributes of the document
                         #       type object, not unrelated strings...

