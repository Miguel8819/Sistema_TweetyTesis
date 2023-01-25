from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FacturaCompra():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS facturaCompra
                        (
                        codFactCompra INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        tipoDoc VARCHAR(40) NOT NULL,
                        nombreProv VARCHAR(40) NOT NULL,
                        nroFacturaCompra VARCHAR (20) NOT NULL,
                        nroCuil INT (12) NOT NULL,
                        fechaEmision VARCHAR (10) NOT NULL, 
                        fechaIngreso VARCHAR (10) NOT NULL,
                        tipoCompra VARCHAR (20) NOT NULL,
                        subtotal VARCHAR (20) NOT NULL,
                        descuento VARCHAR (20) NOT NULL,
                        iva VARCHAR (20) NOT NULL,
                        importeTotal VARCHAR (20) NOT NULL)
                        """
            cursor.execute(sql)
            self.conn.commit()

        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS tablaFacturaCompra
                        (
                        nroFacturaCompra VARCHAR (20) NOT NULL,
                        codCuilProv INT(12) NOT NULL,
                        fechaIngreso VARCHAR (10) NOT NULL, 
                        codProducto INT (8) NOT NULL,
                        codBarra VARCHAR(45) NOT NULL,
                        producto VARCHAR(45) NOT NULL,
                        cantidad INT(45) NOT NULL,
                        precioUnitario VARCHAR(45) NOT NULL,
                        subtotal VARCHAR(45) NOT NULL)
                        """
            cursor.execute(sql)
            self.conn.commit()

    def insertFactCompra(self, tipoDoc, nombreProv, nroFactCompra, nroCuil, fechaEmision, fechaIngreso, tipoCompra, subtotal, descuento, iva, importeTotal):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO facturaCompra (tipoDoc, nombreProv, nroFacturaCompra, nroCuil, fechaEmision, fechaIngreso, tipoCompra, subtotal, descuento, iva, importeTotal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (tipoDoc, nombreProv, nroFactCompra, nroCuil, fechaEmision, fechaIngreso, tipoCompra, subtotal, descuento, iva, importeTotal))
            self.conn.commit()
    
    def insertTabla(self, nroFacturaCompra, codCuilProv, fechaIngreso, codProducto, codBarra, producto, cantidad, precioUnitario, subtotal):
        with self.conn.cursor() as cursor: 
            sql = """INSERT INTO tablaFacturaCompra (nroFacturaCompra,codCuilProv, fechaIngreso, codProducto, codBarra, producto, cantidad, precioUnitario, subtotal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nroFacturaCompra, codCuilProv, fechaIngreso, codProducto, codBarra, producto, cantidad, precioUnitario, subtotal))
            self.conn.commit()

    def autoCompleteFacNum(self):
        with self.conn.cursor() as cursor:
            sql ="""SELECT nroFacturaCompra FROM facturacompra"""
            cursor.execute(sql)
            result = cursor.fetchall()
            new_list = [i[0] for i in result]
            #print(new_list)  #Test print
            self.model = QStringListModel()
            self.model.setStringList(new_list)
            if self.model:
                return self.model

    def getFactByProv(self, nombreProv):
        with self.conn.cursor() as cursor:
            sql = """SELECT nroFacturaCompra, nroCuil, nombreProv, fechaEmision, fechaIngreso FROM facturacompra WHERE nombreProv = %s"""
            cursor.execute(sql, (nombreProv))
            result = cursor.fetchall()
            return result

    def getFactByNum(self, numFact):
        with self.conn.cursor() as cursor:
            sql = """SELECT nroFacturaCompra, nroCuil, nombreProv, fechaEmision, fechaIngreso FROM facturacompra WHERE nroFacturaCompra = %s"""
            cursor.execute(sql, (numFact))
            result = cursor.fetchall()
            return result

    def getDetalleFactura(self, numFact):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM facturacompra WHERE nroFacturaCompra = %s"""
            cursor.execute(sql, (numFact))
            result = cursor.fetchall()
            return result

    def getDetalleTablaFactura(self, numFact):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM tablafacturacompra WHERE nroFacturaCompra = %s"""
            cursor.execute(sql, (numFact))
            result = cursor.fetchall()
            return result
        

    # def updateStock(self,stock,CodBarras):
    #     with self.conn.cursor() as cursor:
    #         sql= """UPDATE product SET stock = %s WHERE CodigoDeBarras = %s"""
    #         cursor.execute(sql,(stock,CodBarras))
    #         self.conn.commit