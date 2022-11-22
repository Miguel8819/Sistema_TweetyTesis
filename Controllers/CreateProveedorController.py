import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets, QtGui
from Database.Connection import connection
from Models.Proveedores import *
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QCompleter
from PyQt5.QtCore import QDate, QStringListModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from datetime import date

class CreateProveedorController():
    def __init__(self, create_proveedor):
        self.proveedor = Proveedor(connection())
        self.create_proveedor = create_proveedor

    def createProveedor(self, nombreProveedor, nombreFactura, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb, proveedores):
        if nombreProveedor:
            fechaAlta= date.today()
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
                    if nombreProveedor and nombreFactura and fechaAlta and calle and numeroCalle and ciudad and codPostal and celular and email and pagWeb:
                        self.proveedor.insertProveedor(nombreProveedor,nombreFactura,fechaAlta,calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb)

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

        

    def showProveedor(self,nombreProveedor, nameProv, nameFact, calle, numCalle, ciudad, codPostal, tel, email, web):
        if nombreProveedor:
            result = self.proveedor.getProveedor(nombreProveedor, '1')
            self.create_proveedor.show_nameProv.setText(str(result[1]))
            self.create_proveedor.show_nameFact.setText(str(result[2]))
            
            self.create_proveedor.show_calle.setText(str(result[4]))
            self.create_proveedor.show_numCalle.setText(str(result[5]))
            self.create_proveedor.show_ciudad.setCurrentText(str(result[6]))
            self.create_proveedor.show_codPostal.setText(str(result[7]))
            self.create_proveedor.show_tel.setText(str(result[8]))
            self.create_proveedor.show_email.setText(str(result[9]))
            self.create_proveedor.show_web.setText(str(result[10]))

    def autoCompleteProveedor(self):
        result = QStringListModel(self.proveedor.autoComplete())
        completer = QCompleter(result, self)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        return completer
        
    