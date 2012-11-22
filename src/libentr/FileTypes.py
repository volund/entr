from FileTypeMusic    import *
from FileTypeDocument import *
from FileTypeImages import *
from FileTypeEbook import *
from FileTypeUnknown  import *
from FileTypeTrash import *

def all_types():
    return [FileTypeMusic(), FileTypeImages(), FileTypeEbook(), FileTypeDocument(), FileTypeUnknown(), FileTypeTrash()]
