from FileTypeMusic    import *
from FileTypeDocument import *
from FileTypeUnknown  import *
from FileTypeTrash import *

def all_types():
    return [FileTypeMusic(), FileTypeDocument(), FileTypeUnknown(), FileTypeTrash()]
