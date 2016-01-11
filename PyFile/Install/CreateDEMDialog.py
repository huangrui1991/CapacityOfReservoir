# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GreateDEMDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CreateDEMDialog(object):
    def setupUi(self, CreateDEMDialog):
        CreateDEMDialog.setObjectName(_fromUtf8("CreateDEMDialog"))
        CreateDEMDialog.resize(378, 183)
        CreateDEMDialog.setMaximumSize(QtCore.QSize(16777214, 16777215))
        CreateDEMDialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.verticalLayout = QtGui.QVBoxLayout(CreateDEMDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.InputFeatureClassLayout = QtGui.QGridLayout()
        self.InputFeatureClassLayout.setObjectName(_fromUtf8("InputFeatureClassLayout"))
        self.InputFeatureClassLabel = QtGui.QLabel(CreateDEMDialog)
        self.InputFeatureClassLabel.setObjectName(_fromUtf8("InputFeatureClassLabel"))
        self.InputFeatureClassLayout.addWidget(self.InputFeatureClassLabel, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(238, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.InputFeatureClassLayout.addItem(spacerItem, 0, 1, 1, 2)
        self.InputFeatureClassPathLineEdit = QtGui.QLineEdit(CreateDEMDialog)
        self.InputFeatureClassPathLineEdit.setObjectName(_fromUtf8("InputFeatureClassPathLineEdit"))
        self.InputFeatureClassLayout.addWidget(self.InputFeatureClassPathLineEdit, 1, 0, 1, 2)
        self.InputFeatureClassPathButton = QtGui.QPushButton(CreateDEMDialog)
        self.InputFeatureClassPathButton.setMaximumSize(QtCore.QSize(30, 30))
        self.InputFeatureClassPathButton.setObjectName(_fromUtf8("InputFeatureClassPathButton"))
        self.InputFeatureClassLayout.addWidget(self.InputFeatureClassPathButton, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.InputFeatureClassLayout)
        self.OutputDEMGridLayout = QtGui.QGridLayout()
        self.OutputDEMGridLayout.setObjectName(_fromUtf8("OutputDEMGridLayout"))
        self.OutputDEMLabel = QtGui.QLabel(CreateDEMDialog)
        self.OutputDEMLabel.setObjectName(_fromUtf8("OutputDEMLabel"))
        self.OutputDEMGridLayout.addWidget(self.OutputDEMLabel, 0, 0, 1, 1)
        self.OutputDEMLineEdit = QtGui.QLineEdit(CreateDEMDialog)
        self.OutputDEMLineEdit.setObjectName(_fromUtf8("OutputDEMLineEdit"))
        self.OutputDEMGridLayout.addWidget(self.OutputDEMLineEdit, 1, 0, 1, 2)
        self.OutputDEMPushButton = QtGui.QPushButton(CreateDEMDialog)
        self.OutputDEMPushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.OutputDEMPushButton.setObjectName(_fromUtf8("OutputDEMPushButton"))
        self.OutputDEMGridLayout.addWidget(self.OutputDEMPushButton, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.OutputDEMGridLayout.addItem(spacerItem1, 0, 1, 1, 2)
        self.verticalLayout.addLayout(self.OutputDEMGridLayout)
        self.HeightFieldGridLayout = QtGui.QGridLayout()
        self.HeightFieldGridLayout.setObjectName(_fromUtf8("HeightFieldGridLayout"))
        self.HeightFieldLabel = QtGui.QLabel(CreateDEMDialog)
        self.HeightFieldLabel.setMaximumSize(QtCore.QSize(80, 16777215))
        self.HeightFieldLabel.setObjectName(_fromUtf8("HeightFieldLabel"))
        self.HeightFieldGridLayout.addWidget(self.HeightFieldLabel, 0, 0, 1, 1)
        self.HeightFieldComboBox = QtGui.QComboBox(CreateDEMDialog)
        self.HeightFieldComboBox.setObjectName(_fromUtf8("HeightFieldComboBox"))
        self.HeightFieldGridLayout.addWidget(self.HeightFieldComboBox, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.HeightFieldGridLayout)
        self.ButtonBox = QtGui.QDialogButtonBox(CreateDEMDialog)
        self.ButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.ButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.ButtonBox.setObjectName(_fromUtf8("ButtonBox"))
        self.verticalLayout.addWidget(self.ButtonBox)
        self.ButtonBox.raise_()
        self.InputFeatureClassLabel.raise_()
        self.InputFeatureClassPathLineEdit.raise_()
        self.InputFeatureClassPathButton.raise_()
        self.OutputDEMLineEdit.raise_()
        self.OutputDEMLabel.raise_()
        self.OutputDEMPushButton.raise_()
        self.HeightFieldComboBox.raise_()
        self.HeightFieldLabel.raise_()
        self.HeightFieldLabel.raise_()

        self.retranslateUi(CreateDEMDialog)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CreateDEMDialog.accept)
        QtCore.QObject.connect(self.ButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CreateDEMDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CreateDEMDialog)

    def retranslateUi(self, CreateDEMDialog):
        CreateDEMDialog.setWindowTitle(_translate("CreateDEMDialog", "CreateDEMDialog", None))
        self.InputFeatureClassLabel.setText(_translate("CreateDEMDialog", "Input Feature Class", None))
        self.InputFeatureClassPathButton.setText(_translate("CreateDEMDialog", "...", None))
        self.OutputDEMLabel.setText(_translate("CreateDEMDialog", "Output DEM", None))
        self.OutputDEMPushButton.setText(_translate("CreateDEMDialog", "...", None))
        self.HeightFieldLabel.setText(_translate("CreateDEMDialog", "HeightField", None))

