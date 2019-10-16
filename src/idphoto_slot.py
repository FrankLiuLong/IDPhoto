import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Ui_idphoto
from image_process import *


def slotpushButton_Open(UiName):
    print("open")
    imgName,imgType = QFileDialog.getOpenFileName(None,"打开图片","","*.jpg;;*.png;;All Files(*)")
    img_original = cv2.imread(imgName)
    #cv2.imshow('img',img_original)
    print(img_original)

def initIDphotoUI(UiName):
    print("init\n")
    UiName.pushButton_Open.clicked.connect(lambda:slotpushButton_Open(UiName))
