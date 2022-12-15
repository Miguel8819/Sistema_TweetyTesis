import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

class gestionBackupController():
    
    def __init__(self, backup):
        self.backup = backup

    def salir(self,gestion_backup):
        gestion_backup.close()