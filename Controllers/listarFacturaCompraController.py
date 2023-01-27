import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import connection
from Models.facturaCompra import FacturaCompra
from Views.detallefacturacompra_ui import Ui_detallefacturacompra

class listarFacturaCompraController():
    def __init__(self, lista_factCompra):
        self.FactCompra = FacturaCompra(connection())
        self.lista_factCompra = lista_factCompra
        self.detalleFact = Ui_detallefacturacompra


    def buscarFactNombreProv(self, nameProv):
        table = self.lista_factCompra.tableWidget
        facturas = self.FactCompra.getFactByProv(nameProv)
        table.setRowCount(0)
        for row_number, row_data in enumerate(facturas):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def buscarFactNumFact(self, numFact):
        table = self.lista_factCompra.tableWidget
        facturas = self.FactCompra.getFactByNum(numFact)
        table.setRowCount(0)
        for row_number, row_data in enumerate(facturas):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def llenarDetalleFactura(self, nroFact):
        self.FactCompra.getDetalleFactura(nroFact)
        self.FactCompra.getDetalleTablaFactura(nroFact)

    def openDetalleFactura(self, Ui_detallefacturacompra, Form):
        table = self.lista_factCompra.tableWidget
        nrofact = table.currentItem().text() 
        print(nrofact)
        factura = self.FactCompra.getDetalleFactura(nrofact)
        print (factura)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea ver detalle de la factura seleccionada?")
        msgBox.setWindowTitle("Abrir Detalle Factura")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.lista_factCompra.Form = QtWidgets.QWidget()
            self.lista_factCompra.ui = Ui_detallefacturacompra()
            self.lista_factCompra.ui.setupUi(self.lista_factCompra.Form)
            self.lista_factCompra.Form.show()
            Form.show()
            print(type(self.detalleFact.input_provFact.setText(str(factura[0][2]))))


    def Salir(self,lista_factCompra):
        lista_factCompra.close()

            