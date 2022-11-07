import sys
#import os

#myDir = os.getcwd()
#sys.path.append(myDir)

from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi    
#from Controllers.menuprincipalController import menuprincipalController

class Ui_menuprincipal(object):
    def __init__(self):
        super(Ui_menuprincipal, self).__init__()
        loadUi(uifile="menuprincipal.ui")
        #self.menuprincipalController = menuprincipalController(self)