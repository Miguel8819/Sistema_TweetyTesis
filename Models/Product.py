from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Product():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS product
                        (
                        codProducto INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,    
                        CodigoDeBarras VARCHAR(45) NOT NULL,
                        producto VARCHAR(45) NOT NULL,
                        categoria VARCHAR(45) NOT NULL,
                        subCategoria VARCHAR(45) NOT NULL,
                        marca VARCHAR(45) NOT NULL,
                        tipoUnidad VARCHAR(45) NOT NULL,
                        unidadDeMedida VARCHAR(45) NOT NULL,
                        stock INT(45) NOT NULL,
                        cant_min_stock INT(45) NOT NULL,
                        PuntoDePedido INT(45) NOT NULL,
                        CostoDeCompra VARCHAR(45) NOT NULL,
                        PrecioDeVenta VARCHAR(45) NOT NULL,
                        activo BOOLEAN NOT NULL
                        
                        )"""
            cursor.execute(sql)
            self.conn.commit()

            # TABLA PRODUCTO POR PROVEEDOR
#______________________________________________________________________________________________________

        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS productoxproveedor
                        (
                        codProducto INT(10) NOT NULL,    
                        codProveedor INT(10) NOT NULL,
                        precio INT(10) NOT NULL
                        )"""
            cursor.execute(sql)
            self.conn.commit()

