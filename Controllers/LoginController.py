import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.User import User
from Controllers.menuprincipalController import menuprincipalController


class LoginController():

    def __init__(self, log_in):
        self.user = User(connection())  
        self.log_in = log_in
        self.menu = menuprincipalController(connection())
        
    def logIn(self,user,password, MenuPrincipal, LogIn): 
        if user and password:
            user = self.user.getUser(user,password)
            if user:
                result= user[3]
                if result == 'Administrador':
                    self.log_in.Form = QtWidgets.QMainWindow()
                    self.log_in.ui = MenuPrincipal()
                    self.log_in.ui.setupUi(self.log_in.Form)
                    self.log_in.Form.show()
                    self.menu.displayText(user)
                    print('Estas logeado')
                    LogIn.close()

                if result == 'Encargado de compras':
                    self.log_in.Form = QtWidgets.QMainWindow()
                    self.log_in.ui = MenuPrincipal()
                    self.log_in.ui.setupUi(self.log_in.Form)
                    self.log_in.Form.show()
                    self.menu.displayText(user)
                    
                    self.log_in.ui.btn_gestionVenta.hide()
                    self.log_in.ui.btn_registrarUsuario.hide()
                    self.log_in.ui.btn_gestionClave.hide()
                    self.log_in.ui.btn_gestionBackup.hide()
                    
                    print('Estas logeado')
                    LogIn.close()
                if result == 'Encargado de ventas':
                    self.log_in.Form = QtWidgets.QMainWindow()
                    self.log_in.ui = MenuPrincipal()
                    self.log_in.ui.setupUi(self.log_in.Form)
                    self.log_in.Form.show()
                    self.menu.displayText(user)
                   
                    self.log_in.ui.page_gestionCompra.hide()                    
                    self.log_in.ui.btn_gestionCompra.hide()
                    self.log_in.ui.btn_registrarUsuario.hide()
                    self.log_in.ui.btn_gestionClave.hide()
                    self.log_in.ui.btn_gestionBackup.hide()
                    self.log_in.ui.btn_gestionStock.hide()
                    print('Estas logeado')
                    LogIn.close()
                if result == 'Encargado de deposito':
                    self.log_in.Form = QtWidgets.QMainWindow()
                    self.log_in.ui = MenuPrincipal()
                    self.log_in.ui.setupUi(self.log_in.Form)
                    self.log_in.Form.show()
                    self.menu.displayText(user)
                    
                    self.log_in.ui.btn_gestionVenta.hide()
                    self.log_in.ui.btn_registrarUsuario.hide()
                    self.log_in.ui.btn_gestionClave.hide()
                    self.log_in.ui.btn_gestionBackup.hide()
                    self.log_in.ui.btn_gestionCompra.hide()
                    self.log_in.ui.page_gestionCompra.hide()  
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
        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese su Usuario y contraseña")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 


    def salir(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cerrar el programa y salir?")
        msgBox.setWindowTitle("Sistema Tweety")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
         sys.exit()

         