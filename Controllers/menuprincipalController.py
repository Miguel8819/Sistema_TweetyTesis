import sys
import os
import threading

myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5 import QtWidgets
from Models.Product import Product


class menuprincipalController():

   def __init__(self, menuprincipal):
     self.menuprincipal = menuprincipal
     self.product= Product
     

   def openFacturacion(self, Ui_venta, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_venta()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 
   
   def openProveedores(self, Ui_proveedores, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_proveedores()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 

   def openCreateProduct(self, Ui_CreateProduct, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_CreateProduct()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 

   def openListaProductos(self, Ui_listaDeProductos, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_listaDeProductos()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show()

   def openClientes(self, Ui_cliente, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_cliente()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show()  
  
   def openListaClientes(self, Ui_lista_clientes, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_lista_clientes()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 

   def openGestionClaves(self, Ui_gestion_claves, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_gestion_claves()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 

   def openGestionBackup(self, Ui_gestion_backup, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_gestion_backup()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 

   def openListaProveedores(self, Ui_lista_proveedores, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_lista_proveedores()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show()   

   def openInformeDeVentas(self, Ui_informeDeVentas, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_informeDeVentas()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show()  

   def openFacturaCompra(self, Ui_facturaCompra, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_facturaCompra()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show()  
   
   def openControlStock(self, Ui_controlDeStock, Form):
     self.menuprincipal.Form = QtWidgets.QWidget()
     self.menuprincipal.ui = Ui_controlDeStock()
     self.menuprincipal.ui.setupUi(self.menuprincipal.Form)
     self.menuprincipal.Form.show()
     Form.show() 

   def manualUsuario(self):
      os.startfile('ManualDeUsuarioSistemaTweety.pdf')  

   def time(self):
        product = self.product.getStockBajo()
        
        if product:
                self.menuprincipal.alarma1.show()
                self.menuprincipal.alarma2.show()
                
        else:
                self.menuprincipal.alarma1.hide()
                self.menuprincipal.alarma2.hide()
   t = threading.Timer(3,time)
   t.start()     

