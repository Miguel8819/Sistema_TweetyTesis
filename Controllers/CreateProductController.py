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

    def createProduct(self,producto,CodigoDeBarras,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta, categoria, subCategoria, marca,tipoUnidad,unidadMedida,CreateProduct):
        if   producto and CodigoDeBarras and cant_min_stock and PuntoDePedido and CostoDeCompra and PrecioDeVenta and categoria and subCategoria and marca and tipoUnidad and unidadMedida:
            self.product.insertProduct(producto,CodigoDeBarras,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta, categoria, subCategoria, marca,tipoUnidad,unidadMedida)
            msg = QMessageBox()
            msg.setWindowTitle('¡Exito!')
            msg.setText("¡Producto Guardado exitosamente!.")

            msg.setIcon(QMessageBox.Information)

            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
       

            x = msg.exec_()
            
            self.create_product.input_prod.clear()
            self.create_product.input_codBarra.clear()
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
            


    def borrar(self):
        self.create_product.input_prod.clear()
        
        self.create_product.input_codBarra.clear()
        self.create_product.input_cantMinStock.clear()
        self.create_product.input_puntoPedido.clear()
        self.create_product.input_costCompra.clear()
        self.create_product.input_precVenta.clear()

    def salir(self, CreateProduct):
        CreateProduct.close()