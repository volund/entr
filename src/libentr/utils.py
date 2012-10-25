from PyQt4 import QtCore

def qstring_as_unicode(qstr):
    codec0 = QtCore.QTextCodec.codecForName("UTF-16");
    return unicode(codec0.fromUnicode(qstr), 'UTF-16')
