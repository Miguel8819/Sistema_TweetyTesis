import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.Proveedores import *
from Models.Product import Product
from Models.facturaCompra import FacturaCompra
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from PyQt5 import QtWidgets
from locale import currency

class facturaCompraController():
    def __init__(self, factura_compra):
        self.proveedor = Proveedor(connection())
        self.product = Product(connection())
        self.facturaCompra = FacturaCompra(connection())
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

    def aceptar(self, CodigoDeBarras, cantidad, precio, subtotal):

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

                    
                    table.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(product[0]))) # codProd
                    table.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(product[1])))  # codBarras
                    table.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(product[2]))  # name
                    table.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(str(cantidad)))  # cant
                    table.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(str(precio)))  # price

                    self.factura_compra.input_codprod.clear()
                    self.factura_compra.input_cantidad.clear()
                    self.factura_compra.input_precio.clear()

                    cantidad = int(table.item(rowCount, 3).text())
                    precio = float(table.item(rowCount, 4).text())
                    subtotal = cantidad*precio

                    table.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(str(subtotal)))  # subtotal

                    self.factura_compra.input_subtotal.setText(str(subtotal))

                    self.calcular_subtotal()
                    self.calcular_iva()
                    self.calcular_importe(neto=any,descuento=any,importe=any)

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

    def guardar(self, tipoDoc, nombreProv, nroFactCompra, nroCuil, fechaEmision, tipoCompra, subtotal, descuento, iva, importeTotal):
        table = self.factura_compra.table_venta
        fechaNow = datetime.now()
        fechaIngreso = datetime.strftime(fechaNow, '%d/%m/%Y %H:%M:%S')
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea guardar factura de compra?")
        msgBox.setWindowTitle("")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            if tipoDoc and nombreProv and nroFactCompra and nroCuil and fechaEmision and fechaIngreso and subtotal and descuento and iva and importeTotal:
                self.facturaCompra.insertFactCompra(tipoDoc, nombreProv, nroFactCompra, nroCuil, fechaEmision, fechaIngreso, tipoCompra, subtotal, descuento, iva, importeTotal)
                for i in range(table.rowCount()):
                    CodProducto = table.item(i,0).text()
                    CodigoDeBarras = table.item(i,1).text()
                    producto = table.item(i,2).text()
                    stock = table.item(i,3).text()
                    precio = table.item(i,4).text()
                    subtotalTabla = table.item(i,5).text()
                    self.facturaCompra.insertTabla(nroFactCompra, nroCuil, fechaIngreso, CodProducto, CodigoDeBarras, producto, stock, precio, subtotalTabla)
                msg = QMessageBox()
                msg.setWindowTitle("Confirmado")
                msg.setText("Factura de Compra guardada")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_() 
        

    def cancelar(self, Ui_FacturaCompra):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cancelar la carga de Factura de compra y salir? Los datos no se guardaran")
        msgBox.setWindowTitle("Cancelar Carga")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            Ui_FacturaCompra.close()


    def calcular_subtotal(self):
        table = self.factura_compra.table_venta
        neto = 0
        for i in range(table.rowCount()):
            neto += float(table.item(i,5).text())

        self.factura_compra.input_subtotal.setText(str(neto))

    def calcular_iva(self):
        subtotal = float(self.factura_compra.input_subtotal.text())
        porcentajeIva = 0.21
        iva = subtotal * porcentajeIva
        self.factura_compra.input_iva.setText(str(iva))

    def calcular_importe(self,neto,descuento,importe):
        if  neto and descuento:
            
                currency ='$ '
                neto = float(self.factura_compra.input_subtotal.text())        
             
                descuento = (neto * (float(self.factura_compra.input_descuento.text())) / 100)
            
                importe = neto - descuento
                descuento_valor = neto - importe

                iva = float(self.factura_compra.input_iva.text())

                importeFinal = importe + iva

                self.factura_compra.input_descuento_2.setText(str(descuento_valor))
                self.factura_compra.input_importe.setText(str(importeFinal))      
            
        else:
            if not neto:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El campo 'neto' esta vacio.")

                msg.setIcon(QMessageBox.Information)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")

                x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un descuento válido.")

                msg.setIcon(QMessageBox.Information)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")

                x = msg.exec_() 


    def remover (self,importe):     
            if importe > '0.0':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea quitar el producto de la lista? ")
                msgBox.setWindowTitle("Remover producto")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    
                    self.factura_compra.table_venta.removeRow(self.factura_compra.table_venta.currentRow())
                    self.calcular_subtotal()
                    self.calcular_iva()
                    #self.calcular_importe(Ui_venta=any,descuento=any,neto=any,importe=any)
        
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La tabla esta vacia")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 