from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Proveedor():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS proveedor
                        (codProveedor INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        nroCuilCuit VARCHAR(12) NOT NULL,
                        nombreProveedor VARCHAR(45) NOT NULL,
                        nombreFactura VARCHAR(45) NOT NULL,
                        fechaAlta VARCHAR (10) NOT NULL, 
                        calle VARCHAR(45) NOT NULL,
                        numeroCalle VARCHAR(45) NOT NULL,
                        ciudad VARCHAR(45) NOT NULL,
                        codPostal VARCHAR(45) NOT NULL,
                        celular VARCHAR(45) NOT NULL,
                        email VARCHAR(45) NOT NULL,
                        pagWeb VARCHAR(45) NOT NULL,
                        activo BOOLEAN NOT NULL,
                        fechaBaja VARCHAR (10) NOT NULL,
                        codUsuario INT(10) NOT NULL
                        )
                        """
            cursor.execute(sql)
            self.conn.commit()

    def insertProveedor(self,nroCuil,nombreProveedor,nombreFactura,fechaAlta,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb,usuario):
        with self.conn.cursor() as cursor:
            activo= 1
            sql = """INSERT INTO proveedor (nroCuilCuit,nombreProveedor,nombreFactura,fechaAlta,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb,activo,codUsuario) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nroCuil,nombreProveedor,nombreFactura,fechaAlta,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb,activo,usuario))
            self.conn.commit()

    def getProveedor(self, nombreProveedor, estado):
        with self.conn.cursor() as cursor:
            sql = """SELECT *
            FROM proveedor 
            WHERE nombreProveedor = %s 
            AND activo = %s"""
            cursor.execute(sql, (nombreProveedor, estado))
            result = cursor.fetchone()
            if result:
                return result

    def getProveedor_2(self, nombreFacturacion, estado):
        with self.conn.cursor() as cursor:
            sql = """SELECT *
            FROM proveedor 
            WHERE nroCuilCuit  = %s 
            AND activo = %s"""
            cursor.execute(sql, (nombreFacturacion, estado))
            result = cursor.fetchone()
            if result:
                return result
                
    def autoComplete(self):
        with self.conn.cursor() as cursor:
            sql ="""SELECT nombreProveedor FROM proveedor"""
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
            sql ="""SELECT nroCuilCuit FROM proveedor"""
            cursor.execute(sql)
            result = cursor.fetchall()
            new_list_2 = [i[0] for i in result]
            #print(new_list)  #Test print
            self.model_2 = QStringListModel()
            self.model_2.setStringList(new_list_2)
            if self.model_2:
                return self.model_2


    def bajaProveedor(self,nombreProveedor,fechaBaja,usuario):
        with self.conn.cursor() as cursor:
            sql = """UPDATE proveedor SET activo = "0", fechaBaja = %s, codUsuario = %s WHERE nombreProveedor = %s"""
            cursor.execute(sql, (fechaBaja,usuario,nombreProveedor))
            self.conn.commit()

    def bajaProveedor2(self,cuil,fechaBaja,usuario):
        with self.conn.cursor() as cursor:
            sql = """UPDATE proveedor SET activo = "0",fechaBaja = %s, codUsuario =%s WHERE nroCuilCuit = %s"""
            cursor.execute(sql, (cuil,fechaBaja,usuario))
            self.conn.commit()

    def altaProveedor(self,nombreProveedor,fechaAlta,usuario):
        with self.conn.cursor() as cursor:
            sql = """UPDATE proveedor SET activo = "1",fechaAlta = %s, codUsuario =%s WHERE nombreProveedor = %s"""
            cursor.execute(sql, (fechaAlta,usuario,nombreProveedor))
            self.conn.commit()

    def getProveedoresActivos(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT  codProveedor, nroCuilCuit,nombreProveedor,nombreFactura,fechaAlta,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb,codUsuario
            FROM proveedor 
            WHERE activo = '1' """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getProveedoresBaja(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT codProveedor, nroCuilCuit,nombreProveedor,nombreFactura,fechaAlta,fechaBaja,celular,email,pagWeb,codUsuario 
            FROM proveedor 
            WHERE activo = '0' """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def UpdateProveedor(self,nroCuil,nombreProveedor, nombreFactura, calle, numeroCalle, ciudad, codPostal, celular, email, pagWeb):
        with self.conn.cursor() as cursor:
            
            sql = """UPDATE proveedor SET  nombreProveedor = %s,nombreFactura=%s ,calle = %s,numeroCalle = %s,ciudad = %s,codPostal = %s,celular = %s,email = %s,pagWeb = %s WHERE nroCuilCuit = %s """
            cursor.execute(sql,(nombreProveedor,nombreFactura,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb,nroCuil))
            self.conn.commit() 

    def insertProductos(self,codProducto,codProveedor,precio):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO productoxproveedor (codProducto,codProveedor,precio) VALUES (%s,%s,%s)"""
            cursor.execute(sql, (codProducto,codProveedor,precio))
            self.conn.commit()

    def deleteProductxProveedor(self,codProveedor):
        with self.conn.cursor() as cursor:
            sql = """DELETE  
            FROM productoxproveedor
            WHERE codProveedor = %s
            
            """
            cursor.execute(sql, codProveedor)
            self.conn.commit()