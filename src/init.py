from Ui_idphoto import *
from PyQt5 import QtCore, QtGui, QtWidgets
from idphoto_slot import *
import cv2
import numpy as np

def initApp():
    img_oneInchBack = cv2.imread("one-inch.jpg")
    cv2.imshow("333",img_oneInchBack)