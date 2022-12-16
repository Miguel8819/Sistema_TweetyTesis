import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.Proveedores import *
from Models.Product import Product
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from PyQt5 import QtWidgets

class facturaCompraController():
    def __init__(self, factura_compra):
        self.proveedor = Proveedor(connection())
        self.product = Product(connection())
        self.factura_compra = factura_compra

    def buscarProv(self,nameProv):
        if nameProv:
                result = self.proveedor.getProveedor(nameProv, '1')
                if result:
                    
                    self.factura_compra.input_nroCuil.setText(str(result[1]))
                         
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El Proveedor ingresado no existe.")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese un Proveedor valido")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 

    def aceptar(self, CodigoDeBarras, cantidad, precio):

            if CodigoDeBarras and (cantidad > '0') and (precio > '0'):
                            
                table = self.factura_compra.table_venta
                product = self.product.getProduct(CodigoDeBarras, '1')
                if product:
                    if table.rowCount() == 50:
                        rowCount = 0
                        table.setRowCount(1)
                    else:
                        rowCount = table.rowCount()
                        table.setRowCount(table.rowCount() + 1)

                    
                    table.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(product[0])))
                    table.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(product[1])))  # codBarras
                    table.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(cantidad)))  # cant
                    table.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(product[2]))  # name
                    table.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(str(product[11])))  # price
                    table.setItem(rowCount, 6, QtWidgets.QTableWidgetItem(str(product[8])))  # stock

                #-------------------------------------------------- 
                   
                    self.factura_compra.input_codprod.setText(str(product[0]))
                    self.factura_compra.input_cantidad.setText(str(cantidad))
                    self.factura_compra.input_precio.setText(str(product[11]))
                    self.factura_compra.input_codprod.clear()
                    self.factura_compra.input_cantidad.clear()

                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El producto ingresado no existe.")

                    msg.setIcon(QMessageBox.Information)

                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")

                    x = msg.exec_()
            else:
                if not CodigoDeBarras :
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Ingrese un codigo de producto.")

                    msg.setIcon(QMessageBox.Information)

                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")

                    x = msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Ingrese una cantidad válida.")

                    msg.setIcon(QMessageBox.Information)

                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")

                    x = msg.exec_()

    def guardar():
        pass

    def cancelar(self, Ui_FacturaCompra):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cancelar la carga de Factura de compra y salir? Los datos no se guardaran")
        msgBox.setWindowTitle("Cancelar Carga")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            Ui_FacturaCompra.close()