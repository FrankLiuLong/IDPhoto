#导入需要的模块
#导入需要的模块
import sys
from Ui_idphoto import *
from PyQt5 import QtWidgets, QtCore
from init import *
from idphoto_slot import *


if __name__ == "__main__":
    initApp()
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    idphoto_dlg.setupUi(Dialog)
    initIDphotoUI(idphoto_dlg)
    #initDialog(Ui_IDPhoto.ui)
    Dialog.show()
    sys.exit(app.exec_())

