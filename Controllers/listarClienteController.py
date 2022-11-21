import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.cliente import Cliente
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QStringListModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QMessageBox


class listarClienteController():
    def __init__(self, listar_cliente):
        self.cliente = Cliente(connection())
        self.listar_cliente = listar_cliente
       

    def listarClientesActivos(self):
        table = self.listar_cliente.tableWidget
        clientes = self.cliente.getClientesActivos()
        table.setRowCount(0)
        for row_number, row_data in enumerate(clientes):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def listarBajaClientes(self):
        table = self.listar_cliente.tableWidget_2
        clientes = self.cliente.getClientesBaja()
        table.setRowCount(0)
        for row_number, row_data in enumerate(clientes):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def darAltaCliente(self):
       table = self.listar_cliente.tableWidget_2
       if table.currentItem() != None:
            nroDni = table.currentItem().text()
            print(nroDni)
            product = self.cliente.getCliente(nroDni, '0')
            print(product)
            if product:
                self.cliente.altaCliente(nroDni)                
            self.listarBajaClientes()
        

    def SalirA(self,listar_cliente):
         listar_cliente.close()