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
            print(nombreProveedor)
            proveedor = self.proveedores.getProveedor(nombreProveedor, '0')
            print(proveedor)
            if proveedor:
                self.proveedores.altaProveedor(nombreProveedor)                
            self.listarBajaProveedores()
        

    def SalirA(self,listar_proveedor):
         listar_proveedor.close()