#______________________________________________________________________________________________________

    
    def getProducts(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getProduct(self, CodigoDeBarras, estado):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product WHERE CodigoDeBarras = %s AND activo = %s"""
            cursor.execute(sql,(CodigoDeBarras,estado))
            result = cursor.fetchone()
            if result:
                return result
    
    def getProduct_2(self, nombre, estado):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product WHERE producto = %s AND activo = %s"""
            cursor.execute(sql,(nombre,estado))
            result = cursor.fetchone()
            if result:
                return result
    
    def insertProduct(self,CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        with self.conn.cursor() as cursor:
            activo = 1
            sql = """INSERT INTO product (CodigoDeBarras,producto,categoria,subCategoria,marca,tipoUnidad,UnidadDeMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta, activo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta,activo))
            self.conn.commit()

    def UpdateProduct(self,CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        with self.conn.cursor() as cursor:
            
            sql = """UPDATE product SET  producto = %s,categoria = %s,subCategoria = %s,marca = %s,tipoUnidad = %s,UnidadDeMedida = %s,cant_min_stock = %s,PuntoDePedido = %s,CostoDeCompra = %s,PrecioDeVenta = %s WHERE CodigoDeBarras = %s """
            cursor.execute(sql,(producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta,CodigoDeBarras))
            self.conn.commit()
                
    def bajaProducto(self,CodigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """UPDATE Product SET activo = "0" WHERE CodigoDeBarras = %s"""
            cursor.execute(sql, CodigoDeBarras)
            self.conn.commit()

    def altaProducto(self,CodigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """UPDATE Product SET activo = "1" WHERE CodigoDeBarras = %s"""
            cursor.execute(sql, CodigoDeBarras)
            self.conn.commit()

    def getProductosActivos(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM Product WHERE activo = '1' """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getProductosBaja(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto,CodigoDeBarras,producto,categoria,subCategoria,marca,tipoUnidad,UnidadDeMedida,stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta
            FROM Product 
            WHERE activo = '0' """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def buscarProductoXcodigo(self,codigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM Product WHERE activo = '1' AND CodigoDeBarras = %s """
            cursor.execute(sql,codigoDeBarras)
            result = cursor.fetchall()
            return result

    def buscarProductoXnombre(self,nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM Product WHERE activo = '1' AND producto = %s """
            cursor.execute(sql,nombre)
            result = cursor.fetchall()
            return result

    def buscarProductoXcodigoB(self,codigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM Product WHERE activo = '0' AND CodigoDeBarras = %s """
            cursor.execute(sql,codigoDeBarras)
            result = cursor.fetchall()
            return result

    def buscarProductoXnombreB(self,nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM Product WHERE activo = '0' AND producto = %s """
            cursor.execute(sql,nombre)
            result = cursor.fetchall()
            return result

    def updateStock(self,cantidad,codigodebarras):
        with self.conn.cursor() as cursor:
            sql = """UPDATE product SET stock = stock + %s WHERE CodigoDeBarras = %s"""
            cursor.execute(sql,(cantidad,codigodebarras))
            self.conn.commit()

    
    def descontarStock(self,cantidad,codigodebarras):
        with self.conn.cursor() as cursor:
            sql = """UPDATE product SET stock = stock - %s
                     WHERE CodigoDeBarras = %s            
            """
            cursor.execute(sql,(cantidad,codigodebarras))
            self.conn.commit()

    def updateCostoCompra(self,valor,codigodebarras):
        with self.conn.cursor() as cursor:
            sql = """UPDATE product SET CostoDeCompra = %s, PrecioDeVenta = CostoDeCompra*1.7 WHERE CodigoDeBarras = %s"""
            cursor.execute(sql,(valor,codigodebarras))
            self.conn.commit()

    def autoCompleteCodProd(self,nombre):
        with self.conn.cursor() as cursor:
            sql ="""SELECT pr.CodigoDeBarras 
            FROM product pr, productoxproveedor pv, Proveedor p
            WHERE pr.codProducto = pv.codProducto      
            AND pv.codProveedor = p.codProveedor
            AND nombreProveedor = %s
            """
            cursor.execute(sql,nombre)
            result = cursor.fetchall()
            new_list_3 = [i[0] for i in result]
            #print(new_list)  #Test print
            self.model_1 = QStringListModel()
            self.model_1.setStringList(new_list_3)
            if self.model_1:
                return self.model_1

    def autoCompleteNameProd(self,nombre):
        with self.conn.cursor() as cursor:
            sql ="""SELECT pr.producto 
            FROM product pr, productoxproveedor pv, Proveedor p
            WHERE pr.codProducto = pv.codProducto      
            AND pv.codProveedor = p.codProveedor
            AND nombreProveedor = %s
            """
            cursor.execute(sql,nombre)
            result = cursor.fetchall()
            new_list_1 = [i[0] for i in result]
            #print(new_list)  #Test print
            self.model = QStringListModel()
            self.model.setStringList(new_list_1)
            if self.model:
                return self.model

    def actualizarCodBarra(self,producto,nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT pr.CodigoDeBarras 
            FROM Product 
            WHERE producto = %s
            AND pr.codProducto = pv.codProducto      
            AND pv.codProveedor = p.codProveedor
            AND nombreProveedor = %s
             """
            cursor.execute(sql,(producto,nombre))
            result = cursor.fetchone()
            return result
        
    def actualizarNombreProd(self,codBarra,nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT pr.producto 
            FROM Product pr, productoxproveedor pv, Proveedor p
            WHERE CodigoDeBarras = %s
            AND pr.codProducto = pv.codProducto      
            AND pv.codProveedor = p.codProveedor
            AND nombreProveedor = %s
             """
            cursor.execute(sql,(codBarra,nombre))
            result = cursor.fetchone()
            return result
        
    def autoComplete(self):
        with self.conn.cursor() as cursor:
            sql ="""SELECT producto FROM product WHERE activo = '1' """
            cursor.execute(sql)
            result = cursor.fetchall()
            new_list = [i[0] for i in result]
            #print(new_list)  #Test print
            self.model = QStringListModel()
            self.model.setStringList(new_list)
            if self.model:
                return self.model
    
    def autoComplete_2(self):
        with self.conn.cursor() as cursor:
            sql ="""SELECT producto FROM product WHERE activo = '0' """
            cursor.execute(sql)
            result = cursor.fetchall()
            new_list_2 = [i[0] for i in result]
            #print(new_list)  #Test print
            self.model_2 = QStringListModel()
            self.model_2.setStringList(new_list_2)
            if self.model_2:
                return self.model_2

                # Funciones de pantalla Control de stock

    def getStockActivos(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, codigoDeBarras, producto, marca, stock, PuntoDePedido, cant_min_stock 
            FROM Product 
            WHERE activo = '1' """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getStockBajo(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, codigoDeBarras, producto, marca, stock, PuntoDePedido, cant_min_stock 
            FROM Product 
            WHERE activo = '1'
            AND stock <= PuntoDePedido
             """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def buscarProductoStock(self,codigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, codigoDeBarras, producto, marca, stock, PuntoDePedido, cant_min_stock 
            FROM Product 
            WHERE activo = '1' 
            AND CodigoDeBarras = %s
            
             """
            cursor.execute(sql,codigoDeBarras)
            result = cursor.fetchall()
            return result
  
    def buscarNombreStock(self,nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, codigoDeBarras, producto, marca, stock, PuntoDePedido, cant_min_stock 
            FROM Product 
            WHERE activo = '1' 
            AND producto = %s
            
             """
            cursor.execute(sql,nombre)
            result = cursor.fetchall()
            return result
    
    def buscarProductoBajoStock(self,codigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, codigoDeBarras, producto, marca, stock, PuntoDePedido, cant_min_stock 
            FROM Product 
            WHERE activo = '1' 
            AND CodigoDeBarras = %s
            AND stock <= PuntoDePedido
             """
            cursor.execute(sql,codigoDeBarras)
            result = cursor.fetchall()
            return result
  
    def buscarNombreBajoStock(self,nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, codigoDeBarras, producto, marca, stock, PuntoDePedido, cant_min_stock 
            FROM Product 
            WHERE activo = '1' 
            AND producto = %s
            AND stock <= PuntoDePedido
             """
            cursor.execute(sql,nombre)
            result = cursor.fetchall()
            return result

    def autoComplete_3(self):
        with self.conn.cursor() as cursor:
            sql ="""SELECT producto 
            FROM product 
            WHERE activo = '1'
            AND stock <= PuntoDePedido
             """
            cursor.execute(sql)
            result = cursor.fetchall()
            new_list_2 = [i[0] for i in result]
            #print(new_list)  #Test print
            self.model_2 = QStringListModel()
            self.model_2.setStringList(new_list_2)
            if self.model_2:
                return self.model_2

#Productos por proveedor

    def productosDeProveedorXnombreProv(self,nombre):
        with self.conn.cursor() as cursor:
            sql = """SELECT pd.codProducto, pd.producto, pd.marca, pp.precio
            FROM Product pd, Proveedor pv, productoxproveedor pp
            WHERE pd.codProducto = pp.codProducto      
            AND pv.codProveedor = pp.codProveedor
            AND nombreProveedor = %s  
            order by pd.codProducto
             """
            cursor.execute(sql, nombre)
            result = cursor.fetchall()
            return result

    def productosDeProveedorXnroCuil(self,nroCuil):
        with self.conn.cursor() as cursor:
            sql = """SELECT pd.codProducto, pd.producto, pd.marca, pp.precio
            FROM Product pd, Proveedor pv, productoxproveedor pp
            WHERE pd.codProducto = pp.codProducto      
            AND pv.codProveedor = pp.codProveedor
            AND nroCuilCuit = %s  
            order by pd.codProducto
             """
            cursor.execute(sql, nroCuil)
            result = cursor.fetchall()
            return result

    def productosParaAgregar(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, producto, marca, CostoDeCompra
            FROM Product 
            WHERE activo = '1'      
             """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def AgregarxCod(self,codProducto):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProducto, producto, marca, CostoDeCompra
            FROM Product 
            WHERE activo = '1'
            AND codProducto = %s      
             """
            cursor.execute(sql, codProducto)
            result = cursor.fetchall()
            return result

    

    
