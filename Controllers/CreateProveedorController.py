import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets, QtGui
from Database.Connection import connection
from Models.Proveedores import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QStringListModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from datetime import datetime

class CreateProveedorController():
    def __init__(self, create_proveedor):
        self.proveedor = Proveedor(connection())
        self.create_proveedor = create_proveedor

    def createProveedor(self,  nombreProveedor, nombreFactura,nroCuil, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb):
        if nombreProveedor:
            
            fechaAlta1= datetime.now()
            fechaAlta= datetime.strftime(fechaAlta1, '%d/%m/%Y %H:%M:%S')
            
            result = self.proveedor.getProveedor(nombreProveedor, '1')
        
            if result:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El proveedor ya existe")
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
                        
                        if nroCuil and nombreProveedor and nombreFactura and fechaAlta and calle and numeroCalle and ciudad and codPostal and celular and email and pagWeb:
                            self.proveedor.insertProveedor(nroCuil,nombreProveedor,nombreFactura,fechaAlta,calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb)

                            msg = QMessageBox()
                            msg.setWindowTitle("Exito")
                            msg.setText("Proveedor guardado")
                            msg.setIcon(QMessageBox.Information)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("")
                            x = msg.exec_()

                            self.create_proveedor.input_nameProv.clear()
                            self.create_proveedor.input_nameFact.clear()
                            self.create_proveedor.input_nroCuil.clear()
                            self.create_proveedor.input_calle.clear()
                            self.create_proveedor.input_numCalle.clear()
                            self.create_proveedor.input_codPostal.clear()
                            self.create_proveedor.input_tel.clear()
                            self.create_proveedor.input_email.clear()
                            self.create_proveedor.input_web.clear()

                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Error")
                            msg.setText("Complete los campos que estan vacios")
                            msg.setIcon(QMessageBox.Information)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("")
                            x = msg.exec_()

        

    def showProveedor(self,nombreProveedor):
        if nombreProveedor:
            result = self.proveedor.getProveedor(nombreProveedor, '1')
            if result:
                self.create_proveedor.show_nroCuil.setText(str(result[1]))
                self.create_proveedor.show_nameProv.setText(str(result[2]))
                self.create_proveedor.show_nameFact.setText(str(result[3]))
                self.create_proveedor.show_calle.setText(str(result[5]))
                self.create_proveedor.show_numCalle.setText(str(result[6]))
                self.create_proveedor.show_ciudad.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal.setText(str(result[8]))
                self.create_proveedor.show_tel.setText(str(result[9]))
                self.create_proveedor.show_email.setText(str(result[10]))
                self.create_proveedor.show_web.setText(str(result[11]))

                self.create_proveedor.input_searchNameProv.clear()
                
            else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El nombre de proveedor no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
                    
                    self.create_proveedor.input_searchNameProv.clear()
                    self.create_proveedor.show_nameProv.clear()
                    self.create_proveedor.show_nameFact.clear()                         
                    self.create_proveedor.show_calle.clear()
                    self.create_proveedor.show_numCalle.clear()
                    self.create_proveedor.show_nroCuil.clear()
                    self.create_proveedor.show_codPostal.clear()
                    self.create_proveedor.show_tel.clear()
                    self.create_proveedor.show_email.clear()
                    self.create_proveedor.show_web.clear()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un nombre de proveedor válido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

                self.create_proveedor.show_nameProv.clear()
                self.create_proveedor.show_nameFact.clear()                
                self.create_proveedor.show_calle.clear()
                self.create_proveedor.show_numCalle.clear()
                self.create_proveedor.show_codPostal.clear()
                self.create_proveedor.show_tel.clear()
                self.create_proveedor.show_email.clear()
                self.create_proveedor.show_web.clear()

    def buscarProveedor(self,nroCuit):
        if nroCuit:
            result = self.proveedor.getProveedor_2(nroCuit, '1')
            if result:
                self.create_proveedor.show_nroCuil.setText(str(result[1]))
                self.create_proveedor.show_nameProv.setText(str(result[2]))
                self.create_proveedor.show_nameFact.setText(str(result[3]))
                self.create_proveedor.show_calle.setText(str(result[5]))
                self.create_proveedor.show_numCalle.setText(str(result[6]))
                self.create_proveedor.show_ciudad.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal.setText(str(result[8]))
                self.create_proveedor.show_tel.setText(str(result[9]))
                self.create_proveedor.show_email.setText(str(result[10]))
                self.create_proveedor.show_web.setText(str(result[11]))

                self.create_proveedor.input_searchNameFact.clear()
            else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El número de Cuit/Cuil no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
                    
                    self.create_proveedor.input_searchNameProv.clear()
                    self.create_proveedor.show_nameProv.clear()
                    self.create_proveedor.show_nameFact.clear()
                    self.create_proveedor.show_calle.clear()
                    self.create_proveedor.show_numCalle.clear()
                    self.create_proveedor.show_nroCuil.clear()
                    self.create_proveedor.show_codPostal.clear()
                    self.create_proveedor.show_tel.clear()
                    self.create_proveedor.show_email.clear()
                    self.create_proveedor.show_web.clear()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un número de Cuit/Cuil válido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

                self.create_proveedor.show_nameProv.clear()
                self.create_proveedor.show_nameFact.clear()                    
                self.create_proveedor.show_calle.clear()
                self.create_proveedor.show_numCalle.clear()
                self.create_proveedor.show_codPostal.clear()
                self.create_proveedor.show_tel.clear()
                self.create_proveedor.show_email.clear()
                self.create_proveedor.show_web.clear()
                


    def showProveedor_2(self,nombreProveedor):
        if nombreProveedor:
            result = self.proveedor.getProveedor(nombreProveedor, '1')
            if result:
                self.create_proveedor.show_nroCuil_2.setText(str(result[1]))
                self.create_proveedor.show_nameProv_2.setText(str(result[2]))
                self.create_proveedor.show_nameFact_2.setText(str(result[3]))
                self.create_proveedor.show_calle_2.setText(str(result[5]))
                self.create_proveedor.show_numCalle_2.setText(str(result[6]))
                self.create_proveedor.show_ciudad_2.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal_2.setText(str(result[8]))
                self.create_proveedor.show_tel_2.setText(str(result[9]))
                self.create_proveedor.show_email_2.setText(str(result[10]))
                self.create_proveedor.show_web_2.setText(str(result[11]))

                self.create_proveedor.input_searchNameProv_2.clear()
            else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El nombre de proveedor no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese un proveedor valido")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 

    def buscarProveedor_2(self,nroCuit):
        if nroCuit:
            result = self.proveedor.getProveedor_2(nroCuit, '1')
            if result:
                self.create_proveedor.show_nroCuil_2.setText(str(result[1]))
                self.create_proveedor.show_nameProv_2.setText(str(result[2]))
                self.create_proveedor.show_nameFact_2.setText(str(result[3]))
                self.create_proveedor.show_calle_2.setText(str(result[5]))
                self.create_proveedor.show_numCalle_2.setText(str(result[6]))
                self.create_proveedor.show_ciudad_2.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal_2.setText(str(result[8]))
                self.create_proveedor.show_tel_2.setText(str(result[9]))
                self.create_proveedor.show_email_2.setText(str(result[10]))
                self.create_proveedor.show_web_2.setText(str(result[11]))

                self.create_proveedor.input_searchNameFact_2.clear()

            else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El número de Cuit/Cuil no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese un número de Cuit/Cuil valido")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()


    def darBajaProveedor(self,proveedores,nombreProveedor):
        if nombreProveedor:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea dar de baja al proveedor?")
            msgBox.setWindowTitle("Baja de proveedor")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
            
                
                if proveedores :                      
                        self.proveedor.bajaProveedor(nombreProveedor)

                msg = QMessageBox()
                msg.setWindowTitle("Confirmado")
                msg.setText("Proveedor dado de baja de la lista")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_() 

                self.create_proveedor.input_searchNameProv_2.clear()
                self.create_proveedor.show_nameProv_2.clear()
                self.create_proveedor.show_nameFact_2.clear()
                            
                self.create_proveedor.show_calle_2.clear()
                self.create_proveedor.show_numCalle_2.clear()
                self.create_proveedor.show_nroCuil_2.clear()
                self.create_proveedor.show_codPostal_2.clear()
                self.create_proveedor.show_tel_2.clear()
                self.create_proveedor.show_email_2.clear()
                self.create_proveedor.show_web_2.clear()

          

        else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un proveedor valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

    def darBajaProveedor2(self,proveedores,cuil):
        if cuil:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea dar de baja al proveedor? ")
            msgBox.setWindowTitle("Baja de proveedor")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
            
                
                if proveedores :                      
                        self.proveedor.bajaProveedor2(cuil)

                msg = QMessageBox()
                msg.setWindowTitle("Confirmado")
                msg.setText("Proveedor dado de baja de la lista")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_() 

                self.create_proveedor.input_searchNameProv_2.clear()
                self.create_proveedor.show_nameProv_2.clear()
                self.create_proveedor.show_nameFact_2.clear()
                            
                self.create_proveedor.show_calle_2.clear()
                self.create_proveedor.show_numCalle_2.clear()
                self.create_proveedor.show_nroCuil_2.clear()
                self.create_proveedor.show_codPostal_2.clear()
                self.create_proveedor.show_tel_2.clear()
                self.create_proveedor.show_email_2.clear()
                self.create_proveedor.show_web_2.clear()

          

        else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un numero de cuit valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 


    def modificarProveedor(self,nombreProveedor, nombreFactura, nroCuil, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb ):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea guardar los cambios del proveedor? ")
        msgBox.setWindowTitle("")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
                    if nombreProveedor != "" and nombreFactura !="" and calle !="" and numeroCalle != ""  and codPostal != "" and celular != "" and email != "" and pagWeb != "":
                        self.proveedor.UpdateProveedor(nroCuil,nombreProveedor, nombreFactura, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb)

                        msg = QMessageBox()
                        msg.setWindowTitle("Confirmado")
                        msg.setText("Cambios guardados")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("")
                        x = msg.exec_() 

                        self.create_proveedor.input_searchNameProv.clear()
                        self.create_proveedor.show_nameProv.clear()

                        self.create_proveedor.show_nameFact.clear()
                        self.create_proveedor.show_ciudad.setCurrentText('Alta Gracia') 

                        self.create_proveedor.show_nameFact.clear()              
                        self.create_proveedor.show_calle.clear()
                        self.create_proveedor.show_numCalle.clear()
                        self.create_proveedor.show_nroCuil.clear()
                        self.create_proveedor.show_codPostal.clear()
                        self.create_proveedor.show_tel.clear()
                        self.create_proveedor.show_email.clear()
                        self.create_proveedor.show_web.clear()

                    else: 
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Hay campos vacios")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_() 

    def cancelar(self, Ui_Proveedores):

        Ui_Proveedores.close()