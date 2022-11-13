import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.User import User
from Views.menuprincipal import Ui_menuprincipal
class LoginController():

    def __init__(self, log_in):
        self.user = User(connection())
        self.log_in = log_in

    def logIn(self,user,password, MenuPrincipal, LogIn):
        if user and password:
            user = self.user.getUser(user,password)
            if user:
                self.log_in.Form = QtWidgets.QMainWindow()
                self.log_in.ui = MenuPrincipal()
                self.log_in.ui.setupUi(self.log_in.Form)
                self.log_in.Form.show()
                print('Estas logeado')
                LogIn.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Usuario o contraseña incorrecta")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

    def salir():
        sys.exit()