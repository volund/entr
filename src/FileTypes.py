from FileTypeMusic    import *
from FileTypeDocument import *
from FileTypeUnknown  import *

def all_types():
    return [FileTypeMusic(), FileTypeDocument(), FileTypeUnknown()]
