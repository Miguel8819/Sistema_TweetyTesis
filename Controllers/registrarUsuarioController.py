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
                                msg.setText("La contraseña no coincide")
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





# def modificarPassword(self, user, oldPassword, newPass, newPassRepeat):
#             if user:
#                 result = self.user.getUser1(user)    
#                 if result:
#                     msgBox = QMessageBox()
#                     msgBox.setIcon(QMessageBox.Information)
#                     msgBox.setText("¿Desea cambiar su contraseña? ")
#                     msgBox.setWindowTitle("")
#                     msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#                     returnValue = msgBox.exec()
#                     flag = 0
#                     exit = False
#                     while exit == False:
#                         if returnValue == QMessageBox.Ok and  oldPassword !="" and newPass != "" and newPassRepeat != "" and newPass == newPassRepeat and oldPassword != newPass and oldPassword != newPassRepeat: 
#                             flag = 1
#                             exit = True
#                         elif returnValue == QMessageBox.Ok and user == "" or oldPassword == "" or newPass == "" or newPassRepeat == "":
#                             flag = 2
#                             exit = True
#                         elif returnValue == QMessageBox.Ok and newPass != newPassRepeat:
#                             flag = 3
#                             exit = True
                        
#                         elif returnValue == QMessageBox.Ok and oldPassword == newPass or oldPassword == newPassRepeat:
#                             flag = 5
#                             exit = True

#                     if flag == 1:
#                         status = self.user.updatePassword(user, oldPassword, newPass)
#                         if status == True:
#                             msg = QMessageBox()
#                             msg.setWindowTitle("Confirmado")
#                             msg.setText("Cambios guardados")
#                             msg.setIcon(QMessageBox.Information)
#                             msg.setStandardButtons(QMessageBox.Ok)
#                             msg.setDefaultButton(QMessageBox.Ok)
#                             msg.setInformativeText("")
#                             x = msg.exec_() 

#                             self.log_in.input_user.clear()
#                             self.log_in.input_oldPassword.clear()
#                             self.log_in.input_newPassword.clear()
#                             self.log_in.input_newPasswordRepetir.clear()
                        
#                         elif status == False:
#                             msg = QMessageBox()
#                             msg.setWindowTitle("Error")
#                             msg.setText("Su contraseña en uso es incorrecta")
#                             msg.setIcon(QMessageBox.Warning)
#                             msg.setStandardButtons(QMessageBox.Ok)
#                             msg.setDefaultButton(QMessageBox.Ok)
#                             msg.setInformativeText("")
#                             x = msg.exec_() 

#                             self.log_in.input_oldPassword.clear()
#                             self.log_in.input_newPassword.clear()
#                             self.log_in.input_newPasswordRepetir.clear()

#                     elif flag == 2: 
#                         msg = QMessageBox()
#                         msg.setWindowTitle("Error")
#                         msg.setText("Hay campos vacios")
#                         msg.setIcon(QMessageBox.Information)
#                         msg.setStandardButtons(QMessageBox.Ok)
#                         msg.setDefaultButton(QMessageBox.Ok)
#                         msg.setInformativeText("Vuelva a intentarlo")
#                         x = msg.exec_() 
                        

#                     elif flag == 3:
#                         msg = QMessageBox()
#                         msg.setWindowTitle("Error")
#                         msg.setText("La contraseña nueva no coincide")
#                         msg.setIcon(QMessageBox.Information)
#                         msg.setStandardButtons(QMessageBox.Ok)
#                         msg.setDefaultButton(QMessageBox.Ok)
#                         msg.setInformativeText("Vuelva a intentarlo")
#                         x = msg.exec_() 

#                     elif flag == 5:
#                         msg = QMessageBox()
#                         msg.setWindowTitle("Error")
#                         msg.setText("La contraseña nueva debe ser diferente a la actual")
#                         msg.setIcon(QMessageBox.Information)
#                         msg.setStandardButtons(QMessageBox.Ok)
#                         msg.setDefaultButton(QMessageBox.Ok)
#                         msg.setInformativeText("Vuelva a intentarlo")
#                         x = msg.exec_() 
#                 else:
#                     msg = QMessageBox()
#                     msg.setWindowTitle("Error")
#                     msg.setText("El usuario no existe")
#                     msg.setIcon(QMessageBox.Information)
#                     msg.setStandardButtons(QMessageBox.Ok)
#                     msg.setDefaultButton(QMessageBox.Ok)
#                     msg.setInformativeText("Vuelva a intentarlo")
#                     x = msg.exec_()
#             else:
#                 msg = QMessageBox()
#                 msg.setWindowTitle("Error")
#                 msg.setText("Complete todos los campos")
#                 msg.setIcon(QMessageBox.Information)
#                 msg.setStandardButtons(QMessageBox.Ok)
#                 msg.setDefaultButton(QMessageBox.Ok)
#                 msg.setInformativeText("Vuelva a intentarlo")
#                 x = msg.exec_() 