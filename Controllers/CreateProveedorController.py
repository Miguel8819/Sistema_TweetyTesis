import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Proveedores import *
from PyQt5.QtWidgets import QMessageBox
from datetime import datetime
from Models.Product import Product
from Controllers import globales

class CreateProveedorController():
    def __init__(self, create_proveedor):
        self.proveedor = Proveedor(connection())
        self.create_proveedor = create_proveedor
        self.product = Product(connection())
        self.usuario= globales.logueado[0]

    def createProveedor(self,  nombreProveedor, nombreFactura,nroCuil, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb):
        if nombreProveedor and nombreFactura and nroCuil and celular:
            fechaAlta1= datetime.now()
            fechaAlta= datetime.strftime(fechaAlta1, '%d/%m/%Y %H:%M:%S')
            result = self.proveedor.getProveedor(nombreProveedor, '1')      
            if result:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El proveedor ya existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_()

            else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Information)
                    msgBox.setText("¿Desea guardar los datos? ")
                    msgBox.setWindowTitle("Confirmacion")
                    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    returnValue = msgBox.exec()
                    if returnValue == QMessageBox.Ok:
                        
                        if nroCuil and nombreProveedor and nombreFactura and fechaAlta and celular :
                            self.proveedor.insertProveedor(nroCuil,nombreProveedor,nombreFactura,fechaAlta,calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb,self.usuario)

                            msg = QMessageBox()
                            msg.setWindowTitle("Exito")
                            msg.setText("Proveedor guardado")
                            msg.setIcon(QMessageBox.Information)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("")
                            x = msg.exec_()

                            self.create_proveedor.input_nameProv.clear()
                            self.create_proveedor.input_nameFact.clear()
                            self.create_proveedor.input_nroCuil.clear()
                            self.create_proveedor.input_calle.clear()
                            self.create_proveedor.input_numCalle.clear()
                            self.create_proveedor.input_codPostal.clear()
                            self.create_proveedor.input_tel.clear()
                            self.create_proveedor.input_email.clear()
                            self.create_proveedor.input_web.clear()
                        else:
                            msg = QMessageBox()
                            msg.setWindowTitle("Exito")
                            msg.setText("Proveedor guardado")
                            msg.setIcon(QMessageBox.Information)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("")
                            x = msg.exec_()

                            self.create_proveedor.input_nameProv.clear()
                            self.create_proveedor.input_nameFact.clear()
                            self.create_proveedor.input_nroCuil.clear()
                            self.create_proveedor.input_calle.clear()
                            self.create_proveedor.input_numCalle.clear()
                            self.create_proveedor.input_codPostal.clear()
                            self.create_proveedor.input_tel.clear()
                            self.create_proveedor.input_email.clear()
                            self.create_proveedor.input_web.clear()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Complete los campos obligatorios")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("")
            x = msg.exec_()     

    def showProveedor(self,nombreProveedor):
        if nombreProveedor:
            result = self.proveedor.getProveedor(nombreProveedor, '1')
            if result:
                self.create_proveedor.show_nroCuil.setText(str(result[1]))
                self.create_proveedor.show_nameProv.setText(str(result[2]))
                self.create_proveedor.show_nameFact.setText(str(result[3]))
                self.create_proveedor.show_calle.setText(str(result[5]))
                self.create_proveedor.show_numCalle.setText(str(result[6]))
                self.create_proveedor.show_ciudad.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal.setText(str(result[8]))
                self.create_proveedor.show_tel.setText(str(result[9]))
                self.create_proveedor.show_email.setText(str(result[10]))
                self.create_proveedor.show_web.setText(str(result[11]))
                self.create_proveedor.input_searchNameProv.clear()
                self.showProductos(nombreProveedor)
                
            else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El nombre de proveedor no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
                    
                    self.create_proveedor.input_searchNameProv.clear()
                    self.create_proveedor.show_nameProv.clear()
                    self.create_proveedor.show_nameFact.clear()                         
                    self.create_proveedor.show_calle.clear()
                    self.create_proveedor.show_numCalle.clear()
                    self.create_proveedor.show_nroCuil.clear()
                    self.create_proveedor.show_codPostal.clear()
                    self.create_proveedor.show_tel.clear()
                    self.create_proveedor.show_email.clear()
                    self.create_proveedor.show_web.clear()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un nombre de proveedor válido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

                self.create_proveedor.show_nameProv.clear()
                self.create_proveedor.show_nameFact.clear()                
                self.create_proveedor.show_calle.clear()
                self.create_proveedor.show_numCalle.clear()
                self.create_proveedor.show_codPostal.clear()
                self.create_proveedor.show_tel.clear()
                self.create_proveedor.show_email.clear()
                self.create_proveedor.show_web.clear()

    def buscarProveedor(self,nroCuit):
        if nroCuit:
            result = self.proveedor.getProveedor_2(nroCuit, '1')
            if result:
                self.create_proveedor.show_nroCuil.setText(str(result[1]))
                self.create_proveedor.show_nameProv.setText(str(result[2]))
                self.create_proveedor.show_nameFact.setText(str(result[3]))
                self.create_proveedor.show_calle.setText(str(result[5]))
                self.create_proveedor.show_numCalle.setText(str(result[6]))
                self.create_proveedor.show_ciudad.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal.setText(str(result[8]))
                self.create_proveedor.show_tel.setText(str(result[9]))
                self.create_proveedor.show_email.setText(str(result[10]))
                self.create_proveedor.show_web.setText(str(result[11]))

                self.create_proveedor.input_searchNameFact.clear()
            else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El número de Cuit/Cuil no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
                    
                    self.create_proveedor.input_searchNameProv.clear()
                    self.create_proveedor.show_nameProv.clear()
                    self.create_proveedor.show_nameFact.clear()
                    self.create_proveedor.show_calle.clear()
                    self.create_proveedor.show_numCalle.clear()
                    self.create_proveedor.show_nroCuil.clear()
                    self.create_proveedor.show_codPostal.clear()
                    self.create_proveedor.show_tel.clear()
                    self.create_proveedor.show_email.clear()
                    self.create_proveedor.show_web.clear()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un número de Cuit/Cuil válido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

                self.create_proveedor.show_nameProv.clear()
                self.create_proveedor.show_nameFact.clear()                    
                self.create_proveedor.show_calle.clear()
                self.create_proveedor.show_numCalle.clear()
                self.create_proveedor.show_codPostal.clear()
                self.create_proveedor.show_tel.clear()
                self.create_proveedor.show_email.clear()
                self.create_proveedor.show_web.clear()
                
    def showProveedor_2(self,nombreProveedor):
        if nombreProveedor:
            result = self.proveedor.getProveedor(nombreProveedor, '1')
            if result:
                self.create_proveedor.show_nroCuil_2.setText(str(result[1]))
                self.create_proveedor.show_nameProv_2.setText(str(result[2]))
                self.create_proveedor.show_nameFact_2.setText(str(result[3]))
                self.create_proveedor.show_calle_2.setText(str(result[5]))
                self.create_proveedor.show_numCalle_2.setText(str(result[6]))
                self.create_proveedor.show_ciudad_2.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal_2.setText(str(result[8]))
                self.create_proveedor.show_tel_2.setText(str(result[9]))
                self.create_proveedor.show_email_2.setText(str(result[10]))
                self.create_proveedor.show_web_2.setText(str(result[11]))

              
            else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El nombre de proveedor no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese un proveedor valido")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 

    def buscarProveedor_2(self,nroCuit):
        if nroCuit:
            result = self.proveedor.getProveedor_2(nroCuit, '1')
            if result:
                self.create_proveedor.show_nroCuil_2.setText(str(result[1]))
                self.create_proveedor.show_nameProv_2.setText(str(result[2]))
                self.create_proveedor.show_nameFact_2.setText(str(result[3]))
                self.create_proveedor.show_calle_2.setText(str(result[5]))
                self.create_proveedor.show_numCalle_2.setText(str(result[6]))
                self.create_proveedor.show_ciudad_2.setCurrentText(str(result[7]))
                self.create_proveedor.show_codPostal_2.setText(str(result[8]))
                self.create_proveedor.show_tel_2.setText(str(result[9]))
                self.create_proveedor.show_email_2.setText(str(result[10]))
                self.create_proveedor.show_web_2.setText(str(result[11]))   

            else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El número de Cuit/Cuil no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese un número de Cuit/Cuil valido")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def showProductos(self,nombre):

        table = self.create_proveedor.tablaProductos
        productos = self.product.productosDeProveedorXnombreProv(nombre)
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def quitarProductos(self):
            table = self.create_proveedor.tablaProductos
            if table.currentItem() != None:    
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea quitar el producto de la lista? ")
                msgBox.setWindowTitle("Remover producto")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    
                    self.create_proveedor.tablaProductos.removeRow(self.create_proveedor.tablaProductos.currentRow())
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("La tabla esta vacia")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_()         

    def deleteProduct(self):
        table = self.create_proveedor.tablaProductos
        if table.currentItem() != None:
            nombre = table.currentItem().text()
            product = self.product.productosDeProveedorXnombreProv(nombre)
            if product:
                self.product.deleteProductxProveedor(nombre)
        self.listProducts()



    def openAgregarProducto(self, Ui_AgregarProducto,Form):
        self.create_proveedor.Form = QtWidgets.QWidget()
        self.create_proveedor.ui = Ui_AgregarProducto()
        self.create_proveedor.ui.setupUi(self.create_proveedor.Form)
        self.create_proveedor.Form.show()
        Form.show() 
    
    def verProductos(self):
        table = self.create_proveedor.tableWidget
        productos = self.product.productosParaAgregar()
        table.setRowCount(0)
        for row_number, row_data in enumerate(productos):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def ingresarProductoaProveedor (self):
        table = self.create_proveedor.tableWidget
        if table.currentItem() != None:
            codProducto = table.currentItem().text()        
            prod = self.product.AgregarxCod(codProducto)
                    
            if prod:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea agregar este producto al proveedor? ")
                msgBox.setWindowTitle("Confirmacion")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                        self.product.insertProductoaProveedor(codProducto) 
                        msg = QMessageBox()
                        msg.setWindowTitle('¡Exito!')
                        msg.setText("¡Producto agregado!.")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        x = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('¡Error!')
                msg.setText("Seleccione el codProducto y luego presione el boton Agregar.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Seleccione el codProducto para agregar un producto.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()
    


    


    def darBajaProveedor(self,proveedores,nombreProveedor,cuil):
        fechaBaja1= datetime.now()
        fechaBaja= datetime.strftime(fechaBaja1, '%d/%m/%Y %H:%M:%S')
        if nombreProveedor:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea dar de baja al proveedor?")
            msgBox.setWindowTitle("Baja de proveedor")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:   
                if proveedores :                      
                        self.proveedor.bajaProveedor(nombreProveedor,fechaBaja,self.usuario)
                msg = QMessageBox()
                msg.setWindowTitle("Confirmado")
                msg.setText("Proveedor dado de baja de la lista")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_() 
                self.create_proveedor.input_searchNameProv_2.clear()
                self.create_proveedor.show_nameProv_2.clear()
                self.create_proveedor.show_nameFact_2.clear()
                self.create_proveedor.show_calle_2.clear()
                self.create_proveedor.show_numCalle_2.clear()
                self.create_proveedor.show_nroCuil_2.clear()
                self.create_proveedor.show_codPostal_2.clear()
                self.create_proveedor.show_tel_2.clear()
                self.create_proveedor.show_email_2.clear()
                self.create_proveedor.show_web_2.clear()
        elif cuil: 
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea dar de baja al proveedor? ")
            msgBox.setWindowTitle("Baja de proveedor")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:  
                if proveedores :                      
                        self.proveedor.bajaProveedor2(cuil,fechaBaja,self.usuario)
                msg = QMessageBox()
                msg.setWindowTitle("Confirmado")
                msg.setText("Proveedor dado de baja de la lista")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_() 
                self.create_proveedor.input_searchNameProv_2.clear()
                self.create_proveedor.show_nameProv_2.clear()
                self.create_proveedor.show_nameFact_2.clear()              
                self.create_proveedor.show_calle_2.clear()
                self.create_proveedor.show_numCalle_2.clear()
                self.create_proveedor.show_nroCuil_2.clear()
                self.create_proveedor.show_codPostal_2.clear()
                self.create_proveedor.show_tel_2.clear()
                self.create_proveedor.show_email_2.clear()
                self.create_proveedor.show_web_2.clear()
                self.create_proveedor.input_searchNameFact_2.clear()
        else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un nombre de proveedor o número de Cuit/Cuil valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

    def modificarProveedor(self,nombreProveedor, nombreFactura, nroCuil, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb ):
        if nombreProveedor or nroCuil: 
            
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea guardar los cambios del proveedor? ")
            msgBox.setWindowTitle("")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                        if nombreProveedor != "" and nombreFactura !="" and calle !="" and numeroCalle != ""  and codPostal != "" and celular != "" and email != "" and pagWeb != "":
                            self.proveedor.UpdateProveedor(nroCuil,nombreProveedor, nombreFactura, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb)

                            msg = QMessageBox()
                            msg.setWindowTitle("Confirmado")
                            msg.setText("Cambios guardados")
                            msg.setIcon(QMessageBox.Information)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("")
                            x = msg.exec_() 

                            self.create_proveedor.input_searchNameProv.clear()
                            self.create_proveedor.show_nameProv.clear()

                            self.create_proveedor.show_nameFact.clear()
                            self.create_proveedor.show_ciudad.setCurrentText('Alta Gracia') 

                            self.create_proveedor.show_nameFact.clear()              
                            self.create_proveedor.show_calle.clear()
                            self.create_proveedor.show_numCalle.clear()
                            self.create_proveedor.show_nroCuil.clear()
                            self.create_proveedor.show_codPostal.clear()
                            self.create_proveedor.show_tel.clear()
                            self.create_proveedor.show_email.clear()
                            self.create_proveedor.show_web.clear()

                        else: 
                            msg = QMessageBox()
                            msg.setWindowTitle("Error")
                            msg.setText("Hay campos vacios")
                            msg.setIcon(QMessageBox.Information)
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setDefaultButton(QMessageBox.Ok)
                            msg.setInformativeText("Vuelva a intentarlo")
                            x = msg.exec_() 
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Ingrese un nombre de proveedor o número de CUIL o CUIT válidos")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 

    def cancelar(self, Ui_Proveedores):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea cancelar y salir?")
        msgBox.setWindowTitle("Proveedores")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:

            Ui_Proveedores.close()