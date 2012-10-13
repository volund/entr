from FileTypeManager import *

f = FileTypeManager()
f.register_default_types()
for fname in ['bla.mp3', 'test.doc', 't.cad']:
    ftype = f.type_for_file(fname)
    print("%s: %s | %s" % (fname, ftype.type_id, ftype.metadata_for_file(fname)))
