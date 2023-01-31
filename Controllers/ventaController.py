import os
from fpdf import FPDF
import sys
import os
from this import s
from tkinter import CURRENT
from tokenize import Number
from datetime import datetime
myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Product import Product
from Models.venta import Venta
from Models.cliente import *
from Models.cabeceraFactura import CabeceraFactura
from Controllers.menuprincipalController import menuprincipalController
from Models.User import User
from Controllers import globales

class ventaController():
    
    idCliente = 0
    
    

    def __init__(self, venta,):
        self.product = Product(connection())
        self.venta = venta
        self.menu = menuprincipalController(connection())
        self.Venta = Venta(connection())
        self.Facturacion = CabeceraFactura(connection())
        self.cliente= Cliente(connection())
        self.user=User(connection())
        print(globales.logueado)
        
        self.usuario = globales.logueado    
    
    def open2(self, Ui_venta):
        self.venta.Form = QtWidgets.QWidget()
        self.venta.ui = Ui_venta()
        self.venta.ui.setupUi(self.venta.Form)
        self.venta.Form.show()   
    

    def buscarCliente(self,nroDni):
        if nroDni:
                result=self.cliente.getCliente(nroDni, '1')
                if result:
                    
                    self.idCliente = result[0]
                    self.venta.input_nombre.setText(str(result[2]))
                    self.venta.input_direccion.setText(str(result[4]))
                    self.venta.input_nroCalle.setText(str(result[5]))
                    self.venta.input_localidad.setText(str(result[6]))       
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El DNI ingresado no existe.")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese un numero de DNI.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 
            
    def aceptar(self, Ui_venta, CodigoDeBarras, cantidad,nombre,stock,precio1,subtotal):
        if cantidad:
            cantidad= int(cantidad)
            if CodigoDeBarras and (cantidad > 0) :             
                table = self.venta.table_venta
                product = self.product.getProduct(CodigoDeBarras, '1')
                if product:
                    if cantidad <= product[8]:
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
                            table.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(str(product[12])))  # price

                            cantidad = int(table.item(rowCount, 2).text())
                            precio = float(table.item(rowCount, 4).text())
                            subtotal = cantidad*precio

                            table.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(str(subtotal)))  # subtotal
                            table.setItem(rowCount, 6, QtWidgets.QTableWidgetItem(str(product[8])))  # stock
                        
                            stock=int(table.item(rowCount, 6).text())
                            self.stockdisponible=stock - cantidad
                           
                        #-------------------------------------------------- 
                        
                            self.venta.input_codprod.setText(str(product[0]))
                            self.venta.input_cantidad.setText(str(cantidad))
                            self.venta.input_producto.setText(str(product[2]))
                            self.venta.input_precio.setText(str(product[12]))
                            self.venta.input_stock.setText(str(product[8]))
                            self.venta.input_subtotal.setText(str(subtotal))
                            self.venta.input_codprod.clear()
                            self.venta.input_producto.clear()
                            self.venta.input_cantidad.clear()
                            self.calcular_subtotal()
                            self.calcular_importe(Ui_venta,neto=any,descuento=any,importe=any)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("La cantidad ingresada es mayor al stock disponible.")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El código de barras no existe.")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_()
            elif nombre and (cantidad > 0) :
                table = self.venta.table_venta
                producto = self.product.getProduct_2(nombre, '1')
                if producto:   
                    if cantidad <= producto[8]:
                        if table.rowCount() == 50:
                            rowCount = 0
                            table.setRowCount(1)
                        else:
                            rowCount = table.rowCount()
                            table.setRowCount(table.rowCount() + 1)
                        table.setItem(rowCount, 0, QtWidgets.QTableWidgetItem(str(producto[0])))
                        table.setItem(rowCount, 1, QtWidgets.QTableWidgetItem(str(producto[1])))  # codBarras
                        table.setItem(rowCount, 2, QtWidgets.QTableWidgetItem(str(cantidad)))  # cant
                        table.setItem(rowCount, 3, QtWidgets.QTableWidgetItem(producto[2]))  # name
                        table.setItem(rowCount, 4, QtWidgets.QTableWidgetItem(str(producto[12])))  # price

                        cantidad = int(table.item(rowCount, 2).text())
                        precio = float(table.item(rowCount, 4).text())
                        subtotal = cantidad*precio

                        table.setItem(rowCount, 5, QtWidgets.QTableWidgetItem(str(subtotal)))  # subtotal
                        table.setItem(rowCount, 6, QtWidgets.QTableWidgetItem(str(producto[8])))  # stock
                        stock=int(table.item(rowCount, 6).text())
                        self.stockdisponible=stock - cantidad
                        print (self.stockdisponible)
                    #-------------------------------------------------- 
                    
                        self.venta.input_codprod.setText(str(producto[0]))
                        self.venta.input_cantidad.setText(str(cantidad))
                        self.venta.input_producto.setText(str(producto[2]))
                        self.venta.input_precio.setText(str(producto[12]))
                        self.venta.input_stock.setText(str(producto[8]))
                        self.venta.input_subtotal.setText(str(subtotal))
                        self.venta.input_codprod.clear()
                        self.venta.input_producto.clear()
                        self.venta.input_cantidad.clear()
                        
                        self.calcular_subtotal()
                        self.calcular_importe(Ui_venta,neto=any,descuento=any,importe=any)
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("La cantidad ingresada es mayor al stock disponible.")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_()
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
                if not CodigoDeBarras or nombre:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Ingrese un codigo de producto o nombre de producto.")
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
        neto += float(table.item(i,5).text())

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

    def remover (self,Ui_venta):  
            table = self.venta.table_venta
            if table.currentItem() != None:        
            
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
        self.venta.input_codprod.clear()
        self.venta.input_cantidad.clear()
        self.venta.input_nroCalle.clear()

    def finalizar (self, Ui_venta):
          
        fecha= datetime.now()
        fechaFactura= datetime.now().strftime("%d/%m/%Y")
        cabecera = 0
      
        table = self.venta.table_venta  
        if fecha and self.idCliente: #Validar todo
            if self.venta.input_importe.text() != '':
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea finalizar la venta? ")
                msgBox.setWindowTitle("Finalizar Venta")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:     
                    cabecera = self.Facturacion.insertCabeceraFactura(fecha, self.idCliente,self.usuario[0])
                    for  i in range(table.rowCount()):
                        # datelle de factura
                        CodProducto = table.item(i,0).text()
                        CodigoDeBarras = table.item(i,1).text()
                        cantidad = table.item(i,2).text()
                        producto = table.item(i,3).text()
                        precio = table.item(i,4).text()
                        condicionPago = self.venta.comboBox_pago.currentText()         
                        
                        if  cabecera  and CodProducto and cantidad and precio and condicionPago: 
                            self.Venta.insertVenta(cabecera, CodProducto, cantidad, precio, condicionPago)
                            self.product.descontarStock(cantidad,CodigoDeBarras)
                            product = self.product.getStockBajo()
        
                            if product:
                                msg = QMessageBox()
                                msg.setWindowTitle("Notificación")
                                msg.setText("Tiene productos con stock bajo.")
                                msg.setIcon(QMessageBox.Information)
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.setDefaultButton(QMessageBox.Ok)
                                msg.setInformativeText("Informar al encargado de stock.")
                                x = msg.exec_()

                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("¿Desea imprimir el comprobante de venta? ")
                    msgBox.setWindowTitle("")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    returnValue = msgBox.exec()
                    if returnValue == QMessageBox.Ok: 
                        lista_datos = []
                        for  i in range(table.rowCount()):    
                            lista_datos.append(( table.item(i,3).text(),table.item(i,2).text(), table.item(i,4).text(),table.item(i,5).text()))

                        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
                        pdf.set_margins(20, 10 , 10)
                        pdf.set_auto_page_break(10)
                        pdf.add_page()
                        # TEXTO
                        
                        pdf.set_font('Arial', '', 48)
                        # titulo
                        pdf.cell(w = 0, h = 7, txt = '', border = 0, ln=1,
                                align = 'C', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = 'X', border = 0, ln=1,
                                align = 'C', fill = 0)
                        pdf.set_font('Arial', '', 10)
                        pdf.cell(w = 0, h = 10, txt = 'Documento no válido como factura', border = 0, ln=1,
                                align = 'C', fill = 0)
                        pdf.image('Imagenes/twetestudi.jpg' , 100 ,35, 25 , 25,'JPG') 

                        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                                align = 'C', fill = 0)
                        pdf.set_font('Times', '', 28)
                        pdf.cell(w = 50, h = 5, txt = 'Libreria Tweety', border = 0, ln=1,
                                align = 'L', fill = 0)
                        pdf.set_font('Arial', '', 12)
                        pdf.cell(w = 0, h = 7, txt ='Recibo N°: 0002-0000000'+ str(cabecera) , border = 0, ln=1,
                                align = 'R', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = 'Articulos escolares y comerciales', border = 0, ln=0,
                                align = 'L', fill = 0)
                        pdf.cell(w = 0, h = 5, txt ='Fecha de emision: '+str(fechaFactura) , border = 0, ln=1,
                                align = 'R', fill = 0)
                        pdf.set_font('Arial', '', 8)
                        pdf.cell(w = 60, h = 5, txt = 'de PEÑA DANIEL ALBERTO', border = 0, ln=1,
                                align = 'C', fill = 0)
                        pdf.set_font('Arial', '', 12)
                        pdf.cell(w = 0, h = 5, txt = 'Roque S. Peña 203 - Loc. A', border = 0, ln=0,
                                align = 'L', fill = 0)
                        pdf.cell(w = 0, h = 5, txt ='CUIT: 20318688800' , border = 0, ln=1,
                                align = 'R', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = 'Tel: (03543) 15 531652', border = 0, ln=0,
                                align = 'L', fill = 0)
                        pdf.cell(w = 0, h = 5, txt ='Inicio de Actividades: 01/10/2021', border = 0, ln=1,
                                align = 'R', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = '5158 BIALET MASSE - CORDOBA', border = 0, ln=0,
                                align = 'L', fill = 0)
                        
                        pdf.cell(w = 0, h = 5, txt ='Ingresos Brutos: 286436927', border = 0, ln=1,
                                align = 'R', fill = 0)
                        
                        pdf.cell(w = 0, h = 5, txt = 'RESPONSABLE MONOTRIBUTO', border = 0, ln=1,
                                align = 'L', fill = 0)

                        pdf.cell(w = 0, h = 10, txt = '', border = 0, ln=1,
                                align = 'C', fill = 0)
                        pdf.cell(w = 0, h = 1, txt = '', border = 1, ln=1,
                                align = 'C', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                                align = 'C', fill = 0)
                        
                        pdf.cell(w = 0, h = 5, txt = 'Cliente: '+ str(self.venta.input_nombre.text()), border = 0, ln=0,
                                align = 'L', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = 'Cond. IVA: ' + str(self.venta.comboBox_iva.currentText()), border = 0, ln=1,
                                align = 'R', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = 'Domicilio: ' + str(self.venta.input_direccion.text()+' '+ str(self.venta.input_nroCalle.text()+' - '+ str (self.venta.input_localidad.text()))), border = 0, ln=0,
                                align = 'L', fill = 0)

                        pdf.cell(w = 0, h = 5, txt = 'Cond. Pago: '+ str(self.venta.comboBox_pago.currentText()), border = 0, ln=1,
                                align = 'R', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                                align = 'C', fill = 0)
                        pdf.cell(w = 0, h = 1, txt = '', border = 1, ln=1,
                                align = 'C', fill = 0)
                        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                                align = 'C', fill = 0)

                        # encabezado

                        pdf.cell(w = 90, h = 7, txt = 'Descripción', border = 1,
                                align = 'C', fill = 0)
                        pdf.cell(w = 20, h = 7, txt = 'Cantidad', border = 1,
                                align = 'C', fill = 0)
                        pdf.cell(w = 40, h = 7, txt = 'Precio Unitario', border = 1,
                                align = 'C', fill = 0)
                        pdf.multi_cell(w = 0, h = 7, txt = 'Subtotal', border = 1,
                                align = 'C', fill = 0)
                        
                        # valores
                        for valor in lista_datos:
                                pdf.set_font('Arial', '', 10)    
                                pdf.cell(w = 90, h = 5, txt = str(valor[0]), border = 0,
                                        align = 'C', fill = 0)
                                pdf.cell(w = 20, h = 5, txt = str(valor[1]), border = 0,
                                        align = 'C', fill = 0)
                                pdf.cell(w = 40, h = 5, txt ='$' + str(valor[2] + '.00'), border = 0,
                                        align = 'C', fill = 0)
                                pdf.multi_cell(w = 0, h = 5, txt ='$' + str (valor[3] +'0'), border = 0,
                                        align = 'C', fill = 0)
                      
                        pdf.set_font('Arial', '', 12)
                        
                        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                        align = 'C', fill = 0)
                        pdf.cell(w = 0, h = 7, txt = 'Subtotal: $' + str(self.venta.input_neto.text()), border = 0, ln=1,
                                align = 'R', fill = 0) 
                        pdf.cell(w = 0, h = 7, txt = 'Descuento:' + str(self.venta.descuento_valor.text()), border = 0, ln=1,
                                align = 'R', fill = 0) 
                        pdf.cell(w = 0, h = 7, txt = 'Importe Total: $' + str(self.venta.input_importe.text()), border = 0, ln=1,
                                align = 'R', fill = 0)  
                        pdf.cell(w = 0, h = 5, txt = 'Gracias por su compra!', border = 1, ln=1,
                                align = 'C', fill = 0)
                        
                                    
                        pdf.output('comprobanteVenta.pdf')
                        os.startfile('comprobanteVenta.pdf') 
                                                 
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
                        self.venta.input_nroCalle.clear()
                    
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("¡Exito!")
                        msg.setText("Venta Finalizada.")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("")
                        x = msg.exec_()
                       
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
                        self.venta.input_nroCalle.clear()

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("No ha ingresado productos.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Debe ingresar el DNI del cliente.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()     

    
        
        
             
    

    
        
        
             

        
