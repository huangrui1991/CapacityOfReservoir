__author__ = 'HR'
import pythonaddins

import arcpy
from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
try:
    import CreateDEMDialog
except ImportError as e:
    print e.message

class DEMGenerater( QtCore.QObject ):
    def __init__(self):
        super(QtCore.QObject, self).__init__()

    InputFilePath = QtCore.QString()

    @QtCore.pyqtSlot()
    def SelectFilePath(self):
        InputFilePath = QtGui.QFileDialog.getOpenFileName()
        if(InputFilePath != None):
            print InputFilePath

class DEMCreater(QtGui.QDialog,CreateDEMDialog.Ui_CreateDEMDialog):
    __demGenerater__ = DEMGenerater()

    def __init__(self,parent = None):
        super(DEMCreater, self).__init__(parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.InputFeatureClassPathButton, QtCore.SIGNAL('click(self)'), self.__demGenerater__,
                               QtCore.SLOT('SelectFilePath()'))

def p():
    print 'hello world'





