import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Proveedores import Proveedor
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QStringListModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QMessageBox


class listarProveedoresController():
    def __init__(self, listar_proveedor):
        self.proveedores = Proveedor(connection())
        self.listar_proveedor = listar_proveedor
       

    def listarProveedoresActivos(self):
        table = self.listar_proveedor.tableWidget
        proveedor = self.proveedores.getProveedoresActivos()
        table.setRowCount(0)
        for row_number, row_data in enumerate(proveedor):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def listarBajaProveedores(self):
        table = self.listar_proveedor.tableWidget_2
        proveedor = self.proveedores.getProveedoresBaja()
        table.setRowCount(0)
        for row_number, row_data in enumerate(proveedor):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def darAltaProveedor(self):
        table = self.listar_proveedor.tableWidget_2      
        if table.currentItem() != None:
            nombreProveedor = table.currentItem().text()
            proveedor = self.proveedores.getProveedor(nombreProveedor, '0')
            
                
            if proveedor:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea dar de alta al proveedor? ")
                msgBox.setWindowTitle("Confirmacion")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                
                if returnValue == QMessageBox.Ok:
                    self.proveedores.altaProveedor(nombreProveedor)                
                    self.listarBajaProveedores()

                    msg = QMessageBox()
                    msg.setWindowTitle('¡Exito!')
                    msg.setText("¡Proveedor dado de alta!.")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('¡Error!')
                msg.setText("Seleccione el nombre del proveedor y luego presione el boton Dar de Alta.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()

        else: 
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Seleccione el nombre del proveedor para dar el alta.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

    def SalirA(self,listar_proveedor):
         listar_proveedor.close()