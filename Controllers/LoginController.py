import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.User import User

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
        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese su Usuario y contraseña")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

    def salir():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cerrar el programa y salir?")
        msgBox.setWindowTitle("Sistema Tweety")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
         sys.exit()

    def modificarPassword(self, user, oldPassword, newPass, newPassRepeat):
            if user:
                result = self.user.getUser1(user)    
                if result:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("¿Desea cambiar su contraseña? ")
                    msgBox.setWindowTitle("")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    returnValue = msgBox.exec()
                    flag = 0
                    exit = False
                    while exit == False:
                        if returnValue == QMessageBox.Ok and  oldPassword !="" and newPass != "" and newPassRepeat != "" and newPass == newPassRepeat and oldPassword != newPass and oldPassword != newPassRepeat: 
                            flag = 1
                            exit = True
                        elif returnValue == QMessageBox.Ok and user == "" or oldPassword == "" or newPass == "" or newPassRepeat == "":
                            flag = 2
                            exit = True
                        elif returnValue == QMessageBox.Ok and newPass != newPassRepeat:
                            flag = 3
                            exit = True
                        
                        elif returnValue == QMessageBox.Ok and oldPassword == newPass or oldPassword == newPassRepeat:
                            flag = 5
                            exit = True

                    if flag == 1:
                        status = self.user.updatePassword(user, oldPassword, newPass)
                        if status == True:
                            msg = QMessageBox()
                            msg.setWindowTitle("Confirmado")
                            msg.setText("Cambios guardados")
                            msg.setIcon(QMessageBox.Information)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("")
                            x = msg.exec_() 

                            self.log_in.input_user.clear()
                            self.log_in.input_oldPassword.clear()
                            self.log_in.input_newPassword.clear()
                            self.log_in.input_newPasswordRepetir.clear()
                        
                        elif status == False:
                            msg = QMessageBox()
                            msg.setWindowTitle("Error")
                            msg.setText("Su contraseña en uso es incorrecta")
                            msg.setIcon(QMessageBox.Warning)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("")
                            x = msg.exec_() 

                            self.log_in.input_oldPassword.clear()
                            self.log_in.input_newPassword.clear()
                            self.log_in.input_newPasswordRepetir.clear()

                    elif flag == 2: 
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Hay campos vacios")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_() 
                        

                    elif flag == 3:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("La contraseña nueva no coincide")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_() 

                    elif flag == 5:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("La contraseña nueva debe ser diferente a la actual")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_() 
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El usuario no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Complete todos los campos")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 


    def salir(self,gestion_clave):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cancelar la operación y salir? ")
        msgBox.setWindowTitle("Cancelar")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            gestion_clave.close()
         