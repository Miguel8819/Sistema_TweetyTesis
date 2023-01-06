import sys
import os

from Controllers.menuprincipalController import *

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import connection
from Models.Product import Product
from fpdf import FPDF
from datetime import datetime

class controlstockController():

    def __init__(self, controlstock):
        self.product = Product(connection())
        self.controlstock = controlstock
    
    def listProducts(self):
        table = self.controlstock.table_product
        products = self.product.getProducts()
        table.setRowCount(0)
        for row_number, row_data in enumerate(products):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))    
      
    def updateProducs(self):
        table = self.controlstock.table_product
        products = []
        fila = []
        for row_number in range(table.rowCount()):
            for column_number in range(table.columnCount()):
                if table.item(row_number,column_number) != None:
                    fila.append(table.item(row_number,column_number).text())
            if len(fila)>0:
                products.append(fila)
            fila = []
        
        if len(products)>0:
            for prod in products:
                self.product.UpdateProduct(prod[0],prod[1],prod[2],prod[3],prod[4],prod[5],prod[6],prod[7],prod[8],prod[9],prod[10],prod[11])
        
        
        self.listProducts()
    
    def deleteProduct(self):
        table = self.controlstock.table_product
        if table.currentItem() != None:
            CodigoDeBarras = table.currentItem().text()
            product = self.product.getProduct(CodigoDeBarras)
            if product:
                self.product.deleteProduct(CodigoDeBarras)
        self.listProducts()


    def listarProductosActivos(self):
        table = self.controlstock.table_product
        productos = self.product.getProductosActivos()
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def listarBajaProductos(self):
        table = self.controlstock.table_product_2
        productos = self.product.getProductosBaja()
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def darAltaProducto(self):
        table = self.controlstock.table_product_2      
        if table.currentItem() != None:
            CodigoDeBarras = table.currentItem().text()  
            product = self.product.getProduct(CodigoDeBarras, '0')
            if product:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea dar de alta al producto? ")
                msgBox.setWindowTitle("Confirmacion")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    self.product.altaProducto(CodigoDeBarras)                
                    self.listarBajaProductos()

                    msg = QMessageBox()
                    msg.setWindowTitle('¡Exito!')
                    msg.setText("¡Producto dado de alta!.")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('¡Error!')
                msg.setText("Seleccione el código de barras del producto y luego presione el boton Dar de Alta.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Seleccione el código de barras del producto para dar el alta.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

    
    def openCreate(self, Ui_CreateProduct):
        self.controlstock.Form = QtWidgets.QWidget()
        self.controlstock.ui = Ui_CreateProduct()
        self.controlstock.ui.setupUi(self.controlstock.Form)
        self.controlstock.Form.show()

    def modifyProduct(self, Ui_MainWindow):
        table = self.controlstock.table_product
        if table.currentItem() != None:
            cod = table.currentItem().text()
            self.controlstock.Form = QtWidgets.QMainWindow()
            self.controlstock.ui = Ui_MainWindow(cod)
            self.controlstock.ui.setupUi(self.controlstock.Form)
            self.controlstock.Form.show()
            product = self.product.getProduct(cod)
        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("No hay selección realizada")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("¡Seleccione un item para modificar!")
                x = msg.exec_()

    def buscarProductoActivo(self,codigoDeBarras,nombre):
        table = self.controlstock.table_product
        if codigoDeBarras:
            productos = self.product.buscarProductoXcodigo(codigoDeBarras)
            if productos:
                
                table.setRowCount(0)
                for row_number, row_data in enumerate(productos):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El código de producto no existe")

                msg.setIcon(QMessageBox.Information)

                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")

                x = msg.exec_()
            
        elif nombre:
            producto = self.product.buscarProductoXnombre(nombre)
            if producto:
                
                table.setRowCount(0)
                for row_number, row_data in enumerate(producto):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El nombre de producto no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese el código o nombre del producto")

            msg.setIcon(QMessageBox.Information)

            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")

            x = msg.exec_()

    def buscarProductoBaja(self,codigoDeBarras,nombre):
        table = self.controlstock.table_product_2
        if codigoDeBarras:
            productos1 = self.product.buscarProductoXcodigoB(codigoDeBarras)
            if productos1:
                
                table.setRowCount(0)
                for row_number, row_data in enumerate(productos1):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El código no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()

        elif nombre:
            producto1 = self.product.buscarProductoXnombreB(nombre)
            if producto1:
                
                table.setRowCount(0)
                for row_number, row_data in enumerate(producto1):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El nombre del producto no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese el código o nombre del producto")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def limpiar (self):
        self.controlstock.table_product.setRowCount(0)
        self.controlstock.input_codigo.clear()
        self.controlstock.input_prod.clear()

    def limpiar_2 (self):
        self.controlstock.table_product_2.setRowCount(0)
        self.controlstock.input_codigo_2.clear()
        self.controlstock.input_prod_2.clear()

    def listarStockActivos(self):
        table = self.controlstock.table_product
        productos = self.product.getStockActivos()
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                

    def listarBajoStock(self):
        table = self.controlstock.table_product_2
        productos = self.product.getStockBajo()
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def buscarStockBajo(self,codigoDeBarras,nombre):
        table = self.controlstock.table_product_2
        if codigoDeBarras:
            productos1 = self.product.buscarProductoBajoStock(codigoDeBarras)
            if productos1:
                
                table.setRowCount(0)
                for row_number, row_data in enumerate(productos1):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El código no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()

        elif nombre:
            producto1 = self.product.buscarNombreBajoStock(nombre)
            if producto1:
                
                table.setRowCount(0)
                for row_number, row_data in enumerate(producto1):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El nombre del producto no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese el código o nombre del producto")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def imprimirLista(self):
        fecha= datetime.now()
        fechaLista= datetime.now().strftime("%d/%m/%Y-%H:%M")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea imprimir la lista? ")
        msgBox.setWindowTitle("")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok: 
            table = self.controlstock.table_product_2   
            lista_datos = []
            for  i in range(table.rowCount()):    
                lista_datos.append(( table.item(i,2).text(),table.item(i,3).text(), table.item(i,4).text(), table.item(i,5).text()))
            pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
            pdf.set_margins(20, 10 , 10)
            pdf.set_auto_page_break(25)
            pdf.add_page()
            # TEXTO
            pdf.set_font('Arial', '', 15)
            pdf.cell(w = 0, h = 7, txt = 'Lista de productos bajos en Stock', border = 1, ln=1,
                                    align = 'C', fill = 0)
            pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                    align = 'C', fill = 0)
            pdf.set_font('Times', '', 28)
            pdf.cell(w = 50, h = 10, txt = 'Libreria Tweety', border = 0, ln=0,
                    align = 'L', fill = 0)
            pdf.set_font('Times', '', 20)
            pdf.cell(w = 0, h = 10, txt = 'Fecha: '+ str(fechaLista), border = 0, ln=1,
                    align = 'R', fill = 0)
            pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                    align = 'C', fill = 0)
            pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                    align = 'C', fill = 0)
            pdf.set_font('Arial', '', 16)
            pdf.cell(w = 50, h = 7, txt = 'Producto', border = 1,
                                    align = 'C', fill = 0)
            pdf.cell(w = 30, h = 7, txt = 'Marca', border = 1,
                    align = 'C', fill = 0)
            pdf.cell(w = 40, h = 7, txt = 'Stock Actual', border = 1,
                    align = 'C', fill = 0)
            pdf.multi_cell(w = 0, h = 7, txt = 'Punto de Pedido', border = 1,
                    align = 'C', fill = 0)
            # valores
            
            for valor in lista_datos:
                    pdf.set_font('Arial', '', 12)    
                    pdf.cell(w = 50, h = 7, txt = str(valor[0]), border = 0,
                            align = 'C', fill = 0)
                    pdf.cell(w = 30, h = 7, txt = str(valor[1]), border = 0,
                            align = 'C', fill = 0)
                    pdf.cell(w = 40, h = 7, txt = str(valor[2]), border = 0,
                            align = 'C', fill = 0)
                    pdf.multi_cell(w = 0, h = 7, txt =str(valor[3]), border = 0,
                            align = 'C', fill = 0)                        
                  
                 
            
            
            pdf.output('listaStockBajo.pdf')
            os.startfile('listaStockBajo.pdf') 

    
    

    def salir(self, controlstock):
        controlstock.close()