import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from Database.Connection import connection
from Models.Product import Product
from PyQt5.QtWidgets import QMessageBox

class CreateProductController():
    def __init__(self, create_product):
        self.product = Product(connection())
        self.create_product = create_product

    def createProduct(self,CodigoDeBarras,producto, categoria, subCategoria, marca,tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta,CreateProduct):
     if CodigoDeBarras:
            
        result = self.product.getProduct(CodigoDeBarras)
        print(result)
        if result:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("ya existe")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()
                    
        else:   
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Desea guardar los datos? ")
                msgBox.setWindowTitle("Confirmacion")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                        
                    if CodigoDeBarras and producto and categoria and subCategoria and marca and tipoUnidad and unidadMedida and cant_min_stock and PuntoDePedido and CostoDeCompra and PrecioDeVenta :
                        self.product.insertProduct(CodigoDeBarras, producto, categoria, subCategoria, marca,tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta)
                        msg = QMessageBox()
                        msg.setWindowTitle('¡Exito!')
                        msg.setText("¡Producto Guardado exitosamente!.")

                        msg.setIcon(QMessageBox.Information)

                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                            

                        x = msg.exec_()
                                    
                        self.create_product.input_prod.clear()
                        self.create_product.input_cod.clear()
                        self.create_product.input_cantMinStock.clear()
                        self.create_product.input_puntoPedido.clear()
                        self.create_product.input_costCompra.clear()
                        self.create_product.input_precVenta.clear()

                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle("Error")
                        msg.setText("Hay campos vacios")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        msg.setInformativeText("Vuelva a intentarlo")
                        x = msg.exec_()     
                        
                                            


    def salir(self, CreateProduct):
        CreateProduct.close()