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
                        
    def showProduct(self,CodigoDeBarras,producto, categoria, subCategoria, marca,tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        if CodigoDeBarras:
            
                result = self.product.getProduct(CodigoDeBarras)
                if result:
                    self.create_product.input_prod_2.setText(str(result[2]))
                    self.create_product.box_cat_2.setCurrentText(str(result[3]))
                    self.create_product.box_subCat_2.setCurrentText(str(result[4]))
                    self.create_product.box_marca_2.setCurrentText(str(result[5]))
                    self.create_product.box_tipoUnid_2.setCurrentText(str(result[6]))
                    self.create_product.box_uniMedi_2.setCurrentText(str(result[7]))
                    self.create_product.input_cantMinStock_2.setText(str(result[8]))
                    self.create_product.input_puntoPedido_2.setText(str(result[9]))
                    self.create_product.input_costCompra_2.setText(str(result[10]))
                    self.create_product.input_precVenta_2.setText(str(result[11]))
                else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El código de barras no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
                    
                    self.create_product.input_prod_2.clear()
                    self.create_product.input_cod_2.clear()
                    self.create_product.input_cantMinStock_2.clear()
                    self.create_product.input_puntoPedido_2.clear()
                    self.create_product.input_costCompra_2.clear()
                    self.create_product.input_precVenta_2.clear()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un código de barras valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

                self.create_product.input_prod_2.clear()
                self.create_product.input_cod_2.clear()
                self.create_product.input_cantMinStock_2.clear()
                self.create_product.input_puntoPedido_2.clear()
                self.create_product.input_costCompra_2.clear()
                self.create_product.input_precVenta_2.clear()

    def showProduct_2(self,CodigoDeBarras,producto, categoria, subCategoria, marca,tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        if CodigoDeBarras:
            
                result = self.product.getProduct(CodigoDeBarras)
                if result:
                    self.create_product.input_prod_3.setText(str(result[2]))
                    self.create_product.box_cat_3.setCurrentText(str(result[3]))
                    self.create_product.box_subCat_3.setCurrentText(str(result[4]))
                    self.create_product.box_marca_3.setCurrentText(str(result[5]))
                    self.create_product.box_tipoUnid_3.setCurrentText(str(result[6]))
                    self.create_product.box_uniMedi_3.setCurrentText(str(result[7]))
                    self.create_product.input_cantMinStock_3.setText(str(result[8]))
                    self.create_product.input_puntoPedido_3.setText(str(result[9]))
                    self.create_product.input_costCompra_3.setText(str(result[10]))
                    self.create_product.input_precVenta_3.setText(str(result[11]))
                else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El código de barras no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un código de barras valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

    def darBajaProducto(self,product,CodigoDeBarras,producto, categoria, subCategoria, marca,tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        if CodigoDeBarras:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea dar de baja al producto? ")
            msgBox.setWindowTitle("Baja de producto")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
            
                
                if product :
                        

                        self.product.bajaProducto(CodigoDeBarras)

                msg = QMessageBox()
                msg.setWindowTitle("Confirmado")
                msg.setText("Producto dado de baja de la lista")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("")
                x = msg.exec_() 

            self.create_product.input_prod_3.clear()
            self.create_product.input_searchcod_2.clear()
            self.create_product.input_cantMinStock_3.clear()
            self.create_product.input_puntoPedido_3.clear()
            self.create_product.input_costCompra_3.clear()
            self.create_product.input_precVenta_3.clear()

          

        else: 
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un código de barras valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 

    def showProduct(self,CodigoDeBarras,producto, categoria, subCategoria, marca,tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        if CodigoDeBarras:
            
                result = self.product.getProduct(CodigoDeBarras)
                if result:
                    self.create_product.input_prod_2.setText(str(result[2]))
                    self.create_product.box_cat_2.setCurrentText(str(result[3]))
                    self.create_product.box_subCat_2.setCurrentText(str(result[4]))
                    self.create_product.box_marca_2.setCurrentText(str(result[5]))
                    self.create_product.box_tipoUnid_2.setCurrentText(str(result[6]))
                    self.create_product.box_uniMedi_2.setCurrentText(str(result[7]))
                    self.create_product.input_cantMinStock_2.setText(str(result[8]))
                    self.create_product.input_puntoPedido_2.setText(str(result[9]))
                    self.create_product.input_costCompra_2.setText(str(result[10]))
                    self.create_product.input_precVenta_2.setText(str(result[11]))
                else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El código de barras no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
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
                msg.setText("Ingrese un código de barras valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 
                self.create_product.input_prod_2.clear()
                self.create_product.input_searchcod.clear()
                self.create_product.input_cantMinStock_2.clear()
                self.create_product.input_puntoPedido_2.clear()
                self.create_product.input_costCompra_2.clear()
                self.create_product.input_precVenta_2.clear()

    def showProduct_2(self,CodigoDeBarras,producto, categoria, subCategoria, marca,tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        if CodigoDeBarras:
            
                result = self.product.getProduct(CodigoDeBarras)
                if result:
                    self.create_product.input_prod_3.setText(str(result[2]))
                    self.create_product.box_cat_3.setCurrentText(str(result[3]))
                    self.create_product.box_subCat_3.setCurrentText(str(result[4]))
                    self.create_product.box_marca_3.setCurrentText(str(result[5]))
                    self.create_product.box_tipoUnid_3.setCurrentText(str(result[6]))
                    self.create_product.box_uniMedi_3.setCurrentText(str(result[7]))
                    self.create_product.input_cantMinStock_3.setText(str(result[8]))
                    self.create_product.input_puntoPedido_3.setText(str(result[9]))
                    self.create_product.input_costCompra_3.setText(str(result[10]))
                    self.create_product.input_precVenta_3.setText(str(result[11]))
                else: 
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("El código de barras no existe")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_() 
                    self.create_product.input_prod_3.clear()
                    self.create_product.input_searchcod_2.clear()
                    self.create_product.input_cantMinStock_3.clear()
                    self.create_product.input_puntoPedido_3.clear()
                    self.create_product.input_costCompra_3.clear()
                    self.create_product.input_precVenta_3.clear()

        else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Ingrese un código de barras valido")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_() 
                self.create_product.input_prod_3.clear()
                self.create_product.input_searchcod_2.clear()
                self.create_product.input_cantMinStock_3.clear()
                self.create_product.input_puntoPedido_3.clear()
                self.create_product.input_costCompra_3.clear()
                self.create_product.input_precVenta_3.clear()

    def modificarProducto(self, CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta ):
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


            

              


    def salir(self, CreateProduct):
        CreateProduct.close()