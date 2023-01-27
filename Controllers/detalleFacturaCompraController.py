import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import connection
from Models.facturaCompra import FacturaCompra

class detalleFacturaCompraController():
    def __init__(self, detalle_factCompra):
        self.factCompra = FacturaCompra(connection())
        self.detalle_factCompra = detalle_factCompra


    def buscarFactNombreProv(self, nameProv):
        table = self.detalle_factCompra.tableWidget
        facturas = self.factCompra.getFactByProv(nameProv)
        table.setRowCount(0)
        for row_number, row_data in enumerate(facturas):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def buscarFactNumFact(self, numFact):
        table = self.detalle_factCompra.tableWidget
        facturas = self.factCompra.getFactByNum(numFact)
        table.setRowCount(0)
        for row_number, row_data in enumerate(facturas):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def openDetalleFactura(self):
        try:
            table = self.detalle_factCompra.tableWidget
            nrofact = table.currentItem().text()
        except: 
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No ha seleccionado un numero de factura de la tabla")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 
        else:    
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea ver detalle de la factura seleccionada?")
            msgBox.setWindowTitle("Abrir Detalle Factura")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                factura = self.factCompra.getDetalleFactura(nrofact)
                detalle_factura = self.factCompra.getDetalleTablaFactura(nrofact)
                if factura and detalle_factura:
                    self.detalle_factCompra.input_facCompra.setText(str(factura[0][1]))
                    self.detalle_factCompra.input_provFact.setText(str(factura[0][2]))
                    self.detalle_factCompra.input_nroFac.setText(str(factura[0][3]))
                    self.detalle_factCompra.input_nroCuil.setText(str(factura[0][4]))
                    self.detalle_factCompra.input_fechaEmision.setText(str(factura[0][5]))
                    self.detalle_factCompra.input_fechaEmision_2.setText(str(factura[0][6]))
                    self.detalle_factCompra.input_tipoCompra.setText(str(factura[0][7]))
                    self.detalle_factCompra.input_subtotal.setText(str(factura[0][8]))
                    self.detalle_factCompra.input_descuento_2.setText(str(factura[0][9]))
                    self.detalle_factCompra.input_iva.setText(str(factura[0][10]))
                    self.detalle_factCompra.input_importe.setText(str(factura[0][11]))

                    table_detalle = self.detalle_factCompra.table_venta
                    table_detalle.setRowCount(0)
                    for row_number, row_data in enumerate(detalle_factura):
                        table_detalle.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table_detalle.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



    def Salir(self,lista_factCompra):
        lista_factCompra.close()

