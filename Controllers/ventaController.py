from ipaddress import summarize_address_range
from locale import currency
import numbers
from re import sub
from sqlite3 import Row
import sys
import os
from this import s
from tkinter import CURRENT
from tokenize import Number
from datetime import datetime
from unittest import result

from Models.cabeceraFactura import CabeceraFactura


from PyQt5.QtWidgets import QApplication, QDialog,QDialogButtonBox, QLabel, QPushButton
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets,QtCore,QtGui
from Database.Connection import connection
from Models.Product import Product
from Models.venta import Venta
from Models.cliente import *

class ventaController():
    
    idCliente = 0
    
    

    def __init__(self, venta):
        self.product = Product(connection())
        self.venta = venta
        self.Venta = Venta(connection())
        self.Facturacion = CabeceraFactura(connection())
        self.cliente= Cliente(connection())
        


    def open2(self, Ui_venta):
        self.venta.Form = QtWidgets.QWidget()
        self.venta.ui = Ui_venta()
        self.venta.ui.setupUi(self.venta.Form)
        self.venta.Form.show()   

       



    def buscarCliente(self,nroDni,nombreCliente,calle,ciudad):
        if nroDni:
            result=self.cliente.getCliente(nroDni, '1')
            self.idCliente = result[0]
            print(self.idCliente)
            self.venta.input_nombre.setText(str(result[2]))
            self.venta.input_direccion.setText(str(result[4]))
            self.venta.input_localidad.setText(str(result[6]))       


    def aceptar(self, Ui_venta, CodigoDeBarras, cantidad,nombre,precio1,subtotal,stock):

            if CodigoDeBarras and (cantidad > '0') :
                            
                table = self.venta.table_venta
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

                    cantidad = float(table.item(rowCount, 2).text())
                    precio = float(table.item(rowCount, 4).text())
                    subtotal = cantidad*precio

                    table.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(str(subtotal)))  # subtotal

                    table.setItem(rowCount, 6, QtWidgets.QTableWidgetItem(str(product[8])))  # stock

                #-------------------------------------------------- 
                   
                    self.venta.input_codprod.setText(str(product[0]))
                    self.venta.input_cantidad.setText(str(cantidad))
                    self.venta.input_producto.setText(str(product[2]))
                    self.venta.input_precio.setText(str(product[11]))
                    self.venta.input_stock.setText(str(product[8]))
                    self.venta.input_subtotal.setText(str(subtotal))
                    self.venta.input_codprod.clear()
                    self.venta.input_cantidad.clear()
                    
                    self.calcular_subtotal()
                    self.calcular_importe(Ui_venta,neto=any,descuento=any,importe=any)
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
        
                



    def cancelar(self, Ui_venta):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cancelar la venta y salir? ")
        msgBox.setWindowTitle("Cancelar Venta")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            Ui_venta.close()


    def calcular_subtotal (self):

      table = self.venta.table_venta

      neto=0

      for  i in range(table.rowCount()):
        neto += float(table.item(i,4).text())

      self.venta.input_neto.setText(str(neto))

    

    def calcular_importe(self, Ui_venta,neto,descuento,importe):
        if  neto and descuento:
            
                currency='$ '
                neto = float(self.venta.input_neto.text())        
             
                descuento =  (neto * (float(self.venta.input_descuento.text())) / 100)
            
                importe= neto-descuento
                descuento_valor= neto - importe

                self.venta.descuento_valor.setText(currency + str(descuento_valor))
                self.venta.input_importe.setText(str(importe))    
            
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
   
    def calcular_pago(self, Ui_venta, efectivo, total):
      
      if efectivo and total:
        
            currency= '$ '
            total = float(self.venta.input_importe.text())
            efectivo= float(self.venta.input_efectivo.text())
            cambio= efectivo - total
            self.venta.input_cambio.setText(currency + str(cambio))
            self.venta.input_total.setText( currency + str(total))
       
      else:
         if not efectivo:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese una cantidad de efectivo.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()  
         else:
            
            
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El campo importe esta vacio")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()    

    def remover (self,Ui_venta,importe):
        
        
        
            if importe > '0.0':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea quitar el producto de la lista? ")
                msgBox.setWindowTitle("Remover producto")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    
                    self.venta.table_venta.removeRow(self.venta.table_venta.currentRow())
                    self.calcular_subtotal()
                    self.calcular_importe(Ui_venta=any,descuento=any,neto=any,importe=any)
                
                    self.venta.input_cambio.clear()
                    self.venta.input_total.clear()
                    self.venta.input_producto.clear()
                    self.venta.input_stock.clear()
                    self.venta.input_precio.clear()
                    self.venta.input_subtotal.clear()
        
                
              
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La tabla esta vacia")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 
        
        
    def limpiar_venta(self, Ui_venta):
     msgBox = QMessageBox()
     msgBox.setIcon(QMessageBox.Information)
     msgBox.setText("¿Desea limpiar la pantalla de ventas? ")
     msgBox.setWindowTitle("Limpiar Venta")
     msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
     returnValue = msgBox.exec()
     if returnValue == QMessageBox.Ok:
        self.venta.table_venta.setRowCount(0)
        self.venta.input_importe.clear()
        self.venta.input_neto.clear()
        self.venta.input_efectivo.clear()
        self.venta.input_cambio.clear()
        self.venta.input_total.clear()
        descuento= '0'
        self.venta.input_descuento.setText(str(descuento))
        self.venta.descuento_valor.clear()
        self.venta.input_producto.clear()
        self.venta.input_stock.clear()
        self.venta.input_precio.clear()
        self.venta.input_subtotal.clear()
        self.venta.input_nroDni.clear()
        self.venta.input_nombre.clear()
        self.venta.input_direccion.clear()
        self.venta.input_localidad.clear()

    def finalizar (self, Ui_venta):
     msgBox = QMessageBox()
     msgBox.setIcon(QMessageBox.Information)
     msgBox.setText("¿Desea finalizar la venta? ")
     msgBox.setWindowTitle("Finalizar Venta")
     msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
     returnValue = msgBox.exec()
     if returnValue == QMessageBox.Ok:

        fecha= datetime.now()
        
        if fecha and self.idCliente:
             self.Facturacion.insertCabeceraFactura(fecha, self.idCliente)

        
        print(datetime.now())
        cabecera=1
        # validaciones
    # guardar cabecera y recuperar el Id 
      
        table = self.venta.table_venta     
        
        for  i in range(table.rowCount()):
            # datelle de factura
            CodProducto = table.item(i,0).text()
            CodigoDeBarras = table.item(i,1).text()
            cantidad = table.item(i,2).text()
            producto = table.item(i,3).text()
            precio = table.item(i,4).text()
            
            
           
            if  cabecera  and CodProducto and cantidad and precio: 
                self.Venta.insertVenta(cabecera, CodProducto, cantidad, precio) 
                
        msg = QMessageBox()
        msg.setWindowTitle('Venta Finalizada')
        msg.setText("¡Venta Guardada exitosamente!.")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()
        
        self.limpiar_venta(Ui_venta)
       


        # idCabecera = 1

        # cada dato que quieras guardar
        # llamar al insert pasandole los datos que recuperaste de la tabla arriba


      
