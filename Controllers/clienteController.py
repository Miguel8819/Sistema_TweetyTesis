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
from datetime import date


class ClienteController():
    def __init__(self, create_cliente):
        self.cliente = Cliente(connection())
        self.create_cliente = create_cliente
        
        

    def exito(self, Ui_Dialog, Form):
        self.create_cliente.Form = QtWidgets.QWidget()
        self.create_cliente.ui = Ui_Dialog()
        self.create_cliente.ui.setupUi(self.create_cliente.Form)
        self.create_cliente.Form.show()
        Form.show()
        
    def createCliente(self, nombreCliente, nroDni, calle, nroCalle, ciudad, codPostal, tel, email):
     if nroDni:

        fechaAlta= date.today()  
        
        result = self.cliente.getCliente(nroDni, '1')
        
        if result:
            msg = QMessageBox()
            msg.setWindowTitle("Exito")
            msg.setText("El cliente ya existe")
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
                
                    if  nombreCliente and nroDni  and ciudad  and tel:
                        self.cliente.insertCliente(nombreCliente, nroDni, fechaAlta, calle, nroCalle, ciudad, codPostal, tel, email)

                            
                        msg = QMessageBox()
                        msg.setWindowTitle("Exito")
                        msg.setText("Cliente guardado")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("")
                        x = msg.exec_()

                        self.create_cliente.input_nameclient.clear()
                        self.create_cliente.input_dni.clear()
                        self.create_cliente.input_calle.clear()
                        self.create_cliente.input_numCalle.clear()
                        self.create_cliente.input_codPostal.clear()
                        self.create_cliente.input_tel.clear()
                        self.create_cliente.input_email.clear()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Por favor complete los campos obligatorios")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_()


                    


    def showCliente(self,nroDni):
        if nroDni:
            
                result = self.cliente.getCliente(nroDni, '1')
                if result:
                    self.create_cliente.show_nameCliente.setText(str(result[2]))
                    self.create_cliente.show_Dni.setText(str(result[1]))
                    
                    self.create_cliente.show_calle.setText(str(result[4]))
                    self.create_cliente.show_numCalle.setText(str(result[5]))
                    self.create_cliente.show_ciudad.setCurrentText(str(result[6]))
                    self.create_cliente.show_codPostal.setText(str(result[7]))
                    self.create_cliente.show_tel.setText(str(result[8]))
                    self.create_cliente.show_email.setText(str(result[9]))

                else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El numero de DNI no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un numero de DNI valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

    def showCliente_2(self,nroDni):
        if nroDni:
            result = self.cliente.getCliente(nroDni, '1')
            if result:
                self.create_cliente.show_nameCliente_2.setText(str(result[2]))
                self.create_cliente.show_Dni_2.setText(str(result[1]))
                
                self.create_cliente.show_calle_2.setText(str(result[4]))
                self.create_cliente.show_numCalle_2.setText(str(result[5]))
                self.create_cliente.show_ciudad_2.setCurrentText(str(result[6]))
                self.create_cliente.show_codPostal_2.setText(str(result[7]))
                self.create_cliente.show_tel_2.setText(str(result[8]))
                self.create_cliente.show_email_2.setText(str(result[9]))

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El numero de DNI no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un numero de DNI valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 
            

    def bajaCliente(self,cliente,nroDni):
        if nroDni:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea dar de baja al cliente? ")
            msgBox.setWindowTitle("Baja de cliente")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
            
                
                if cliente :
                        

                        self.cliente.bajaCliente(nroDni)

                msg = QMessageBox()
                msg.setWindowTitle("Confirmado")
                msg.setText("Cliente dado de baja de la lista")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_() 

            self.create_cliente.show_nameCliente_2.clear()
            self.create_cliente.show_Dni_2.clear()
            self.create_cliente.show_calle_2.clear()
            self.create_cliente.show_numCalle_2.clear()
            self.create_cliente.show_codPostal_2.clear()
            self.create_cliente.show_tel_2.clear()
            self.create_cliente.show_email_2.clear()

          

        else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un numero de DNI valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

                
    def modificarCliente(self, CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta ):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea guardar los cambios del producto? ")
        msgBox.setWindowTitle("")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
                    if producto != "" and cant_min_stock !="" and PuntoDePedido !="" and CostoDeCompra != "" and PrecioDeVenta !="":
                        self.product.UpdateProduct(CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta)

                        msg = QMessageBox()
                        msg.setWindowTitle("Confirmado")
                        msg.setText("Cambios guardados")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("")
                        x = msg.exec_() 

                        
                        self.create_product.input_prod_2.clear()
                        self.create_product.input_searchcod.clear()
                        self.create_product.input_cantMinStock_2.clear()
                        self.create_product.input_puntoPedido_2.clear()
                        self.create_product.input_costCompra_2.clear()
                        self.create_product.input_precVenta_2.clear()

                    else: 
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Hay campos vacios")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_() 


    def cancelar(self, Ui_cliente):

        Ui_cliente.close()


    