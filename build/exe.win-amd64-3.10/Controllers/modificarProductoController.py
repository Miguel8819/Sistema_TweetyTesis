import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Product import Product

class modificarProductoController():

    def __init__(self, modificar):
        self.product = Product(connection())
        self.modificar = modificar

    def modificarProducto(self, CodigoDeBarras):
        
        self.product.modificarProduct(CodigoDeBarras,self.modificar.input_prod.text(),
        self.modificar.input_cantMinStock.text(),self.modificar.input_puntoPedido.text(),
        self.modificar.input_costCompra.text(),self.modificar.input_precVenta.text())
 
    def borrar(self):
        self.modificar.input_prod.clear()
        self.modificar.input_cantMinStock.clear()
        self.modificar.input_puntoPedido.clear()
        self.modificar.input_costCompra.clear()
        self.modificar.input_precVenta.clear()
    
    def salir(self, ModificarProducto):
        ModificarProducto.close()

        product = self.product.getProduct(self.input_codBarra)