import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.User import User

class RegistrarController():

    def __init__(self, registrar):
        self.user = User(connection())
        self.registrar = registrar

    def registrarUsuario(self, user, password, repitPassword,rol):
            if user and password and repitPassword and rol:
                
                result = self.user.getUser1(user)
                
                if result:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El usuario ya existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("")
                    x = msg.exec_()

                else:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Information)
                        msgBox.setText("¿Desea guardar los datos? ")
                        msgBox.setWindowTitle("Confirmacion")
                        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        returnValue = msgBox.exec()
                        if returnValue == QMessageBox.Ok:
                            
                            if returnValue == QMessageBox.Ok and  password !="" and repitPassword != ""  and password == repitPassword: 
                                self.user.registrarUsuario(user,password,rol)

                                msg = QMessageBox()
                                msg.setWindowTitle("Exito")
                                msg.setText("Usuario guardado")
                                msg.setIcon(QMessageBox.Information)
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.setDefaultButton(QMessageBox.Ok)
                                msg.setInformativeText("")
                                x = msg.exec_()

                                self.registrar.input_usuario.clear()
                                self.registrar.input_password.clear()
                                self.registrar.repit_password.clear()
                                
                            
                            elif returnValue == QMessageBox.Ok and password != repitPassword:
                            
                                msg = QMessageBox()
                                msg.setWindowTitle("Error")
                                msg.setText("Las contraseñas no coincide")
                                msg.setIcon(QMessageBox.Information)
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.setDefaultButton(QMessageBox.Ok)
                                msg.setInformativeText("Vuelva a intentarlo")
                                x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Por favor complete todos los campos")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()

    def cancelar(self, Ui_registrarUsuario):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cancelar y salir?")
        msgBox.setWindowTitle("Usuarios")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            Ui_registrarUsuario.close()                
