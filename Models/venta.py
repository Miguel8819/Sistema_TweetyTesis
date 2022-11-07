class Venta():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS venta
                        (
                        codVenta INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        codCabecera INT (10) NOT NULL,
                        codProducto INT (10) NOT NULL,
                        cantidad VARCHAR(100) NOT NULL,
                        precioUnitario VARCHAR(100) NOT NULL 
                        
                        
                        )"""
            cursor.execute(sql)
            self.conn.commit()

   
    
    def getVentas(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getVenta(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta WHERE codVenta = %s"""
            cursor.execute(sql,cod)
            result = cursor.fetchone()
            if result:
                return result
    
    def updateVenta(self,table_venta):
        with self.conn.cursor() as cursor:
            sql = """UPDATE venta SET  cantidad = %s, descripcion= %s, precio_unit = %s, descuento = %s, total = %s, stock = %s, WHERE codigo = %s """
            cursor.execute(sql,( table_venta))
            self.conn.commit()

    def deleteVenta(self,cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM venta WHERE codVenta = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
    
    def insertVenta(self,codCabecera,codProducto,cantidad,precio):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO venta (codCabecera,codProducto,cantidad,precioUnitario) VALUES (%s,%s,%s,%s)"""
            cursor.execute(sql, (codCabecera,codProducto,cantidad,precio))
            self.conn.commit()