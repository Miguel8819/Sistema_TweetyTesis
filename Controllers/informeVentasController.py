import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.venta import Venta
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QStringListModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QMessageBox


class listarVentas():
    def __init__(self, listar_VentasDiarias):
        self.venta = Venta(connection())
        self.listar_ventasDiarias = listar_VentasDiarias
       

    def listarVentas(self):
        table = self.listar_ventasDiarias.tableWidget
        ventasDiarias = self.venta.ventasDiarias()
           
        table.setRowCount(0)
        for row_number, row_data in enumerate(ventasDiarias):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def detalleVenta(self):
        table = self.listar_ventasDiarias.tableWidget_3
        ventasDiarias = self.venta.detalleVentas()
           
        table.setRowCount(0)
        for row_number, row_data in enumerate(ventasDiarias):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))