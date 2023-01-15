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
            cliente = self.cliente.getCliente(nroDni, '0')
                    
            if cliente:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea dar de alta al cliente? ")
                msgBox.setWindowTitle("Confirmacion")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    self.cliente.altaCliente(nroDni)                
                    self.listarBajaClientes()

                    msg = QMessageBox()
                    msg.setWindowTitle('¡Exito!')
                    msg.setText("¡Cliente dado de alta!.")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('¡Error!')
                msg.setText("Seleccione el número de dni del ciente y luego presione el boton Dar de Alta.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Seleccione el número de DNI del cliente para dar el alta.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()


    def SalirA(self,listar_cliente):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea salir?")
        msgBox.setWindowTitle("Lista de clientes")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
           listar_cliente.close()