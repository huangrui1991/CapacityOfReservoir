__author__ = 'HR'

import arcpy
from PyQt4 import QtCore
from PyQt4 import QtGui
import sys
import CreateDEMDialog

class DEMGenerater():
    def __init__(self):
        pass

    InputFilePath = QtCore.QString()

    @QtCore.pyqtSlot()
    def SelectFilePath(self):
        InputFilePath = QtGui.QFileDialog.getOpenFileName()
        if(InputFilePath != None):
            pass

class DEMCreater(QtGui.QDialog,CreateDEMDialog.Ui_CreateDEMDialog):
    __demGenerater__ = DEMGenerater()

    def __init__(self,parent = 0):
        super(DEMCreater, self).__init__(parent)
        self.setupUi(self,CreateDEMDialog)
        QtCore.QObject.connect(self,self.InputFeatureClassPathButton,"click(self)",self.__demGenerater__,"SelectFilePath(self)")



