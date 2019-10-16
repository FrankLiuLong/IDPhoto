# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/liuqingbin/SoftwareProject/Python/IDPhoto/src/idphoto.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IDPhoto(object):
    def setupUi(self, IDPhoto):
        IDPhoto.setObjectName("IDPhoto")
        IDPhoto.resize(448, 366)
        self.pushButton_Save = QtWidgets.QPushButton(IDPhoto)
        self.pushButton_Save.setGeometry(QtCore.QRect(290, 210, 112, 32))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.comboBox_Size = QtWidgets.QComboBox(IDPhoto)
        self.comboBox_Size.setGeometry(QtCore.QRect(300, 80, 91, 32))
        self.comboBox_Size.setObjectName("comboBox_Size")
        self.comboBox_Color = QtWidgets.QComboBox(IDPhoto)
        self.comboBox_Color.setGeometry(QtCore.QRect(300, 150, 91, 32))
        self.comboBox_Color.setObjectName("comboBox_Color")
        self.graphicsView = QtWidgets.QGraphicsView(IDPhoto)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 231, 251))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_Open = QtWidgets.QPushButton(IDPhoto)
        self.pushButton_Open.setGeometry(QtCore.QRect(290, 20, 112, 32))
        self.pushButton_Open.setObjectName("pushButton_Open")

        self.retranslateUi(IDPhoto)
        QtCore.QMetaObject.connectSlotsByName(IDPhoto)

    def retranslateUi(self, IDPhoto):
        _translate = QtCore.QCoreApplication.translate
        IDPhoto.setWindowTitle(_translate("IDPhoto", "证件照"))
        self.pushButton_Save.setText(_translate("IDPhoto", "保存"))
        self.pushButton_Open.setText(_translate("IDPhoto", "打开"))

idphoto_dlg = Ui_IDPhoto()