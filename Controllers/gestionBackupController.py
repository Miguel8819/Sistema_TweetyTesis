import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox


class gestionBackupController():
    
    def __init__(self, backup):
        self.backup = backup
    
   

    def salir(self,gestion_backup):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea salir?")
        msgBox.setWindowTitle("Backup")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            gestion_backup.close()