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
                        importeTotal VARCHAR (20) NOT NULL,
                        activo BOOLEAN NOT NULL,
                        motivoAnulacion VARCHAR (1000) NOT NULL,
                        anulo INT (10) NOT NULL,
                        codUsuario INT (10) NOT NULL
                        )

                        """
            cursor.execute(sql)
            self.conn.commit()

        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS tablaFacturaCompra
                        (
                        codTablaFactura INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        nroFacturaCompra VARCHAR (20) NOT NULL,
                        codCuilProv INT(12) NOT NULL,
                        fechaIngreso VARCHAR (10) NOT NULL, 
                        codProducto INT (8) NOT NULL,
                        codBarra VARCHAR(45) NOT NULL,
                        producto VARCHAR(45) NOT NULL,
                        cantidad INT(45) NOT NULL,
                        precioUnitario VARCHAR(45) NOT NULL,
                        subtotal VARCHAR(45) NOT NULL,
                        codFacturacompra INT (10) NOT NULL
                        )
                        """
            cursor.execute(sql)
            self.conn.commit()

    def insertFactCompra(self, tipoDoc, nombreProv, nroFactCompra, nroCuil, fechaEmision, fechaIngreso, tipoCompra, subtotal, descuento, iva, importeTotal,usuario):
        with self.conn.cursor() as cursor:
            activo = '1'
            sql = """INSERT INTO facturaCompra (tipoDoc, nombreProv, nroFacturaCompra, nroCuil, fechaEmision, fechaIngreso, tipoCompra, subtotal, descuento, iva, importeTotal,codUsuario, activo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (tipoDoc, nombreProv, nroFactCompra, nroCuil, fechaEmision, fechaIngreso, tipoCompra, subtotal, descuento, iva, importeTotal,usuario,activo))
            id = cursor.lastrowid
            self.conn.commit()
            return id

    def insertTabla(self, codfacturaCompra, nroFacturaCompra, codCuilProv, fechaIngreso, codProducto, codBarra, producto, cantidad, precioUnitario, subtotal):
        with self.conn.cursor() as cursor: 
            sql = """INSERT INTO tablaFacturaCompra (nroFacturaCompra,codCuilProv, fechaIngreso, codProducto, codBarra, producto, cantidad, precioUnitario, subtotal,codFacturacompra) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nroFacturaCompra, codCuilProv, fechaIngreso, codProducto, codBarra, producto, cantidad, precioUnitario, subtotal,codfacturaCompra))
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
            sql = """SELECT nroFacturaCompra, nroCuil, nombreProv, fechaEmision, fechaIngreso,codUsuario FROM facturacompra WHERE nombreProv = %s
            AND activo = '1'
            """
            cursor.execute(sql, (nombreProv))
            result = cursor.fetchall()
            return result

    def getFactByNum(self, numFact):
        with self.conn.cursor() as cursor:
            sql = """SELECT nroFacturaCompra, nroCuil, nombreProv, fechaEmision, fechaIngreso,codUsuario FROM facturacompra WHERE nroFacturaCompra = %s
            AND activo = '1'
            """
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
            sql = """SELECT codProducto, codBarra, producto, cantidad, precioUnitario, subtotal FROM tablafacturacompra WHERE nroFacturaCompra = %s"""
            cursor.execute(sql, (numFact))
            result = cursor.fetchall()
            return result
        
    def  insertMotivoCompra(self,motivo,nroFactura,anulo):
        with self.conn.cursor() as cursor:         
            sql = """UPDATE facturaCompra SET motivoAnulacion = %s, activo = '0', anulo = %s
            WHERE facturaCompra.nroFacturaCompra = %s
            """
            print(sql)
            cursor.execute(sql,(motivo,anulo,nroFactura))
            self.conn.commit()

    def anular_compra(self,nroFactura):
        with self.conn.cursor() as cursor:
            sql ="""UPDATE  product, tablaFacturaCompra, facturaCompra SET product.stock = product.stock - tablaFacturaCompra.cantidad 
                    WHERE facturaCompra.nroFacturaCompra = tablaFacturaCompra.nroFacturaCompra
                    AND product.codProducto = tablaFacturaCompra.codProducto 
                    AND  facturaCompra.nroFacturaCompra = %s          
                    """
            cursor.execute(sql,nroFactura)
            self.conn.commit()

        